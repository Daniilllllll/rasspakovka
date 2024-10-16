def print_params(a = 1, b = "Stroka", c = True):
    print(a, b, c)

print_params(11, "b")
print_params(22, "c", False)
print_params(33)
print_params()

print_params(b=25)
print("OK")
print_params(c = [1,2,3])
print("OK")

values_list = [777, "Ork", True]
values_dict = {'a': 34, 'b': 'Pain', 'c': False }
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [9.8, "Идущий к реке"]

print_params(*values_list_2)