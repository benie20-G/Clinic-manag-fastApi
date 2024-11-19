from sqlalchemy import Column,Boolean, Integer, String, ForeignKey, Text, DateTime,CheckConstraint
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import Enum
import enum


# class GenderEnum(enum.Enum):
#     male = "male"
#     female = "female" 

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    date_of_birth =Column(DateTime,nullable=False)
    email = Column(String(100),nullable=False, unique=True)
    gender = Column(String, nullable=False)
    address = Column(String(255), default='Not Provided')
    phone = Column(String(20), nullable=False)

    appointments = relationship("Appointment", back_populates="patient")
    __table_args__ = (
        CheckConstraint("gender IN ('male', 'female')", name="check_gender"),
    )

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    specialty = Column(String(100), nullable=False)
    email = Column(String(100),nullable=False,unique=True)
    contact_number = Column(String(100),unique=True)

    appointments = relationship("Appointment", back_populates="doctor")


class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    symptoms = Column(Text, nullable=True)

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
    medical_record = relationship("MedicalRecord", uselist=False, back_populates="appointment")

class Billing(Base):
    __tablename__ = 'billings'
    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey('appointments.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    is_paid = Column(Boolean,default=False)

    appointment = relationship("Appointment")

class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id", ondelete="CASCADE"))
    diagnosis = Column(Text, nullable=False)
    treatment = Column(Text, nullable=False)

    # Relationship to the Appointment model
    appointment = relationship("Appointment", back_populates="medical_record")