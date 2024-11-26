b = 0 
while True:
    print('โปรแกรมบวกค่าเรื่อยๆ ถ้าต้องการออกจากโปรแกรมกรุณาพิมพ์ "หยุด"')
    try: 
        num = input('ใส่ค่า : ')   
        if num == "หยุด":
            print(f'ผลรวมทั้งหมด {b}')
            print('โปรแกรมสิ้นสุด')
            break  
   
        num = int(num) 
        if num == 0:
            raise ZeroDivisionError
                 
        elif num < 0:
            raise Exception

        b = b + num
        print(f'ผลรวมตอนนี้ {b}')
        print('--------------------------------------')

    except ValueError:
        print('ใส่เฉพาะตัวเลข')
    except ZeroDivisionError:
        print('ห้ามใส่ค่าเป็น 0')
    except :
        print('ห้ามใส่ค่าติดลบ')