#first
stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()

print (stuff[0])
print(stuff.__getitem__(0))
print(list.__getitem__(stuff,0))
# print(dir(stuff))

#second-class; constructors and destructors
class PartyAnimal:
    x = 0
    y = 5
    name = ''

    def __init__(self,name):
        self.name = name
        print(self.name,"is constructed as","x =",self.x,"y =",self.y)

    def party(self):
        self.x = self.x + 1
        print(self.name, "so far has x as",self.x)

    def teaparty(self,y):
        self.y = self.y + y
        print(self.name, "has y =",self.y)

    def __del__(self):
        print(self.name, "has destructed x =",self.x,"y =",self.y)

# an = PartyAnimal()
# an.party()
# an.teaparty(10)
# print("an is ",an)
# an = 50 #The --del-- is called now and our variables are discarded
# print("now an is",an)
class executing(PartyAnimal):
    points = 0

    def easy(self):
        self.points = self.points + 6
        self.party()
        self.teaparty(1000)
        print(self.name,"points",self.points)


s = PartyAnimal('Sally')
s.party()
s.teaparty(10)
print("----------")
j = PartyAnimal('Jim')
j.party()
j.teaparty(20)
print("-----------")
s = executing('Sally')
j = executing('Jim')
s.easy()
j.easy()
print("-----------")
s = 20
j = 20


