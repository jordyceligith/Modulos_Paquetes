import pytest

from temperaturas.temp_convrt import F_to_K, C_to_R,C_to_F

@pytest.mark.parametrize(
    "f, k",
    [
        (0, 255.3722222222222),
        (12, 262.0388888888889),
        (40, 277.59444444444443)
   
    ]
)

def test_convertior(f, k):
    print(F_to_K(f))
    assert F_to_K(f) == k

@pytest.mark.parametrize(
    "c, r",
    [
        (2, 495.27000000000004),
        (23, 533.07),
        (30, 545.6700000000001)
    ]
)

def test_convertior(c, r):
    print(C_to_R(c))
    assert C_to_R(c) == r

@pytest.mark.parametrize(
    "c, f",
    [
        (2, 35.6),
        (23, 73.4),
        (30, 86.0)
    ]
)

def test_convertior(c, f):
    print(C_to_F(c))
    assert C_to_F(c) == f

