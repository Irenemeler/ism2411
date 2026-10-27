# Self-Assessment Answers
# 1. The first bug I identified was that total = sale replaced the
# previous total instead of adding each sale. The correct approach is
# total += sale. Print statements and tracing help me find bugs.
#
# 2. apply_discount(price, tier) takes a price and a discount tier.
# It returns the price after applying the correct discount.
#
# 3. AI Disclosure: I used ChatGPT to explain the exercises, help me
# understand debugging, and review my code. This helped me understand
# functions, loops, and variable scope. I still need to test the code
# myself to make sure I understand how it works.


# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price * (1 - discount)


print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


# --- Exercise 3 ---
discounted_price = apply_discount(200, "gold")
print(f"After gold discount: ${discounted_price:.2f}")

tax = calculate_tax(discounted_price, 0.07)
total = discounted_price + tax
print(f"After tax: ${total:.2f}")


def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


print(
    f'final_price(200, "gold", 0.07) = '
    f'${final_price(200, "gold", 0.07):.2f}'
)


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"),
          (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
# Fixed version of broken_sales.py.
# Bug 1: total = sale overwrote the total instead of adding each sale.
# Fix: use total += sale.
# Bug 2: the for loop was missing a colon.
# Fix: add a colon at the end of the for statement.
# Bug 3: the while loop used <= len(sales), causing an index error.
# Fix: use i < len(sales).

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---
x = 100  # Global variable

def double_it():
    x = 999  # Local variable, separate from global x
    return x * 2

print(x)           # Prints 100
print(double_it()) # Prints 1998
print(x)           # Still prints 100

# Scope means where a variable can be accessed.
# The x inside double_it() is local to the function, so it
# does not change the global x outside the function.
