from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from api import choices
from api.services import exceptions as service_exc
from api.utils import exceptions as utils_exc
from api.utils.dto import TokenData
from api.utils.jwt_tool import jwt_tool

security = HTTPBearer()


class TokenValidator:
    def __init__(self, role_name: choices.Role | None = None):
        self.role_name = role_name

    def __call__(
        self, credentials: HTTPAuthorizationCredentials = Depends(security)
    ) -> TokenData:
        token = credentials.credentials
        try:
            token_data: TokenData = jwt_tool.decode_token(token)
            if not self.role_name or token_data.role_name == self.role_name:
                return token_data
            else:
                raise service_exc.UnauthorizedError(
                    detail=f"You must have role {self.role_name.value}"
                )
        except utils_exc.JWTToolError as e:
            raise service_exc.UnauthorizedError(detail=e.detail) from e
