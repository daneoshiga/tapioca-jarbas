import pytest

from tapioca_jarbas import Jarbas


@pytest.fixture
def wrapper():
    return Jarbas()


def test_resource_access(wrapper):
    resource = wrapper.documents()
    assert resource.data == 'http://jarbas.datasciencebr.com/api/document/'
