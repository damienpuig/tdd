
class Calculator(object):

    def __init__(self, nb1, nb2):
        self.number1 = nb1
        self.number2 = nb2

    def sum(self):
        s = self.number1 + self.number2

        return s

    def divide_sum_by(self, nb):

        s = self.number1 + self.number2

        result = s / nb

        return result
