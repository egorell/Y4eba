class car:
    def __init__(self, year, color, type):
        self.year = year
        self.color = color
        self.type = type
    def start(self):
        print("Машина заведена")
    def stop(self):
        print("Машина заглушена")
    def set_year(self, year):
        self.year = year
    def set_color(self, color):
        self.color = color
    def set_type(self, type):
        self.type = type
car=Car('Зеленая', '2017', 'Toyota')
car.start()
car.stop()
car.set_year(2017)
car.set_type('Toyota')
car.set_color('Зеленая')

