class fruit:
   def __init__(self):
       print("FRUITS")
class apple(fruit):
    def getdata(self):
        name="Apple"
        color="Red"
        flavor="sweet"
        print(f"{name} tastes {flavor}")
class orange(apple):
    def getdata1(self):
        name="Orange"
        color="orange"
        flavor="sour"
        print(f"{name} tastes {flavor}")
res=orange()
res.getdata()
res.getdata1()