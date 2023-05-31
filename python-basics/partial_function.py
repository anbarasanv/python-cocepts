from functools import partial

TAX_RATE = 10

def final_price(price, tax_rate):
    return (price+(price*(tax_rate/100)))

# The TAX_RATE is frozen for below execution, if it get modified
# In the future the price will always depend on the initial tax rate.
price = partial(final_price, tax_rate=TAX_RATE)

print(price(250))
