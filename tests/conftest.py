import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.configs import settings
from app.db import Base, get_session
from main import app

TEST_DATABASE_URL = settings.db_url

test_engine = create_async_engine(TEST_DATABASE_URL, echo=True)
TestSession = async_sessionmaker(bind=test_engine, expire_on_commit=False)


@pytest_asyncio.fixture(autouse=True)
async def setup_test_db():
    async with test_engine.begin() as c:
        await c.run_sync(Base.metadata.create_all)
        yield

    async with test_engine.begin() as c:
        await c.run_sync(Base.metadata.drop_all)


async def test_session():
    async with TestSession() as session:
        yield session


@pytest_asyncio.fixture(autouse=True)
async def replace_get_session():
    app.dependency_overrides[get_session] = test_session
