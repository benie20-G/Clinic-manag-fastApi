from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/billing", tags=["Billing"])

@router.post("/", response_model=schemas.BillingResponse)
def create_billing(billing: schemas.BillingCreate, db: Session = Depends(get_db)):
    new_billing = models.Billing(**billing.dict())
    db.add(new_billing)
    db.commit()
    db.refresh(new_billing)
    return new_billing

@router.get("/{billing_id}", response_model=schemas.BillingResponse)
def get_billing(billing_id: int, db: Session = Depends(get_db)):
    billing = db.query(models.Billing).filter(models.Billing.id == billing_id).first()
    if not billing:
        raise HTTPException(status_code=404, detail="Billing record not found")
    return billing

@router.get("/", response_model=list[schemas.BillingResponse])
def list_billing(db: Session = Depends(get_db)):
    return db.query(models.Billing).all()

# Update a billing's information
@router.put("/{billing_id}", response_model=schemas.BillingResponse)
def update_billing(billing_id: int, updated_billing: schemas.BillingCreate, db: Session = Depends(get_db)):
    billing = db.query(models.Billing).filter(models.Billing.id == billing_id).first()
    if not billing:
        raise HTTPException(status_code=404, detail="Billing not found")
    for key, value in updated_billing.dict().items():
        setattr(billing, key, value)
    db.commit()
    db.refresh(billing)
    return billing

@router.delete("/{billing_id}", status_code=204)
def delete_billing(billing_id: int, db: Session = Depends(get_db)):
    billing = db.query(models.Billing).filter(models.Billing.id == billing_id).first()
    if not billing:
        raise HTTPException(status_code=404, detail="Billing record not found")
    db.delete(billing)
    db.commit()
