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

# below method we can obtain the amount as the first installment


class Calculate_InstallmentAmount(CalculateAmortizationSchedule):  # correct
    def execute(self):
        interest = (1 + (self.interestRate /
                         self.frequency_of_Payment))**-self.terms_of_Loans
        paymentAmount = self.loan_Amount / ((1-interest) / (self.interestRate /
                                                            self.frequency_of_Payment))
        return paymentAmount


class Calculate_InterestPaymentAmount(CalculateAmortizationSchedule):  # correct
    def execute(self):
        interest = self.interestRate / self.frequency_of_Payment
        initialAmount = self.loan_Amount * interest
        return initialAmount


class Calculate_PrincipalAmount(CalculateAmortizationSchedule):
    def execute(self, installmentAmount, interestPayment):
        pricipalAmount = interestPayment - installmentAmount
        return pricipalAmount


class Calculate_OutstandingBalance(CalculateAmortizationSchedule):
    def execute(self, pricipalAmount):
        outStandingBalance = self.loan_Amount - pricipalAmount
        return outStandingBalance


def calculateAmortizationSchedule(interestRate: int, terms_of_Loans: int, frequency_of_Payment: int, loan_Amount: int) -> int:
    installmentAmount = Calculate_InstallmentAmount(
        interestRate, terms_of_Loans, frequency_of_Payment, loan_Amount).execute()

    interestPayment = Calculate_InterestPaymentAmount(
        interestRate, terms_of_Loans, frequency_of_Payment, loan_Amount).execute()

    principalAmount = Calculate_PrincipalAmount(
        interestRate, terms_of_Loans, frequency_of_Payment, loan_Amount).execute(interestPayment, installmentAmount)

    outStandingBalance = Calculate_OutstandingBalance(
        interestRate, terms_of_Loans, frequency_of_Payment, loan_Amount).execute(principalAmount)

    print(installmentAmount, interestPayment,
          principalAmount, outStandingBalance)


if __name__ == "__main__":
    calc = calculateAmortizationSchedule(6, 6, 1, 5000)
    print(calc)
