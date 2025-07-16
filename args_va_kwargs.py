# Mavzu: *args va **kwargs
# bular bizda bir nehcta malumotlarni function ga uzatish imkonini beradi.
# *args - bu biz bergan ma'lumotlarni tuple () qilib qaytaradi
# **kwargs - bu bizda bir nechta ma'lumotlarni dict (lug'at) qilib uzatadi.

# 1 - usul
# def args_va_kwargs(*args):
#     return args
#
# print(args_va_kwargs("Ziyobek", "Ozodbek", "Karina", "Muhammadumar", "Sayodbek", "Ro'zmat"))
#
# # 2 - usul
# def args_va_kwargs(args, e,t,y,r):
#     return args,e,t,y,r
#
# args = 1,2,3,4,5
# print(args_va_kwargs(*args))
#
# # kwargs - bu 1 usul
# def args_va_kwargs(**kwargs):
#     return kwargs
#
# print(args_va_kwargs(name="Ziyobek", age=12))
#
# # 2 - usul
# def args_va_kwargs(name):
#     return name
#
# kwargs = {"name": "Ro'zmat"}
# print(args_va_kwargs(**kwargs))
#
# # def malumot(m,i,x,r,e):
# #     return m,i,x,r,e
# #
# # print(malumot(1,2,3,4,5))
#
# print(1,2,3)
# print(1,2,3)
# print(1,2,34)


# def ziyobek_muhammadumar(*args, **kwargs):
#     print(f"bu args {args}")
#     print(f"bu kwargs {kwargs}")
#
# print(ziyobek_muhammadumar(1,2,3,4,5, name="Ziyobek", age=12))