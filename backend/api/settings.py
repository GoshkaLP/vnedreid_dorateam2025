from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


def get_model_config(env_prefix: str = "") -> SettingsConfigDict:
    return SettingsConfigDict(env_prefix=env_prefix, env_file=".env", extra="ignore")


class AppSettings(BaseSettings):
    name: str = "VNEDREID DORATEAM"
    version: str = "1.0.0"
    title: str = "VNEDREID DORATEAM"
    summary: str = "VNEDREID DORATEAM API SOLUTION"


class PostgresSettings(BaseSettings):
    host: str
    port: int
    password: str
    user: str
    db: str
    db_schema: str

    @property
    def connection_url(self) -> str:
        url = URL.create(
            "postgresql",
            username=self.user,
            password=self.password,
            host=self.host,
            database=self.db,
        )
        return url.render_as_string(hide_password=False)

    model_config = get_model_config("postgres_")


class JWTSettings(BaseSettings):
    secret_key: str

    model_config = get_model_config("jwt_")


class OpenrouterSettings(BaseSettings):
    url: str
    token: str
    model: str

    model_config = get_model_config("openrouter_")


class OrionSoftGPTSettings(BaseSettings):
    token: str
    username: str
    url: str
    salt: str

    model_config = get_model_config("orionsoftgpt_")


app_settings = AppSettings()
postgres_settings = PostgresSettings()
jwt_settings = JWTSettings()
openrouter_settings = OpenrouterSettings()
orionsoftgpt_settings = OrionSoftGPTSettings()
