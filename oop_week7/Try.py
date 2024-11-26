while True:
    try :
        print("โปรดแกรมหาพื้นที่ 3 เหลี่ยม")
        a = int(input('ใส่ค่าฐาน \n'))
        if a == 0:
            raise ZeroDivisionError
        elif a <0:
            raise Exception
        a = int(input('ใส่ค่าความสูง \n'))
        if a == 0:
            raise ZeroDivisionError
        elif a <0:
            raise Exception
        q =0.5 * a * a
        print(f'พื้นที่ของ 3 เหลี่ยม={q}')

        print("โปรมแกรมหาพื้นที่ 4 เหลี่ยม")
        a = int(input('ใส่ค่าความกว้าง \n'))
        if a == 0:
            raise ZeroDivisionError
        elif a <0:
            raise Exception
        a = int(input('ใส่ค่าความยาว\n'))
        if a == 0:
            raise ZeroDivisionError
        elif a <0:
            raise Exception
        s =  a * a
        print(f'พื้นที่ของ 4 เหลี่ยม={s}')
        print("โปรแกรมหาพื้นที่วงกลม")
        a = int(input('ใส่ค่ารัศมี\n'))
        if a ==0:
            raise ZeroDivisionError
        elif a<0:
            raise Exception
        o = 3.14 *a ** 2
        print(f'พื้นที่ของวงกลม={0}')
    except ValueError:
        print('ใส่เฉพาะตัวเลขเต็ม')
    except ZeroDivisionError:
        print('ห้ามใส่เงขศูนย์')
    except:
        print("ห้ามติดลบ")

