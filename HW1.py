s_tr = 'Привет'
i_nt = 5
f_loat = 2.5
b_ytes = b'bytes'
b_ytes_2 = bytes([50,100,76,72,41])
my_list =[True, 786, 3.14, 'text', 70.2]
my_tuple =(123, 5.14, '2+3', 60.4)
my_dict = {"number":23,2: True, "my_list":[1,2,3]}
fr_set = frozenset ("Alex")

print(s_tr,type(s_tr))
print(i_nt,type(i_nt))
print(f_loat,type(f_loat))
print(my_list,type(my_list))
print(my_tuple,type(my_tuple))
print(my_dict,type(my_dict))
print(fr_set,type(fr_set))
print(b_ytes,type(b_ytes))
print((chr(50)),type(b_ytes_2))

#str_1 = 'Hi'
#str_2 = ' Vadim'
#str_3 = str_1+str_2
#print(str_3)

a = '2'
b = 14
print(a+','+str(b))

a = '2'
b = 14
print(a+'+'+str(b))
