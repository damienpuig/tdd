
class Calculator(object):

    def __init__(self, nb1, nb2):
        self.number1 = nb1
        self.number2 = nb2

    def sum(self):
        return self.number1 + self.number2

    def divide_sum_by(self, nb):

        s = self.sum()

        result = s / nb

        return result
