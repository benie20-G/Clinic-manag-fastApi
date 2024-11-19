from fastapi import FastAPI
from app.database import engine, Base
from app.routers import patients, doctors, appointments, billing

app = FastAPI(title="Clinic Management System")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(appointments.router)
app.include_router(billing.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Clinic Management API"}
