# Dictionary (Lug'at)
# dict bizda har doim key=value bilan yoziladi.
# dict (dictionary) da har qanday ma'lumot turini saqlasak bo'ladi

# bu ichma ich kirgan ma'lumotni chiqarish
# print(lugat["lug'at"]["name"])
# bu lug'atdan ma'lumot olish
# print(lugat["name"])

# bu ma'lumot o'zgartirish
# lugat["name"] = "Ozodbek"
# print(lugat)

# dict methods
# items - bu bizda dictdan key ni ham valueni ham olib keladi
# for x, i in lugat.items():
#     print(x, i)

# bu lug'atga ma'lumot qo'shish
# lugat["Holati"] = "maktabi o'quvchisi"
# print(lugat)
#
# # get bizda value (qiymatni olish)
# m = lugat.get("age")
# print(m)

# bu lug'atdan ma'lumotni qirqib olish
# n = lugat.pop("number")
# print(n)s
# print(lugat)

# bu bizda lug'atni tozalaydi
# lugat.clear()
# print(lugat)

# lugat = {
#     "name": "Ziyobek",
#     "age": 12,
#     "number": 998934587755,
#     "list": [1,2,3,4,5,6],
#     "lug'at": {"name": "Shoxjahon"}
# }

# bu lug'atni nusxalaydi
# m = lugat.copy()
# print(m)

# # bu bizda faqat kalitlarni olib keladi
# print(lugat.keys())
#
# # bu bizda faqat qiymatlarni olib keladi
# print(lugat.values())

#

# Topshiriq
# inputdan 3 ta ma'lumot qabul qilib lug'atga dictga saqlash
# 1. ismi
# 2. yoshi
# 3. telefon raqami


talabalar = {
"ozodbek": "b",
"ziyobek": "y",
"shoxjahon": "r",
}

a = input("ism kiriting:")

for k,v in talabalar.items():
    if a== k:
        print(v)

    elif a !=k:
        print("buodam mavjud emas")
























