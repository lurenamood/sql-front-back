# api/app/models/user_model.py

# Modelo de datos (puede representar cómo están en la DB)
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    status: str  # Podrías usar Enum para 'active', 'inactive'


