import unittest
from parameterized import parameterized
from add import add
class TestCal(unittest.TestCase):
    """
    """
    @parameterized.expand[

        ((20,20), 1)
    ]

    def test_add(self):
        self.assertEqual(add(20,20), 40)
        self.assertEqual(add(firstnumber, secondnumber), result)


if '__name__' == '__main__':
    unittest.main()
