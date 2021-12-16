class grandfather:
    def __init__(self,a,b,c,d):
        print("mano is great")
        self.name = a
        self.age = b
        self.location = c
        self.status=d
    def home(self):
        pass

class father(grandfather):
    def __init__(self,d,e):
        print("she is unique")
        super().__init__("mano",45,"bangalore","married")
        self.number = d
        self.phone = e


class child(father):
    def __init__(self,r,t):
        print("she is marvelious")
        #super().__init__("mano",45,"bangalore","married")
        self.num = r
        self.ph = t

mano=child(10,3089709834)
mano.child(num)
