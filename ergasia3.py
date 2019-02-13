x = input("Δώστε το όνομα κάποιου αρχείου Python π.χ. example.py\n")
x_new = x + "_no_comments.py"
with open( x, 'r') as code, open( x_new, 'w') as out:
    for line in code:
        if not line.startswith('#'):
            out.write(line + '\n')
import os
os.remove(x)
os.rename(x_new, x)
