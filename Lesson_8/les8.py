class Student:
    firstName = "Olga"
    lastName =  "Birilova"
    groupNumber = "Z76"
    age = 25
    
    def getFullName(self):
        print(f"{self.firstName} {self.lastName}")
        
    def getAge(self):
        print(f"Age {self.age}")

    def GroupNumber(self):
        print(f"Group number {self.groupNumber}")
     
    def setNameAge(self, firstName: str, lastName: str, age: int):
        self.firstName = firstName
        self.lastName =  lastName
        self.age = age
        print("Name and age has been changed.")

    def setGroupNumber(self, groupNumber: str):
        self.groupNumber = groupNumber
        print("Group number has been changed.")

Olga = Student()
Olga.getFullName()
Olga.getAge()
Olga.GroupNumber()

Bradley = Student()
Bradley.setNameAge("Bradley", "Pitt", 58)
Bradley.setGroupNumber("K62")
Bradley.getFullName()
Bradley.getAge()
Bradley.GroupNumber()

Johnny = Student()
Johnny.setNameAge("Johnny", "Depp", 59)
Johnny.setGroupNumber("F71")
Johnny.getFullName()
Johnny.getAge()
Johnny.GroupNumber()

Tom = Student()
Tom.setNameAge("Tom", "Cruise", 60)
Tom.setGroupNumber("Q19")
Tom.getFullName()
Tom.getAge()
Tom.GroupNumber()

Nicolas = Student()
Nicolas.setNameAge("Nicolas", "Coppola", 58)
Nicolas.setGroupNumber("S14")
Nicolas.getFullName()
Nicolas.getAge()
Nicolas.GroupNumber()

John = Student()
John.setNameAge("John", "Nicholson", 85)
John.setGroupNumber("A52")
John.getFullName()
John.getAge()
John.GroupNumber()