# pass - bu code ni uxlab tur degani
# def (funksiya) - bu karobga ichida biz yozgan code larimizni saqlaydi va code ni qayta qayta yozishdan qochish uchun ishlatiladi
# def funskiyo_nome(ism="Ozodbek"):
#     # ma'lumot berish ni 1 usuli
#     # ism = "ism"
#     # return oxirgi natijani qaytarish
#     return ism
#
# print(funskiyo_nome())

# def tictets():
#     ism = input("Ismingiz")
#     age = int(input("Yoshingizni kiritng: "))
#     if age <= 5 and 60 < age:
#         return f"Siz uchun chipta tekin"
#
#     elif yosh > 5 and yosh < 18:
#         return "Siz uchun chipta 10$"
#
#     elif yosh > 18 and yosh < 60:
#         return "Siz uchun chipta 15$"
#
#
# print(tictets())

def telephone_list():
    telephone_list = {}
    ism = input("Ismingizni kriting: ")
    number = int(input("Telefon raqam kiritng: "))

    telephone_list[ism] = number
    search = input("Ism kiriting")

    for key, value in telephone_list.items():
        if key == search:
            print(f"Uning {value} telephone raqami")

        else:
            print(f"{search} bunday odam mavjud emas")


print(telephone_list())