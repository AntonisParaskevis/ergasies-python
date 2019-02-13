import collections, string
filename=input("Δώστε το όνομα ενός αρχείου κειμένου, π.χ. example.txt\n")
file = open(filename, "r+") 
text = file.read()
counts = collections.Counter(text)
srtd = ''.join(sorted(set(text).intersection(string.ascii_lowercase), key=counts.get))
result = text.translate(str.maketrans(srtd, srtd[::-1]))
result = result.upper()
print(result)
file.close()
import time
time.sleep(30)

