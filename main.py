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

    def createTable(self, a, b, c, d):
        table = pd.DataFrame(
            columns=["Installment Amount", "Interest Portion", "Principal Portion", "Balance Due"])

        table["Installment Amount"] = a
        table["Interest Portion"] = b
        table["Principal Portion"] = c
        table["Balance Due"] = d

        return table

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

        installments = [0]
        interestPortion = [0]
        principalPortion = [0]
        balanceDue = [self.loan_Amount]

        a = self.loan_Amount * interest
        for i in range(1, self.terms_of_Loans+1):
            installments.insert(i, installment)
            a = balanceDue[i-1] * interest
            interestPortion.insert(i, a)
            b = installment - a
            principalPortion.insert(i, b)
            c = balanceDue[i-1] - b
            balanceDue.insert(i, c)

        table = self.createTable(installments, interestPortion,
                                 principalPortion, balanceDue)

        return table.round(2)


class CalculateSinkingFund(CalculateAmortizationSchedule):

    def createTable(self, a, b, c, d, e):

        table = pd.DataFrame(
            columns=["Installment Amount", "Interest Payment", "Sinking Fund Deposit", "Sinking Fund Interest", "Sinking Fund Balance"])

        table["Installment Amount"] = a
        table["Interest Payment"] = b
        table["Sinking Fund Deposit"] = c
        table["Sinking Fund Interest"] = d
        table["Sinking Fund Balance"] = e

        return table

    def installmentAmount(self):
        interest = (1 + (self.interestRate /
                         self.frequency_of_Payment))**-self.terms_of_Loans
        paymentAmount = self.loan_Amount / ((1-interest) / (self.interestRate /
                                                            self.frequency_of_Payment))
        return paymentAmount

    def execute(self):
        installment = self.installmentAmount()
        interest = self.interestRate / self.frequency_of_Payment
        interestPayment = self.loan_Amount * interest
        sinkingFundDeposit = installment - interestPayment
        sinkingFundInterest = installment - \
            (interestPayment + sinkingFundDeposit)
        sinkingFundBalance = installment - interestPayment

        Installments = [installment] * self.terms_of_Loans
        InterestPayment = [interestPayment] * self.terms_of_Loans
        SinkingFundDeposit = [sinkingFundDeposit] * self.terms_of_Loans
        SinkingFundInterest = [sinkingFundInterest]
        SinkingFundBalance = [sinkingFundBalance]

        for i in range(0, self.terms_of_Loans-1):
            SinkingFundBalance.insert(
                i+1, (SinkingFundBalance[i] * interest) + SinkingFundDeposit[i] + SinkingFundBalance[i])

        for i in range(0, self.terms_of_Loans-1):
            SinkingFundInterest.insert(i+1, (SinkingFundBalance[i] * interest))

        table = self.createTable(Installments, InterestPayment, SinkingFundDeposit,
                                 SinkingFundInterest, SinkingFundBalance)

        return(table)


if __name__ == "__main__":
    # calc = CalculateAmortization(5.75, 24, 1, 8460)
    # print(calc.execute())
    c = CalculateSinkingFund(6, 6, 1, 5000)
    print(c.execute())
