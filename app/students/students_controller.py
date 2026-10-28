from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.shared.database import get_db
from app.students import students_repository, students_schemas

router = APIRouter(prefix="/students", tags=["students"])

@router.get("/", response_model=list[students_schemas.StudentResponse])
def read_students(db: Session = Depends(get_db)):
    return students_repository.get_students(db)

@router.post("/", response_model=students_schemas.StudentResponse)
def create_new_student(student: students_schemas.StudentCreate, db: Session = Depends(get_db)):
    return students_repository.create_student(db=db, student=student)