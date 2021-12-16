class grandfather:
    def __init__(self,a,b,c):
        print("mano is great")
        self.name = a
        self.age = b
        self.location = c
     
    def home(self):
        pass

class father(grandfather):
    def __init__(self,d,e):
        print("she is unique")
        super().__init__("mano",45,"bangalore")
        self.number = d
        self.phone = e

mano=father(20,30)
