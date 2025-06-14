# #List bizda ro'yxat
# # 1. Olma
# # 2. Anor
# # 3. Banan
# # Har bir ma'lumot indexlangan bo'ladi
# # Ro'yxat bu o'zida vaqtinchalik ma'lumotlarni saqlab turadigan ma'lumot turi
# # mevalar = ["Olma 0", "Anor 1", "Banan 2", True, 38746, 45.2]
# # listdan bitda ma'lumotni index yordamida olvolish
# # print(mevalar[3])
# # print(mevalar[5])
# # print(mevalar)
# # print(type(mevalar))
#
# # o'zgarucvchisiz yozsak bo'ladi va print siz consolega chiqadi
# # input("Salom Dunyo")
#
# #-------------------------listda qo'shish methodlari-----------------------------
# # append - oxiridan listga ma'lumot qo'shish
# # mevalar = ["Olma", "Anor", "Banan", "Banan", True, 38746, 45.2]
# # mevalar.append("Shoxjahon uyquchi")
# # print(mevalar)
# #
# # # insert - bizda hoxlagan joyimizga ma'lumot qo'shish
# # mevalar.insert(5, 234.54)
# # print(mevalar)
# #
# # # extend - bizda 2 ta listni birlashtirib berardi
# # sabzavotlar = ["Pamidor", "Sabzi", "Kartoshka", "Redizka", "Piyoz"]
# # mevalar.extend(sabzavotlar)
# # sabzavotlar.extend(mevalar)
# # print(mevalar, sabzavotlar)
# # print(sabzavotlar)
# #
# # n = sabzavotlar.count("Banan")
# # print(n)
#
# # 1 - topshiriq
# # Mevalar degan ro'yxat eng kami 10 ta ma'lumot bo'sin
# # eng kami bitda bir xil ma'lumot bo'sin
# # ichiga oxiridan so'z qo'shish
# # Listni o'rtasiga bitda sabzavot
# # listdan ayni bitda ma'lumotni chiqarish
#
# # 2 - topshiriq
# # 2 ta listni birlashtirish
# # va ichidan bitda ma'lumotni indexni olib chiqish
# # keyin tartiblash
#
# # 3 - topshiriq
# # raqamli tartiblangan ro'yxat [1,2,3,4,5,6,7,8,9,10]
# # bu ro'yxatni ichidan 8 ni o'chirib tashlash
# # shuni teskari qilib o'girish
#
# # 4 - topshiriq
# # raqamli tartiblangan ro'yxat [1,2,3,4,5,6,7,8,9,10]
# # yana bitda list qo'shish kerak [11, 12, 13, 14, 15]
# # shuni teskari qilib o'girish
#
# # 5 - topshiriq
# # bizda bitda list bor shuni ichidan
# # eng kami bitda bir xil ma'lumot bo'sin
# # 8 dan yana bitda ma'lumot bo'lsa oshani chiqarsin bomasa bir xil malumot yoq desin
#
# # m = [1,2,3,4,5,6,7,8,9,10]
# # n = [11, 12, 13, 14, 15]
# # print(m[-1])
# # m.extend(n)
# # # print(m[::-1])
# # if m.count(8):
# #     print(f"Bir xil ma'lumot bor")
# # else:
# #     print('bir xil malumot mavjud emas')
#
# m = [1, 3, 5]
# if m[0] and m[-1]:
#     print(m[0], m[-1])
# # n= [ 2, 6, 8]
# # m.extend(n)
# # print(m)
# # v = [7, 8]
# # f = [10, 9, 1, 1, 2]
# # v.extend(f)
# # print(v)
# #
# # s = [4, 5, 1]
# # g = [3, 3, 3, 3, 3]
# # s.extend(g)
# # print(s)
#
