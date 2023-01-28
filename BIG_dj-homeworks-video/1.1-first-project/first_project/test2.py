

total = int(input())

list_names = []

for x in range(total):
    list_names.append(input())

check = True


while check:
    count_index = 0
    if len(list_names) >= 2:
        print(list_names[count_index])
        print(list_names[len(list_names)-1:][0])
        list_names.pop(count_index)
        list_names.pop(len(list_names)-1)
    else:
        if len(list_names) == 0:
            check = False
        else:
            print(list_names[0])
            check = False
