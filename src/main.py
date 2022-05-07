"""
"Clean" your room with unpacking, *args, and **kwargs.
This activity will teach you a core concept (*args & **kwargs)
to get started with Django.

(Inspired by the status of my room during the final period)
"""

from actions import inspect, smell
from items import gifts_from_friend, stationery_items
from trash_can import TrashCan

# Part 1. Unpacking
# You've got a package from a friend that consists of 3 items.
# Try unboxing it with Python's unpacking.
# (Unpack & inspect the items.)
item1, item2, item3 = gifts_from_friend.values()
inspect(item1, item2, item3)

# The second item turned out to be a bouquet.
# You want to smell each flower.
# Can you take out the flowers from flowers through unpacking?
# (Unpack & smell each item.)
freesia, rose, anemone, lily_of_the_valley = item2

smell(freesia)
smell(rose)
smell(anemone)
smell(lily_of_the_valley)


# Part 2. Unpacking & *args
# Oh no! Your desk is a mess.
# Throw away all the trash in a can and empty the can.
items_on_desk = [
    {"pencil case": stationery_items},
    "empty water bottle",
    "eraser crumbs",
    "used tissue",
    "battery charger",
]

pencil_case, *trash, battery_charger = items_on_desk

trash_can = TrashCan()

trash_can.put(*trash)
trash_can.check()

trash_can.empty()
trash_can.check()


# Part 3. Unpacking & **kwargs (WIP)
