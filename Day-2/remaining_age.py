# brief intro
print("Hello user we assume that you would live up to 100 years of age.")
print("NB: this is only a presumption it it is not in anyway real")

# get user age
age = int(input("Hello user kindly tell us how old you are in years: "))
years_remaining = 100 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
month_remaining = years_remaining * 12
print(f"You have {years_remaining} more years to live.")
print(f"you have {days_remaining} days to live.")
print(f"you have {weeks_remaining} weeks to live.")
print(f"you have {month_remaining} months to live.")