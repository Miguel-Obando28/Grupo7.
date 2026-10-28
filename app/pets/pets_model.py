from datetime import datetime

from sqlalchemy import DateTime, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.shared.database import Base


class PetModel(Base):
 __tablename__ = "pets"
__table_args__ = (
UniqueConstraint("student_id", "name", name="uq_pet_name_per_student"),
)

id: Mapped[str] = mapped_column(String(36), primary_key=True)
student_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
name: Mapped[str] = mapped_column(String(50), nullable=False)
species: Mapped[str] = mapped_column(String(50), nullable=False)
age: Mapped[int | None] = mapped_column(Integer, nullable=True)
created_at: Mapped[datetime] = mapped_column(
DateTime(timezone=True), nullable=False
)
updated_at: Mapped[datetime] = mapped_column(
DateTime(timezone=True), nullable=False
)