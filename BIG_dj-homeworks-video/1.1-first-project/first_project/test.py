

total = int(input())

all_numbers = []
max_number = 0

for x in range(total):
    num = int(input())
    if num > max_number:
        max_number = num
    all_numbers.append(num)


result = []
current_index = 1

for item in all_numbers:
    result.append(item)
    sum_items = item
    for items in all_numbers[current_index:]:
        sum_items += items
        result.append(item+items)
        result.append(sum_items)
    current_index += 1

result.append(sum(all_numbers))
print(result)

count = 0

for item in range(20):
    if item in result:
        pass
    else:
        if item == 0:
            pass
        else:
            print(item)
            break


