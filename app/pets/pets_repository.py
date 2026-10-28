from collections.abc import Iterator
from contextlib import contextmanager

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.pets.pets_model import PetModel
from app.pets.pets_schemas import Pet
from app.shared.database import SessionLocal


@contextmanager
def _session(db: Session | None) -> Iterator[tuple[Session, bool]]:
    """Entrega (sesión, es_propia). Si no te pasan sesión, abre una."""
    if db is not None:
        yield db, False
        return
    with SessionLocal() as own:
        yield own, True


def _to_schema(row: PetModel) -> Pet:
    return Pet(
        id=row.id,
        studentId=row.student_id,
        name=row.name,
        species=row.species,
        age=row.age,
        createdAt=row.created_at,
        updatedAt=row.updated_at,
    )


class PetsRepository:
    def find_all_by_student(
        self, student_id: str, db: Session | None = None
    ) -> list[Pet]:
        with _session(db) as (s, _):
            rows = s.scalars(
                select(PetModel).where(PetModel.student_id == student_id)
            ).all()
            return [_to_schema(r) for r in rows]

    def find_by_id(self, pet_id: str, db: Session | None = None) -> Pet | None:
        with _session(db) as (s, _):
            row = s.get(PetModel, pet_id)
            return _to_schema(row) if row else None

    def find_by_student_and_name(
        self, student_id: str, name: str, db: Session | None = None
    ) -> Pet | None:
        with _session(db) as (s, _):
            row = s.scalars(
                select(PetModel).where(
                    PetModel.student_id == student_id, PetModel.name == name
                )
            ).first()
            return _to_schema(row) if row else None

    def save(self, pet: Pet, db: Session | None = None) -> Pet:
        with _session(db) as (s, owned):
            row = s.get(PetModel, pet.id)
            if row is None:
                row = PetModel(id=pet.id)
                s.add(row)
            row.student_id = pet.studentId
            row.name = pet.name
            row.species = pet.species
            row.age = pet.age
            row.created_at = pet.createdAt
            row.updated_at = pet.updatedAt
            s.flush()
            result = _to_schema(row)
            if owned:
                s.commit()
            return result

    def delete(self, pet_id: str, db: Session | None = None) -> None:
        with _session(db) as (s, owned):
            s.execute(delete(PetModel).where(PetModel.id == pet_id))
            if owned:
                s.commit()
            else:
                s.flush()

    def delete_by_student(self, student_id: str, db: Session | None = None) -> None:
        with _session(db) as (s, owned):
            s.execute(delete(PetModel).where(PetModel.student_id == student_id))
            if owned:
                s.commit()
            else:
                s.flush()


pets_repository = PetsRepository()