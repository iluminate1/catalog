from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = True
    secret_key: str = "ca4ef18501748e41762538ff12a98dfe"


class DatabaseConfig(BaseModel):
    name: str = "db"
    user: str = "user"
    password: str = "pass"
    host: str = "localhost"
    port: int = 5432
    echo: bool = False


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
        case_sensitive=False,
        env_prefix="BACKEND__",
        env_ignore_empty=True,
        extra="ignore",
    )
    app: AppConfig = AppConfig()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()
