import pytest
from httpx import AsyncClient, ASGITransport
from main import app

url = "http://127.0.0.1:8080"

data = {"username": "muhammad", "email": "example@asd.com", "password": "13cd45678"}


@pytest.mark.asyncio
async def test_process():
    async with AsyncClient(transport=ASGITransport(app=app), base_url=url) as ac:
        response = await ac.post("/auth/sign-up/", json=data)

        assert response.status_code == 400
        # assert "access_token" in response.json()

        response = await ac.get("/users/muhammad")

        assert response.status_code == 200
        assert response.json() == data

        response = await ac.get("/users/maam")

        assert response.status_code == 404
