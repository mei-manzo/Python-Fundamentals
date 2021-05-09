#1.
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# 1.Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# def fun1(listx):
#     listx[1][0] = 15
#     return listx
# print(fun1(x))

# 2.Change the last_name of the first student from 'Jordan' to 'Bryant'
# def fun2(listx):
#     listx[0]['last_name'] = 'Bryant'
#     return listx
# print(fun2(students))

# 3.In the sports_directory, change 'Messi' to 'Andres'
# def fun3(listx):
#     listx['soccer'][0] = 'Andres'
#     return listx
# print(fun3(sports_directory))

# 4.Change the value 20 in z to 30
# def fun4(listx):
#     listx[0]['y'] = 30
#     return listx
# print(fun4(z))

#2.
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(listx):
    for x in range (len(listx)):
        new_dict = listx[x]
        for key in new_dict:
            print(key, '-', new_dict[key])

iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#4.

# def printInfo(dictx):
#     for x in dictx:
#         new_dict = dictx[x]
#         for key in new_dict:
#             return(key, '-', new_dict[key])

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

