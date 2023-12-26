import pytest


@pytest.fixture(scope='function', autouse=True)
def hook(request):
#    print("\nbefore test")
    yield
#    print("\nafter test")


@pytest.fixture(scope='session', autouse=True)
def suite(request):
#    print("\nbefore all")
    yield
#    print("\nafter all")
