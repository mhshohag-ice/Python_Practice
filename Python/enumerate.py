def skip_elements(elements):
    my_list =[]
    for index, x in enumerate(elements):
        index = index + 1
        if index == 1 or index % 2 != 0:
            my_list.append(x)
    return my_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
