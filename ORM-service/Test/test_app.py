import pytest
import requests


def test_my_json_response():
    r = requests.get("http://localhost:8004/api/v1/exact/17")
    assert r.status_code == 200
    assert r.json is not None
    print(r.json())
    # assert r.json()[0]['simproId'] is not None
