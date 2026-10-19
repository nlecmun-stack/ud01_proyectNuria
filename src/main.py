"""
Temperature and currency converter.
Author : Nuria Lechuga
Date   : 2026-10-19
Version: 1.0
"""
# We ask the user for an amount of money in euros.
euros = float(input("Euros: "))

# We convert euros to USD.
print(f"USD: {euros*1.12:.2f}")