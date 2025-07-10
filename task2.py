list_1_to_10 = [ i for i in range(1,11) ]
print(f"Original list: {list_1_to_10}")

list_elem = list_1_to_10[0:5]
print(f"Extracked first five element: {list_elem}")

list_reverse = list(reversed(list_elem))
print(f"Reversed extracted element: {list_reverse}")