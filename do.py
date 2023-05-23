import re

names = ["Telesphore", "Rib skee", "Drink water free", "Do it though"]
regex = "^\w+\s\w+$"
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)