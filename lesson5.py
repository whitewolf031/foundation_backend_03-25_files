# Har bir element bizda indekslangan bo'ladi va 0 dan
# lst = ["Shoxjahon", 39485, True, True, "ejhgf"]

# Bu ayni lst dagi bitda ma'lumotni chaqirvolish
# print(lst[1])

# Ma'lumotni shunday o'zgartirsak bo'ladi
# lst[2] = False
# print(lst)

# len uzunligini sanash
# print(len(lst))

# List ni if elif shartlar bilan ishlatsak boladi
# if lst == "Shoxjahon":
#     print(lst)

# Xar xil ma'lumot turlaridan listga o'tkasak bo'ladi
# m = "Ro'zmat"
# n = list(m)
# print(n)
#
# lst = ["Shoxjahon", 39485, True, True, "ejhgf"]
# m = lst.index(True)
# e = lst.index("ejhgf")
# print(m)
# print(e)

# Listga ma'lumot qo'shishni 3 xil usuli bor
# 1. append - har doim oxiridan qoshish
# 2. extend - 2 listni birlashtirish
# 3. insert - hoxlagan joyimizga qoshish indeks orqali

# Ochirish va qo'shish methodlarini o'zgaruvchiga olib yozish shart emas

#1. Listga ma'lumot qo'shish
# mevalar = ["olma", "nok"]
# mevalar.append("anor")
# print(mevalar)

#2. extend 2 ta listni birlashtirish
# sonlar = [1, 2]
# sonlar.extend([3, 4])
# print(sonlar)

#3. insert - hoxlagan joyimizga qoshish indeks orqali
# mevalar = ["olma", "banan"]
# mevalar.insert(2, "nok")
# mevalar.insert(1, "Shoxjahon")
# print(mevalar)  # ['olma', 'nok', 'banan']

# listni ichidagi ma'lumotni o'chirish
# mevalar = ["olma", "nok", "banan", 34785, True, False]
# print(mevalar)
# mevalar.remove("nok")  # nomi bilan o‘chiradi
# mevalar.remove(34785)
# mevalar.remove(True)
# print(mevalar)  # ['olma', 'banan']

# in bizda ichida borligini tekshiradi
# mevalar = ["olma", "Anor"]
# if "banan" in mevalar:
#     print(True)
#
# elif "olma" in mevalar:
#     print("Olma mavjud")
#
# else:
#     print(False)

# bu listni butunlay tozalab tashlaydi
# mevalar = ["olma", "banan"]
# mevalar.clear()
# print(mevalar)  # []

# count bir xil ma'lumotlarni topib sanab beradi
# mevalar = ["olma", "olma", "banan", "Anor", "Nok", "anor"]
# print(mevalar.count("olma"))  # 2
# print(mevalar.count("Anor"))  # 2

# sort bizda tartiblash uchun va text va raqamlar uchun ham ishlaydi
# sonlar = [3, 1, 4, 2]
# text = ["a", "d", "b", "f", "c"]
# print(text)
# print(sonlar)
# text.sort()
# print(text)
# sonlar.sort()
# print(sonlar)  # [1, 2, 3, 4]

# teskari qilib beradi ro'yxatni
# sonlar.reverse()
# print(sonlar)  # [4, 3, 2, 1]


# while True:
#     m = input("Ismingizni kiriting: ")
#     print(f"Salom {m}")

# n = "secret"
#
# while True:
#     m = input("Parolni kiriting: ")
#     if m == n:
#         print("Xush kelibsiz!")
#
#     else:
#         print("Noto'g'ri")

# while True:
#     m = int(input("Raqam kiriting: "))
#
#     if m >= 0:
#         print(f"Son kiritngiz {m}")
#
#     else:
#         print("Sonni qayta kiritng")

# i = 0
#
# while i <= 5:
#     print(i)
#     i += 1

# while True:
#     son = int(input("Raqam kiriting: "))
#     print("Siz kiritgan sonning kvadrati shunga teng", son ** 2)


# i = 0
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# while True:
#     m = input("So'z kiriting: ")
#     if m == "stop":
#         print("Dastur to'xtadi")
#         break


# while True:
#     m = int(input("10 dan kichkina son kiritng: "))
#     if m < 10:
#         print("Siz sonni kiritdingiz", m)
#         break
#     else:
#         print("Kiritgan soningiz 10 dan katta yoki teng")
