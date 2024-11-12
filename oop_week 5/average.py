nums = []
on = int(input("No. :"))
for i in range(on):
    num = int(input('ใส่ค่า :'))
    nums.append(num)
a=sum(num) / len(nums)
print(nums)
print(f'ค่าเฉลี่ย{a}')