import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get("http://api.github.com/zen")
    print(r.text)


