from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from typing import List 

router = APIRouter(prefix="/patients", tags=["Patients"])

# Create a new patient
@router.post("/", response_model=schemas.PatientResponse)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    new_patient = models.Patient(**patient.dict())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

# Get a single patient by ID
@router.get("/{patient_id}", response_model=schemas.PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

# List all patients
@router.get("/", response_model=List[schemas.PatientResponse])
def list_patients(db: Session = Depends(get_db)):
    return db.query(models.Patient).all()

# Update a patient's information
@router.put("/{patient_id}", response_model=schemas.PatientResponse)
def update_patient(patient_id: int, updated_patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    for key, value in updated_patient.dict().items():
        setattr(patient, key, value)
    db.commit()
    db.refresh(patient)
    return patient

# Delete a patient
@router.delete("/{patient_id}", response_model=dict)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    db.delete(patient)
    db.commit()
    return {"detail": "Patient deleted successfully"}
