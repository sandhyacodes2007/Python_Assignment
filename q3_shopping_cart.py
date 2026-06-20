
# ========================
# Part A - Spot the Bug
# =========================

def add_item_bug(item, cart=[]):
    cart.append(item)
    return cart

print("Part A - Bug Demonstration")
print(add_item_bug("apple"))
print(add_item_bug("banana"))
print(add_item_bug("milk", cart=["bread"]))
print(add_item_bug("eggs"))

"""
Output:

['apple']
['apple', 'banana']
['bread', 'milk']
['apple', 'banana', 'eggs']

Explanation:
The default list cart=[] is created only ONCE when the function
is defined, not every time it is called.

Therefore:
1. apple is added to the shared default list.
2. banana is added to the same list.
3. A new list ['bread'] is explicitly passed, so it is separate.
4. eggs is added to the original shared default list.

This is the famous mutable default argument bug.
"""


# =========================
# Part B - Correct Version
# =========================

def add_item(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\nPart B - Fixed Version")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", ["bread"]))
print(add_item("eggs"))

"""
Output:

['apple']
['banana']
['bread', 'milk']
['eggs']

Each call without a cart now gets a fresh empty list.
"""


# =========================
# Part C - Shopping Cart
# =========================

def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


def update_price(price_tuple, new_price):
    """
    Demonstrates tuple immutability.
    Attempting to modify a tuple element raises TypeError.
    """
    price_tuple[0] = new_price


def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = total * (cart["discount"] / 100)
    final_total = total - discount_amount

    return final_total


# =========================
# Demonstration
# =========================

customer1 = create_cart("Aarav", 10)
customer2 = create_cart("Riya", 5)

add_to_cart(customer1, "Laptop", 50000, 1)
add_to_cart(customer1, "Mouse", 800, 2)

add_to_cart(customer2, "Book", 500, 3)
add_to_cart(customer2, "Pen", 20, 5)

print("\nCustomer 1 Cart:")
print(customer1)

print("\nCustomer 2 Cart:")
print(customer2)

print("\nCustomer 1 Total:", calculate_total(customer1))
print("Customer 2 Total:", calculate_total(customer2))

# Proves carts are independent
add_to_cart(customer1, "Keyboard", 1500, 1)

print("\nAfter modifying Customer 1 Cart:")

print("Customer 1:")
print(customer1)

print("Customer 2 (unchanged):")
print(customer2)


# =========================
# Tuple Immutability Demo
# =========================

price_info = ("Laptop", 50000)

try:
    update_price(price_info, 60000)
except TypeError as e:
    print("\nTuple Modification Error:")
    print(e)


# =========================
# Discussion Points
# =========================

"""
1. Why is discount=0 safe but cart=[] dangerous?

discount=0 is safe because integers are immutable.
Python does not modify the integer object itself.

cart=[] is dangerous because lists are mutable.
The same list object is reused across function calls.


2. What is the difference between rebinding and mutating?

Rebinding:
    x = [1, 2]
    x = [3, 4]

The variable x now points to a completely new object.

Mutating:
    x = [1, 2]
    x.append(3)

The original object itself changes.


3. Which of these are mutable?

Mutable:
    list
    dict
    set

Immutable:
    tuple
    str
    int


4. When you pass a list into a function and modify it,
   do changes reflect outside? Why?

Yes.

Lists are mutable objects.

When a list is passed to a function, both the caller and
the function refer to the same underlying object.

Mutating that object (append, remove, update, etc.)
changes it everywhere that references it.
"""