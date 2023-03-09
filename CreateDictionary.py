'''
Noel Desmarais
CS 021D
A helper function that formats a string of characters into a list to be used in the final program
'''

_string = input("Enter list: ")
alpha = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
_list = []
for i in range(0,len(_string)):
    _list.append(_string[i])
print(_list)
