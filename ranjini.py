import indhu

class father(indhu.grandfather):
    def __init__(self,d,e):
        print("she is unique")
        super().__init__("mano",45,"bangalore","married")
        self.number = d
        self.phone = e

mano=father(20,30)
