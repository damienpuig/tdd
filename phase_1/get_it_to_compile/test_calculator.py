from __future__ import with_statement
from phase_1.get_it_to_compile.calculator import Calculator


class TestCalculator(object):

    def test_initiate_calculator(self):
        nb1 = 1
        nb2 = 2

        calculator = Calculator(nb1, nb2)

        assert calculator.number1 == nb1
        assert calculator.number2 == nb2

    def test_sum(self):
        nb1 = 1
        nb2 = 2

        calculator = Calculator(nb1, nb2)

        assert (nb1 + nb2) == calculator.sum()

    def test_divide_sum_by(self):

        nb1 = 1
        nb2 = 2
        divide_nb = 3

        calculator = Calculator(nb1, nb2)

        assert calculator.divide_sum_by(divide_nb) == 1