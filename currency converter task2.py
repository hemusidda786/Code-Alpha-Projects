from forex_python.converter import CurrencyRates
import pandas as pd
c = CurrencyRates()
amount = int(input("Enter the aomunt:"))
from_currency = input("Form Currency:").upper()
to_currency = input("To Currency:").upper()

print(from_currency,"To ",to_currency,amount)
result = c.convert(from_currency,to_currency,amount)
print(result)