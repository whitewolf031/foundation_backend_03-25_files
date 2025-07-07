import lesson20
from lesson20 import *

yuklangan_malumot = Ismlar

print(Ismlar)
print(raqamlar)
print(jami_qiymat("3", "5"))
























# # # pass - bu code ni uxlab tur degani
# # # def (funksiya) - bu karobga ichida biz yozgan code larimizni saqlaydi va code ni qayta qayta yozishdan qochish uchun ishlatiladi
# # # def funskiyo_nome(ism="Ozodbek"):
# # #     # ma'lumot berish ni 1 usuli
# # #     # ism = "ism"
# # #     # return oxirgi natijani qaytarish
# # #     return ism
# # #
# # # print(funskiyo_nome())
# #
# # # def tictets():
# # #     ism = input("Ismingiz")
# # #     age = int(input("Yoshingizni kiritng: "))
# # #     if age <= 5 and 60 < age:
# # #         return f"Siz uchun chipta tekin"
# # #
# # #     elif yosh > 5 and yosh < 18:
# # #         return "Siz uchun chipta 10$"
# # #
# # #     elif yosh > 18 and yosh < 60:
# # #         return "Siz uchun chipta 15$"
# # #
# # #
# # # print(tictets())
# #
# # def telephone_list():
# #     telephone_list = {}
# #     ism = input("Ismingizni kriting: ")
# #     number = int(input("Telefon raqam kiritng: "))
# #
# #     telephone_list[ism] = number
# #     search = input("Ism kiriting")
# #
# #     for key, value in telephone_list.items():
# #         if key == search:
# #             print(f"Uning {value} telephone raqami")
# #
# #         else:
# #             print(f"{search} bunday odam mavjud emas")
# #
# #
# # print(telephone_list())
#
# def get_vote_count(lugat):
#     m = list(lugat.values())
#     return m[0] - m[-1]
#
# print(get_vote_count({"upvotes": 13, "downvotes": 0}))
# print(get_vote_count({"upvotes": 2, "downvotes": 33}))
# print(get_vote_count({"upvotes": 132, "downvotes": 132}))
#

# def society_name(friends):
#     for x in friends:
#         m = str(x[0])
#         return m

	# for x in friends:
	#     lst.append(i)

# print(society_name(["Adam", "Sarah", "Malcolm"]))

# def asc_des_none(lst, text):
#     if text == "Asc":
#         return sorted(lst)
#
#     elif text == "Des":
#         list(reversed(lst))
#         return sorted(lst, reverse=True)
#
#     else:
#         return lst
#
# print(asc_des_none([4,3,2,1], "Asc"))
# print(asc_des_none([7,8,11,66], "Des"))
# print(asc_des_none([1,2,3,4], "None"))
# print(asc_des_none([5,6,7,8,9], "Des"))
# print(asc_des_none([55, 54, 53, 52, 51], "Asc"))
# print(asc_des_none([8,9,10], "None"))

