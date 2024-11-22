import random
class student:
    def __init__(self,ชื่อนามสกุล,ชื่อเล่น,):
        self.name = ชื่อนามสกุล
        self.nickname = ชื่อเล่น
        self.score = random.randint(1,10)
        self.editscore = random.randint(1,10)
    def Scores(self):
        if self.score >=5:
            print(f"{self.name} {self.nickname} {self.score} : คุณสอบผ่าน")
        else :
            print(f"{self.name} {self.nickname} {self.score} : คุณสอบตก")
            print("--------------สอบตก-----------")
            if self.editscore >=5:
                print(f"{self.name} {self.nickname} {self.editscore} :ผ่าน")
            else:
                 print(f"{self.name} {self.nickname} {self.score} : ตก")
student1 =student("Pinthip Rungsri","pin",)
student2 =student("nanticha wongyong","ice",)
student3 =student("Saowalak Pankaew","Taengkwa",) 
student4 =student("Thanchanok Chaichana","Ked",) 
student5 =student("Chananporn Pimsena","Mint",)

student1.Scores()
student2.Scores()
student3.Scores()
student4.Scores()
student5.Scores()