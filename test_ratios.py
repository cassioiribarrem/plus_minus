from unittest import TestCase
from main import plusMinus

class TestPlusMinus(TestCase):
    def tests_if_the_plus_minus_class_exists(self):
        if plusMinus(1, [1]):
            return

    def tests_the_receiving_of_parameters(self):
         function = plusMinus(3, [1, 2, 3])
         assert function.n == 3 and function.arr == [1, 2, 3]

    def tests_the_counting_of_positive_numbers(self):
        function = plusMinus(3, [1, 2, 3])
        assert function.positive_numbers() == 3

    def test_the_counting_of_negative_numbers(self):
        function = plusMinus(4, [0, 1, -1, 2])
        assert function.negative_numbers() == 1

    def test_the_counting_of_nule_numbers(self):
        function = plusMinus(4, [0, -1, 1, 0])
        assert function.nule_numbers() == 2

    def test_the_calculating_of_ratios(self):
        function = plusMinus(4, [-1, 0, 1, 2])
        assert function.ratios() == (0.5, 0.25, 0.25)