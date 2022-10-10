# Emojilang parser
from sys import argv

path = argv[0]

with open(path, "r") as file:
    lines = file.readlines()
    