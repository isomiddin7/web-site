# # A4 javobi
# # list1 = [3, 6, 9, 12, 15, 18, 21]
# # list2 = [4, 8, 12, 16, 20, 24, 28]
# # res = []

# # odd_elements = list1[1::2]
# # print("Toq index dagi sonlar")
# # print(odd_elements)

# # even_elements = list2[0::2]
# # print("Juft index dagi sonlar")
# # print(even_elements)

# # print("Umumiy natija")
# # res.extend(odd_elements)
# # res.extend(even_elements)
# # print(res)

# # A5 javobi
# # sample_list = [34, 54, 67, 89, 11, 43, 94]

# # print("Original list ", sample_list)
# # element = sample_list.pop(4)
# # print("List After removing element at index 4 ", sample_list)

# # sample_list.insert(2, element)
# # print("List after Adding element at index 2 ", sample_list)

# # sample_list.append(element)
# # print("List after Adding element at last ", sample_list)

# # A6 javobi

# # sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# # # print("Original list ", sample_list)
# # count_dict = dict()
# # for item in sample_list:
# #     if item in count_dict:
# #         count_dict[item] += 1
# #     else:
# #         count_dict[item] = 1

# # print(count_dict)


# # A7 javobi
# # sample_list = [87, 52, 44, 53, 54, 87, 52, 53]

# # print("Original list", sample_list)

# # sample_list = list(set(sample_list))
# # print("unique list", sample_list)

# # t = tuple(sample_list)
# # print("tuple ", t)

# # print("Minimum number is: ", min(t))
# # print("Maximum number is: ", max(t))


# # LOOPS
# # 1) For
# # 2) While
# num = int(input("Enter a number: "))
# check = False

# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             check = True
#             # break out of loop
#             break

#     # check if flag is True
#     if check:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")


# # word = 'Python for the kids'
# # for i in word:
# #     if i == "a" or i == "e" or i == "u" or i == "i" or i == "o":
# #         continue
# #     print(i, end="")
# # # Pythn fr th kds


# import random
# print("Maxfiy sonni topish o'yinini o'ynaysizmi ?")
# print("Oynash uchun 'Ha' yoki 'Yo'q' deb yozing")
# tanlov = input(">>>> ").strip()
# if tanlov == "Ha"or tanlov == "ha" :
#     secret_son = random.randint(0, 10)
#     urinishlar_soni = 3
#     print("Maxfiy sonni toping")
#     print("Maxfiy son 0 va 10 orailqda")
#     print(secret_son)
#     while urinishlar_soni > 0:
#         kiritilgan_son = int(input(">>>> "))
#         urinishlar_soni -= 1
#         if urinishlar_soni == 0:
#             print("Sizda urinishlar soni qolmadi qayta pul to'lang")
#         else:
#             if kiritilgan_son == secret_son:
#                 print("Tabriklaymiz siz maxfiy sonni topdingiz !!!")
#                 break
#             else:
#                 print(f"Siz maxfiy sonni topa olmadingiz :(")
#                 print(f"Sizda {urinishlar_soni} urinish  qoldi ")
#                 print("Qayta urinib ko'ring")
# elif tanlov == "Yo'q" or tanlov == "yo'q":
#     print("Keyingi safar ko'rishguncha :( ")
#     quit()
# else:
#     print("Oynash uchun 'Ha' yoki 'Yo'q' deb yozing")
#     print('Shulardan faqat biitasini tanglang')


a = int(input(":"))
d = a-1, a+1
print(d)