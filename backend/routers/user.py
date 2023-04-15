import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2
from .. database import get_db
from ..models import User

router = APIRouter()


@router.get("/me", response_model=schemas.UserResponse)
def get_user_info(db: Session = Depends(get_db), user_id: str = Depends(oauth2.require_user)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user


@router.delete("/{user_id}")
def delete_user(user_id: uuid.UUID, db: Session = Depends(get_db),
                current_user: User = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="You do not have permission to delete this user")

    db.delete(user)
    db.commit()
    return {"message": "User deleted"}
