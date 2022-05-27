"""
"Clean" your (digital) room with unpacking, *args, and **kwargs in Python.

(Inspired by the status of my room during the final exam period)
"""

from actions import inspect, smell
from items import gifts_from_friend
from cleaning_desk import TrashCan
from washing_clothes import WashingMachine

# Part 1. Unpacking
# You've got a package from a friend that consists of 3 items.
# Try unboxing and inspecting it.

# How to use `inspect()`: inspect(arg1, arg2, arg3)

# YOUR CODE GOES HERE ---
item1, item2, item3 = gifts_from_friend
inspect(item1, item2, item3)
# -----------------------

# The second item turned out to be a bouquet.
# You want to check what flowers there are and what each of them smells like.
# Can you take out and smell each flower from the bouquet?

# How to use `smell()`: smell(arg1)

# YOUR CODE GOES HERE ---
freesia, rose, anemone, lily_of_the_valley = item2

smell(freesia)
smell(rose)
smell(anemone)
smell(lily_of_the_valley)
# -----------------------


# Part 2. Unpacking & *args
# Oh no! Your desk is a mess.
# Throw away all the trash in a can and empty the can.
# Be careful, though. You don't want to throw away the pencil case and the battery charger!

# TrashCan has 3 methods: `check_status()`, `put()`, and `empty()`.
# `trash_can.check_status()`: shows the current status of the trash can
# `trash_can.put(*args)`: puts the arguments into the trash can
# `trash_can.empty()`: empties the trash can

items_on_desk = [
    "pencil case",
    "empty water bottle",
    "eraser crumbs",
    "used tissue",
    "battery charger",
]

trash_can = TrashCan()

# YOUR CODE GOES HERE ---
_, *trash, _ = items_on_desk

trash_can.check_status()

trash_can.put(*trash)
trash_can.check_status()

trash_can.empty()
trash_can.check_status()
# -----------------------


# Part 3. Unpacking & **kwargs
# Now, you need to do laundry as there's a pile of clothes that you haven't washed for 2 weeks.
# Use two asterisks (**) to put clothes with the detergent into the washing machine.

# WashingMachine has 3 methods: `check_status()`, `put()`, and `start()`.
# `washing_machine.check_status()`: shows the current status of the washing machine
# `washing_machine.put(arg1, **arg2)`: puts arg1 (detergent) with args2
# `washing_machine.start()`: starts the washing machine and washes the clothes

clothes = {
    "normal": {
        "t-shirt",
        "socks",
        "underwear",
    },
    "perm press": {
        "blouse",
        "slacks",
    },
    "delicate": {"cashmere sweater", "silk shirt"},
}

detergent = "tide"
washing_machine = WashingMachine()

# YOUR CODE GOES HERE ---
washing_machine.check_status()

washing_machine.put(detergent, clothes=clothes)
washing_machine.check_status()

washing_machine.start()
washing_machine.check_status()
# -----------------------
