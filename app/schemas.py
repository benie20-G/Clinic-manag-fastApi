from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class PatientBase(BaseModel):
    name: str
    address: Optional[str] = 'Not Provided'
    phone: str

class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attribute = True


class DoctorBase(BaseModel):
    name: str
    specialty: str

class DoctorCreate(DoctorBase):
    pass

class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attribute = True


class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    symptoms: Optional[str]

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentResponse(AppointmentBase):
    id: int

    class Config:
        from_attribute = True


class BillingBase(BaseModel):
    appointment_id: int
    amount: int

class BillingCreate(BillingBase):
    pass

class BillingResponse(BillingBase):
    id: int

    class Config:
        from_attribute = True


class MedicalRecordBase(BaseModel):
    diagnosis: str
    treatment: str

class MedicalRecordCreate(MedicalRecordBase):
    appointment_id: int

class MedicalRecordResponse(MedicalRecordBase):
    id: int
    appointment_id: int

    class Config:
        from_attributes = True