from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from enum import Enum


# Enum for Gender to standardize male/female options
class GenderEnum(str, Enum):
    male = "male"
    female = "female"


class PatientBase(BaseModel):
    name: str
    date_of_birth: datetime
    email: str
    gender: GenderEnum
    address: Optional[str] = 'Not Provided'
    phone: str


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):
    id: int

    class Config:
        orm_mode = True


class DoctorBase(BaseModel):
    name: str
    specialty: str
    email: str
    contact_number: Optional[str] = None


class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    id: int

    class Config:
        orm_mode = True


class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    symptoms: Optional[str] = None


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    id: int

    class Config:
        orm_mode = True


class BillingBase(BaseModel):
    appointment_id: int
    amount: int
    is_paid: Optional[bool] = False


class BillingCreate(BillingBase):
    pass


class BillingResponse(BillingBase):
    id: int

    class Config:
        orm_mode = True


class MedicalRecordBase(BaseModel):
    diagnosis: str
    treatment: str


class MedicalRecordCreate(MedicalRecordBase):
    appointment_id: int


class MedicalRecordResponse(MedicalRecordBase):
    id: int
    appointment_id: int

    class Config:
        orm_mode = True
