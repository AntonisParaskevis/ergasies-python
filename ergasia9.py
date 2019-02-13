def maxSequence(a):
        best_value = a[0]
        best_idx = (0,0)
        for start_element in range(0, len(a)+1):
            for stop_element in range(start_element+1, len(a)+1):
                sum_sublist = sum(a[start_element:stop_element])
                if sum_sublist > best_value:
                    best_value = sum_sublist
                    best_idx = (start_element, stop_element)
        print("Η υπολίστα [{}:{}] ειναι αυτή με το μεγαλύτερο άθροισμα,το οποίο ισούται με {}".format(best_idx[0], best_idx[1], best_value))
print("Πληκτρολογήστε μια λίστα αριθμών")
a = [int(x) for x in input().split()]
maxSequence(a)
import time
time.sleep(10)
