# def iss_odd(n):
#     return n % 2 != 0
import string
from os import MFD_ALLOW_SEALING

#
# def is_leap_year(year):
#     if year % 400== 0:
#         return True
#     if year % 100 == 0:
#         return False
#     if year % 4 == 0:
#         return True
#
# print(is_leap_year(2024))
# print(is_leap_year(1900))
#
# def print_triangular_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         print(i, "t", total)
#         total += i
#
# print_triangular_numbers(5)


#
# def reverse(s):
#     result = ""
#     for ch in s:
#         result = ch + result
#     return result
# print(reverse("hello world"))
#
# def reverse_slice(s):
#     return s[::-1]
#
# print(reverse_slice("hello world"))
#
# def remove_all_occurrences(sub, s):
#     return s.replace(sub, "")
#
# print(remove_all_occurrences("l", "hello world"))
#
# def remove_all(substr, main_str):
#     return main_str.replace(substr, "")
#
# print(remove_all("an", "banana"))
# print(remove_all("iss", "Mississippi"))
# print(remove_all("cyc", "bicycle"))


#
# def substitute(message, key):
#     alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
#     result = ""
#     for char in message:
#         index = alphabet.find(char.lower())
#         if index == -1:
#             result = result + char
#         elif char.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "qtgjeopwmazxğülruvbfdhjklşisu"
# print(substitute("Hello World!", key))


# def remove_dups(s):
#     result = ""
#     for char in s:
#         if char not in result:
#             result = result + char
#     return result
#
# print(remove_dups("hello world"))
# print(remove_dups("mississippi"))








