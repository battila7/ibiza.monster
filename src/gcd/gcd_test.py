import math
from hypothesis import given
from hypothesis.strategies import integers

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

@given(integers(min_value = 1), integers(min_value = 1))
def test(a, b):
    assert gcd(a, b) == math.gcd(a, b)

test()
