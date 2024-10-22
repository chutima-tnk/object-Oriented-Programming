print("โปรแกรมคำนวณเกรด")
a = int(input("โปรดใส่คะแนน :"))
if a< 0 or a >100 :
    print('กรอกดีๆ')
elif a >= 80:
    print('เกรด4')
elif a >=70:
    print('เกรด3')
elif a >=60:
    print('เกรด2')
elif a >=50:
    print('เกรด1')
else :
    print('สอบตก')
    print('ต้องการสอบแก้หรือ ถ้าต้องการพิม 1 ไม่ต้องการพิม 2')
    c = int(input('เลือก : '))
    if c == 1 :
        d = 50-a
        print(f'ตุณขาดคะแนน{d}')
    elif c==2:
        print('ตกต่อไปเถอะะะ')
    else :
        print('1 หรือ2 อย่ากวนตีน')