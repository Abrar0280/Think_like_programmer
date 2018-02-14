import re

def digits(x):
   return [
       int(g)
       if g.isdigit()
       else g
       for g in re.split(r'(\d+)$', x)
   ]

s1 = ['11', '2', 'A', 'B', 'B1', 'B11', 'B2', 'B21', 'C', 'C11', 'C2']

print(sorted(s1, key=digits))


# === Output === #

# ['2', '11', 'A', 'B', 'B1', 'B2', 'B11', 'B21', 'C', 'C2', 'C11']
