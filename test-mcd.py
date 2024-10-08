import unittest

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcd_4(a, b, c, d):
    return mcd(mcd(mcd(a, b), c), d)


class TestOperaciones(unittest.TestCase):
    def test_mcd4(self):
        esperado = 3
        actual = mcd_4(3, 12, 24, 36)
        self.assertEqual(actual, esperado)


if __name__ == '__main__':
    unittest.main()

