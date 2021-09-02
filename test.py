"""
pytest
"""
from app import app


def test1():
    """A dummy docstring."""
    response = app.test_client().get("/")
    assert response.status_code == 200


def test2():
    """A dummy docstring."""
    response = app.test_client().get("/edit")
    assert response.status_code == 200


def test3():
    """A dummy docstring."""
    response = app.test_client().get("/edit")
    assert b"To Do App" in response.data
    assert b"Todo Title" in response.data
    assert b"Add" in response.data


#    assert b"Project" in response.data
