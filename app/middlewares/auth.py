import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta


class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = "secret"

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hash_password: str):
        return self.pwd_context.verify(plain_password, hash_password)

    def create_access_token(self, user_id: int) -> str:
        payload = {
            "exp": datetime.utcnow() + timedelta(days=0, minutes=5),
            "iat": datetime.utcnow(),
            "sub": user_id,
        }
        return {
            "access_token": jwt.encode(payload, self.secret, algorithm="HS256"),
            "token_type": "bearer",
        }

    def decode_token(self, token: str):

        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            return payload["sub"]

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Signature has expired")
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail="Invalid token")

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):

        return self.decode_token(auth.credentials)


auth = AuthHandler()
