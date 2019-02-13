import math 
def primeFactors(n):
                if n >= 1000000 or n < 2:
                        print("Μη έγκυρο νούμερο")
                else:
                        while n % 2 == 0:
                                print (2) 
                                n = n / 2
                        for i in range(3,int(math.sqrt(n))+1,2):
                                while n % i== 0: 
                                        print (i) 
                                        n = n / i
                        if n > 2:
                                print (n)
n = int(input("Πληκτρολογήστε κάποιον αριθμό\n"))
primeFactors(n) 
import time
time.sleep(15)
