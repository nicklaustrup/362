import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):
    def test1(self):
        contrived_func(0)

    def test2(self):
        contrived_func(1)

    def test3(self):
        contrived_func(-1)

    def test4(self):
        contrived_func(16.5)

    def test5(self):
        contrived_func(20)

    def test6(self):
        contrived_func(21)

    def test7(self):
        contrived_func(-2)

    def test8(self):
        contrived_func(22)


if __name__ == '__main__':
    unittest.main()
