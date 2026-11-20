# myList = [76, 92.3, 'hello', True, 4, 76]
# myList.append("apple")
# myList.append(76)
# myList.insert(3, "cat")
# myList.insert(0, 99)
# print(myList)
#
# print(myList.index('hello'))
#
#
# print(myList.count(76))
#
# myList.remove(76)
# print(myList)
#
# myList.pop(myList.index(True))
# print(myList)


# def sum_of_squares(number_list):
#     total = 0
#     for number in number_list:
#         total = total + number**2
#     return total
#
# my_list = [3, 4, 5 ]
# print(sum_of_squares(my_list))

#
# def sum_evens(xs):
#     sum = 0
#     for number in number_list:
#         if x % 2 == 0:
#             sum += number
#     return sum
#
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum_evens(my_list))


# def count_five_letter(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter
#
# my_list = {'apple', 'cat', 'lemon', 'phyton', 'tiger'}
# print(count_five_letter(my_list))

# def sum_until_even(number_list):
#     sum = 0
#     for number in number_list:
#         if number % 2 == 0:
#             break
#         sum += number
#     return sum
#
# my_list = [1, 3, 3, 7, 5, 6, 1, 9]
# print(sum_until_even(my_list))


# def count_until_sam(words):
#     count= 0
#     for word in words:
#         count = count + 1
#         if word == 'sam':
#             break
#     return count
#
# my_list = ["joe", "ali", "veli", "sam", "sami"]
#
# print(count_until_sam(my_list))

# def replace(s, old, new):
#     parts = s.split(old)
#     new_string = new.join(parts)
#     return new_string
#
# print(replace("Mississippi", "i", "I"))
# s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
# print(replace(s, "om", "am"))
# print(replace(s, "o", "a"))



# def max(xs):
#     largest = xs[0]
#     for x in xs:
#         if x > largest:
#             largest = x
#     return largest
# print(max([1,2,3,4,5]))
# print(max([-10,-25,-3,-1]))
# print(max([42]))