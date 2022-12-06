import pytest
import Pytest.Calculator as Cal


def test_add():
    assert Cal.add(10, 5) == 15


def test_sub():
    assert Cal.sub(20, 10) == 10


@pytest.mark.skip(reason="No need multiple this iteration")
def test_multiply():
    assert Cal.multiply(10, 5) == 50


def test_division():
    assert Cal.division(100, 50) == 2

# pytest --html=report.html
