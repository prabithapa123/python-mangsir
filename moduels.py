from datetime import date
from time import time
from camelcase import CamelCase


today = date.today()

print(today)


timestamp = time()
print(timestamp)


c = CamelCase()
print(c.hump("hello there world"))