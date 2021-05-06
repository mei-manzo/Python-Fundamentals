# 1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
# def biggie_size(listx):
#     new_list = []
#     for x in range (len(listx)): #since we are using "in" and not "range", refers to actual item within list
#         if listx[x]>0: 
#             new_list.append("big")
#         elif listx[x]<0:
#             new_list.append(listx[x])
#     return new_list
# print(biggie_size([-1, 3, 5, -5]))

# 2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
# def count_positives(listx):
#     count = 0
#     for x in listx:
#         if x>0:
#             count += 1
#         else:
#             pass
#     listx[(len(listx)-1)] = count
#     return listx
# print(count_positives([1,6,-4,-2,-7,-2]))

# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
# def sum_total(listx):
#     sum = 0
#     for x in listx:
#         sum += x
#     return sum
# print(sum_total([6,3,-2]))

# 4. Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
# def average(listx):
#     sum = 0
#     for x in listx:
#         sum += x
#     avg = sum/(len(listx))
#     return avg
# print(average([1,2,3,4]))
        

# 5. Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
# def length(listx):
#     return len(listx)
# print(length([]))

# 6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
# def minimum(listx):
#     mini = 0
#     for x in listx:
#         if x<mini:
#             mini = x
#         elif len(listx)==0:
#             return False
#         else:
#             pass
#     return mini
# print(minimum([]))


# 7. #check on returning false# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
# def maximum(listx):
#     max = 0
#     for x in listx:
#         if x>max:
#             max = x
#         elif len(listx)==0:
#             return(False)
#         else:
#             pass
#     return max
# print(maximum([]))

# 8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
# def ult_analysis(list): 

# 9. Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse(listx):
    switchNum = len(listx)//2
    for x in range (len(listx)):
        holder_val = listx[x]
        listx[x] = listx[len(listx)-1]
        listx[len(listx)-1] = holder_val
    return listx
print(reverse([37,2,1,-9]))