import Pytest.Calculator as Cal
import pytest


@pytest.mark.smokeAddTest
def test_add():
    assert Cal.add(100, 50) == 150


def test_multiply():
    assert Cal.multiply(10, 5) == 50


def test_division():
    assert Cal.division(100, 50) == 2
