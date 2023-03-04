class Tank:
    def __init__(self, name, national, comander):
        self._name = name
        self._national = national
        self._comander = comander

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def national(self):
        return self._national

    @national.setter
    def national(self, national):
        self._national = national

    @property
    def comander(self):
        return self._comander

    @comander.setter
    def comander(self, comander):
        self._comander = comander

name = input("name")
national = input("national")
comander = input("comander")
tank = Tank(name, national, comander)
print(tank.name)
print(tank.national)
print(tank.comander)
print("____________________________________________")
tank.name = input("name")
tank.national = input("national")
tank.comander = input("comander")
print(tank.name)
print(tank.national)
print(tank.comander)