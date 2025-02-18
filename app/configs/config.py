from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRETKEY: str

    DB_USER: str
    DB_HOST: str
    DB_PASS: str
    DB_NAME: str

    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_HOST: str
    TEST_DB_NAME: str

    MODE: str
    model_config = SettingsConfigDict(env_file=".env")

    @property
    def db_url(self):
        if self.MODE == "TEST":
            return f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}/{self.TEST_DB_NAME}"
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}/{self.DB_NAME}"


settings = Settings()
