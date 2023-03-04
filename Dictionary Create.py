'''
Noel Desmarais
CS 021D
A program that creates a dictionary from a string of characters for Enigma code
'''

_string = input("Enter list: ")
alpha = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
_list = []
for i in range(0,len(_string)):
    _list.append(_string[i])
print(_list)
