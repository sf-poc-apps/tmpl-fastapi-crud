from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    assert client.get("/healthz").text == "ok"


def test_banner_on_index():
    r = client.get("/")
    assert r.status_code == 200
    assert "sf-banner.js" in r.text


def test_create_and_delete_item():
    r = client.post("/items", data={"name": "First", "note": "hello"}, follow_redirects=False)
    assert r.status_code == 303
    assert "First" in client.get("/").text
