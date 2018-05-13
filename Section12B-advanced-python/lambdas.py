def alter(values, check):
        # return list(filter(check, values))
    return [val for val in values if check(val)]


def remove_numbers(value):
    return alter(value, lambda x: x not in [str(n) for n in range(10)])


def skip_letter(value, letter):
    return alter(value, lambda x: x != letter)


print(skip_letter("hello", "e"))


my_list = [1, 2, 3, 4, 5, 'a', 'b', 'c']


print(remove_numbers("hel5lo"))


# def check_not_five(x):
# 	return x != 5


another_list = alter(my_list, lambda x: x != 5)
#another_list = alter(my_list, check_not_five)

print(another_list)
