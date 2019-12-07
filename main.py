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


class CalculateAmortization(CalculateAmortizationSchedule):

    def installmentAmount(self):
        interest = (1 + (self.interestRate /
                         self.frequency_of_Payment))**-self.terms_of_Loans
        paymentAmount = self.loan_Amount / ((1-interest) / (self.interestRate /
                                                            self.frequency_of_Payment))
        return paymentAmount

    def execute(self):

        installment = self.installmentAmount()
        interest = self.interestRate / self.frequency_of_Payment
        balanceDue = self.loan_Amount

        table = pd.DataFrame(
            columns=["Installment Amount", "Interest Portion", "Principal Portion", "Balance Due"])

        installments = [0]
        interestPortion = [0]
        principalPortion = [0]
        balanceDue = [self.loan_Amount]

        installments.insert(1, installment)
        a = self.loan_Amount * interest
        interestPortion.insert(1, a)
        b = installment - a
        principalPortion.insert(1, b)
        c = balanceDue[0] - b
        balanceDue.insert(1, c)

        for i in range(2, self.terms_of_Loans+1):
            installments.insert(i, installment)
            a = balanceDue[i-1] * interest
            interestPortion.insert(i, a)
            b = installment - a
            principalPortion.insert(i, b)
            c = balanceDue[i-1] - b
            balanceDue.insert(i, c)

        table["Installment Amount"] = installments
        table["Interest Portion"] = interestPortion
        table["Principal Portion"] = principalPortion
        table["Balance Due"] = balanceDue

        return table.round(2)

    # return interestPortion


if __name__ == "__main__":
    calc = CalculateAmortization(5, 10, 12, 20000).execute()
