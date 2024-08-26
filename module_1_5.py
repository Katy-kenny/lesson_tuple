immutable_var = 1,2,'a','b'
print('Immutable tuple:', immutable_var)
#immutable_var[0] = 3 кортеж (tuple) относится к неизменяемым типам данных,
#                     он используется для создания списков с разными типами данных,
#                     который необходимо оставить неизменнным


mutable_list = [2,'a','b']

mutable_list[2] = 'c'
mutable_list.append(1)
mutable_list.extend(['Modified', '3'])
print('Mutable list: ', mutable_list)
