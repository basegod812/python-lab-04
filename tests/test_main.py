import unittest
from main import filter_evens, factorial, fibonacci, repeat


class TestFunctionalLab(unittest.TestCase):
    def test_filter(self):
        self.assertEqual(filter_evens([1, 2, 3, 4]), [2, 4])

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)

    def test_memoization(self):
        self.assertEqual(fibonacci(20), 6765)
        self.assertIn((20,), fibonacci.cache)

    def test_parameterized_decorator(self):
        calls = []
        @repeat(3)
        def record():
            calls.append(1)
            return len(calls)
        self.assertEqual(record(), 3)
        self.assertEqual(len(calls), 3)


if __name__ == "__main__":
    unittest.main()
