import uuid
from typing import Generic, TypeVar

from pydantic import BaseModel

from api.services.schemas.base import BaseServiceSchema

ServiceSchema = TypeVar("ServiceSchema", bound=BaseServiceSchema)
ApiSchema = TypeVar("ApiSchema", bound="BaseApiSchema")


class BaseApiSchema(BaseModel, Generic[ServiceSchema]):
    @classmethod
    def from_service_schema(cls, service_schema: ServiceSchema) -> ApiSchema:
        raise NotImplementedError

    def to_service_schema(self, **kwargs) -> ServiceSchema:
        raise NotImplementedError


class IdApiSchemaMixin(BaseModel):
    id: uuid.UUID
