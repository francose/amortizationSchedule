## Calculate Amortization & Sinking Fund

**_method takes 4 parameters_**

1. Interest rate
2. Years
3. Frequency of the interest that hits in that period of time
4. Loan amount

### Calculating Amortization Table

```python
'''Create an instance of CalctulateAmortization class and pass the parameters as intergers '''
calculate = CalctulateAmortization(5, 10, 12, 20000)
'''TO run the calculations we need to call execute funtion '''
calculate.execute()

```

### Calculating Sinking Fund Table

```python
''' Create an instance of CalculateSinkingFund class and pass the parameters as integers'''
calculate = CalculateSinkingFund(6, 6, 1, 5000)
'''TO run the calculations we need to call execute funtion '''
calculate.execute()
```
