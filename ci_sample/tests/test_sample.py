from fastapi import Response
from fastapi.testclient import TestClient

from ci_sample.main import app
client = TestClient(app)

def test_1():
    resp: Response = client.get('/ping')
    assert resp.status_code == 200

def test_must_fail():
    resp: Response = client.get('/na')
    assert resp.status_code == 404