from __future__ import with_statement
import pytest
from phase_2.get_to_compile.calculator import Calculator
from entry_error import EntryError


class TestCalculator(object):

    def SetUp(self):
        self.nb1 = 1
        self.nb2 = 2
        self.calculator = Calculator(self.nb1, self.nb2)

    def Teardown(self):
        pass

    def test_initiate_calculator(self):
        self.SetUp()

        assert self.calculator.number1 == self.nb1
        assert self.calculator.number2 == self.nb2

        self.Teardown()

    def test_sum(self):
        self.SetUp()

        assert (self.nb1 + self.nb2) == self.calculator.sum()

    def test_divide_sum_by(self):
        self.SetUp()

        divide_nb = 3

        assert self.calculator.divide_sum_by(divide_nb) == 1


        divide_nb = None

        with pytest.raises(EntryError):
            self.calculator.divide_sum_by(divide_nb)


        divide_nb = 0

        with pytest.raises(EntryError):
            self.calculator.divide_sum_by(divide_nb)