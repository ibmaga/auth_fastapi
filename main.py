from fastapi import FastAPI
import logfire

from app.api.routes.auth import router as auth_router
from app.api.routes.users import router as users_router


app = FastAPI()
logfire.configure()
logfire.instrument_fastapi(app)

app.include_router(auth_router)
app.include_router(users_router)
