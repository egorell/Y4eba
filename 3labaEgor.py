class Tank:
    def __init__(self, name, national, comander):
        self._name = name
        self._national = national
        self._comander = comander

    def get_name(self):
        return self._name

    def set_age(self, name):
        self._name = name

    def get_age(self):
        return self._national

    def set_name(self, national):
        self._national = national

    def get_name(self):
        return self._comander

    def set_name(self, comander):
        self._comander = comander

name = input("name")
national = input("national")
comander = input("comander")
tank = Tank(name, national, comander)
print(tank._name)
print(tank._national)
print(tank._comander)