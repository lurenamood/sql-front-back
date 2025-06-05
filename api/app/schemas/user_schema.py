# api/app/schemas/user_schema.py

from pydantic import BaseModel

# This class defines the structure of a User returned by the API (e.g., via GET)
class User(BaseModel):
    id: int               # Unique user ID
    US_email: str         # User's email address
    US_name: str          # User's first name
    US_surname: str       # User's last name
    status: str           # Account status: 'active' or 'inactive'

# This class is used when updating user data (PUT or PATCH)
class UserUpdate(BaseModel):
    US_id: int            # User ID to update
    US_name: str          # New first name
    US_surname: str       # New last name
    US_email: str         # New email address
