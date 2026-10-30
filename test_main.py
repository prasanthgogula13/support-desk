from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
def test_create_ticket_endpoint():
    response = client.post(
        "/tickets",
        json={
            "title": "  Unable to connect to VPN  ",
            "description": "  Connection fails from home.  ",
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        "title": "Unable to connect to VPN",
        "description": "Connection fails from home.",
        "status": "open",
    }


def test_create_ticket_endpoint_rejects_blank_title():
    response = client.post(
        "/tickets",
        json={
            "title": "   ",
            "description": "Connection fails from home.",
        },
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"][-1] == "title"


def test_create_ticket_endpoint_rejects_missing_description():
    response = client.post(
        "/tickets",
        json={
            "title": "Unable to connect to VPN",
        },
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"][-1] == "description"


def test_create_ticket_endpoint_rejects_non_string_title():
    response = client.post(
        "/tickets",
        json={
            "title": 123,
            "description": "Connection fails from home.",
        },
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"][-1] == "title"
