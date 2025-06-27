# raqamlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # bu eng katasini chiqarib beradi
# print(max(raqamlar))
# # eng kichkinasini chiqarib beradi bular harflar uchun ham ishlidi
# print(min("nfefagfg"))
# # bu jami qiymatni qaytaradi
# print(sum(raqamlar))
# # print("Ziyobek")

# i = 5
# while i == 5:
#     print(i)
#     break


lst = ["Sayodbek", "Ziyobek"]

if len(lst) > 2:
    print("4 tadan ko'p odam online")

elif len(lst) <= 2:
    print(f"{lst[0]} va {lst[-1]} shular online")

else:
    print('Hech kim online emas')