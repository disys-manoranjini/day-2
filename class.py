class creditcard:
    creditlimit=100
    def __init__(self,a,b):
        self.basicpay=a
        self.expiry=b
    def recivecard(self):
        print (self.basicpay,self.expiry)


mano=creditcard(5,7)
#mano.salary()
mano.recivecard()
