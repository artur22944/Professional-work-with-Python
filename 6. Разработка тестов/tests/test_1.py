import unittest
import task_1


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for i, (a, b, c, expected) in enumerate([
            (1, 8, 15, (-3, -5)),
            (1, -13, 12, (12, 1)),
            (-4, 28, -49, 3.5),
            (1, 1, 1, 'корней нет'),
        ]):
            with self.subTest(i):
                result = task_1.solution(a, b, c)
                self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
