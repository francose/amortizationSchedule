import pandas as pd
import numpy as np
from datetime import date
from typing import Callable, List
from abc import ABC, abstractclassmethod, abstractmethod


class CalculateAmortizationSchedule(ABC):

    def __init__(self, interestRate: int, terms_of_Loans: int, frequency_of_Payment: int, loan_Amount: int) -> int:
        try:
            self.interestRate = interestRate/100
            self.terms_of_Loans = terms_of_Loans * frequency_of_Payment
            self.loan_Amount = loan_Amount
            self.frequency_of_Payment = frequency_of_Payment
            super(CalculateAmortizationSchedule, self).__init__()
        except AttributeError as e:
            print(e)

    @abstractmethod
    def execute(self):
        return self.__init__()


class CalculatePaymentAmount(CalculateAmortizationSchedule):
    def execute(self):
        interest = (1 + (self.interestRate /
                         self.frequency_of_Payment))**-self.terms_of_Loans
        paymentAmount = self.loan_Amount / ((1-interest) / (self.interestRate /
                                                            self.frequency_of_Payment))
        return paymentAmount


if __name__ == "__main__":
    paymentAmount = CalculatePaymentAmount(5, 10, 12, 20000).execute()
    print(paymentAmount)
