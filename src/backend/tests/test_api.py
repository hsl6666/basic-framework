from fastapi.testclient import TestClient

from app.main import create_app


def test_health_endpoint_returns_service_status():
    client = TestClient(create_app())

    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {
        "service": "backend-scaffold",
        "status": "ok",
        "version": "0.1.0",
    }


def test_chat_endpoint_returns_langgraph_response():
    client = TestClient(create_app())

    response = client.post(
        "/api/v1/chat",
        json={"message": "hello", "session_id": "test-session"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["session_id"] == "test-session"
    assert body["engine"] == "langgraph-local"
    assert "hello" in body["answer"]
    assert body["frameworks"]["langgraph"] is True
    assert body["frameworks"]["langchain"] is True
    assert body["frameworks"]["deepagents"] is True


def test_chat_endpoint_rejects_empty_messages():
    client = TestClient(create_app())

    response = client.post("/api/v1/chat", json={"message": ""})

    assert response.status_code == 422
