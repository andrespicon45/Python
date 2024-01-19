pat_num= [
    '''###\n# #\n# #\n# #\n###''',
    '''# \n#\n#\n#\n#''',
    '''###\n# #\n # \n#  \n###''',
    '''###\n  #\n###\n #\n###''',
    '''# #\n# #\n###\n  #\n  #''',
    '''###\n#  \n###\n #\n###''',
    '''###\n#  \n###\n# #\n###''',
    '''###\n  #\n # \n#\n#''',
    '''###\n# #\n###\n# #\n###''',
    '''###\n# #\n###\n  #\n###'''
]

num=input('Ingrese un numero entero no negativo:')
for i in num:
    i_num=int(i)
    print(pat_num[i_num])
