from fastapi import APIRouter, Depends, HTTPException
from models import User
from dependencies import get_session
from main import bcrypt_context
from schemas import UserSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def Home():
    """
    Rota de autenticação
    """
    return {"message": "Sign in endpoint"}  

@auth_router.post("/create_account")
async def create_account(user_schema: UserSchema, session: Session = Depends(get_session)):
    user = session.query(User).filter(User.email==user_schema.email).first()    
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        cripted_password = bcrypt_context.hash(user_schema.password)
        new_user = User(name=user_schema.name, email=user_schema.email, password=cripted_password)
        session.add(new_user)
        session.commit()
        return {"message": f"User created successfully: {new_user.email}"}