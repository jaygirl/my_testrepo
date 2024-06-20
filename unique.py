my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
my_list_2 = my_list[:]
unique_list =[]

for i in range(len(my_list_2)):
    if my_list_2[0] in my_list_2[1:]:
        del my_list_2[0]
        print(my_list_2)
    else:
        unique_list.append(my_list_2[0])
        del my_list_2[0]
print("The list with unique elements only:")
#print(my_list)
print(unique_list)