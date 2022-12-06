import pytest


@pytest.mark.parametrize("num, output", [(1, 11), (2, 12), (10, 20)])
def test_sum(num, output):
    assert 10 + num == output
