import pytest

# パラメータライズで異なる値をテスト
@pytest.mark.parametrize("input, expected", [(1, 2), (2, 4), (3, 6)])
def test_multiply(input, expected):
    assert input * 2 == expected
