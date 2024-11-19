from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/medical_records", tags=["Medical Records"])

@router.post("/", response_model=schemas.MedicalRecordResponse)
def create_medical_record(record: schemas.MedicalRecordCreate, db: Session = Depends(get_db)):
    appointment = db.query(models.Appointment).filter(models.Appointment.id == record.appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    medical_record = models.MedicalRecord(**record.dict())
    db.add(medical_record)
    db.commit()
    db.refresh(medical_record)
    return medical_record

@router.get("/{record_id}", response_model=schemas.MedicalRecordResponse)
def get_medical_record(record_id: int, db: Session = Depends(get_db)):
    medical_record = db.query(models.MedicalRecord).filter(models.MedicalRecord.id == record_id).first()
    if not medical_record:
        raise HTTPException(status_code=404, detail="Medical Record not found")
    return medical_record

@router.delete("/{record_id}")
def delete_medical_record(record_id: int, db: Session = Depends(get_db)):
    medical_record = db.query(models.MedicalRecord).filter(models.MedicalRecord.id == record_id).first()
    if not medical_record:
        raise HTTPException(status_code=404, detail="Medical Record not found")
    
    db.delete(medical_record)
    db.commit()
    return {"detail": "Medical Record deleted"}
