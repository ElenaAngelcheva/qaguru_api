import pytest

@pytest.fixture()
def create_user(request):
    return {
        "name": str(request.param[0]),
        "job": str(request.param[1])
    }
