"""
Module: farming_diary
This script simulates a farming diary where different crops (corn and rice) are grown, watered,
and checked for ripeness.
"""

"""Farming diary module."""

from farm.corn import Corn


print("\n\n Day One: Corn")

corn = Corn()

corn.water()

print(f"The corn crop produced {corn.grains} grains")

if corn.ripe():
    print("The corn crop is ripe")
else:
    print("The corn crop is not ripe")
