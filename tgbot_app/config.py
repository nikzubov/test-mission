from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    T_TOKEN: str
    R_PASSWORD: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
