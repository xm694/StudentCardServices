import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from jose.backends import RSAKey
from jose.constants import ALGORITHMS
from typing import Optional

SECRET_KEY = "f03f0d5cdfadaaba51dba7f14c85422c98bda1521a78abb7186e069502ed14d7"  
ALGORITHM = "HS256"  

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
       # Extract details from the payload
        user_id: int = payload.get("id")
        email: str = payload.get("sub")
        first_name: str = payload.get("first_name")
        last_name: str = payload.get("last_name")
        permissions: str = payload.get("permissions")

        # Check for necessary attributes
        if not email or not permissions:
            raise credentials_exception
        
        # Return the details
        return {
            "id": user_id,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "permissions": permissions,
        }
    except JWTError:
        raise credentials_exception

def is_admin(current_user: dict = Depends(get_current_user)) -> dict:
    if current_user["permissions"] != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access forbidden: Admins only")
    return current_user

def is_user(current_user: dict = Depends(get_current_user)) -> dict:
    if current_user["permissions"] != "user":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access forbidden: Users only")
    return current_user
