import random





def generate_code(length=8):
    data = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''.join(random.choice(data) for x in range(length))   # اختار قيمة عشوائية من كل قيم الداتا لكل اكس موجودة ضمن نطاق ال 8
    return code 