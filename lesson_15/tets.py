class WaterBird:
    def __init__(self, name):
        self.name = name
        print('Bird is {}'.format(self.name))

    def where_is_live(self):
        print('on the Earth')

    def swim(self):
        print('Can swim fast')

    def voice(self):
        pass

class Penguin(WaterBird):
    def __init__(self, name):
        super().__init__(name)
        print('Penguin is ready')

    def where_is_live(self):
        print('North pole')

    def run(self):
        print('Run fast')

    def voice(self):
        print('pi-pi-pi')


class Duck(WaterBird):
    def __init__(self, name):
        super().__init__(name)
        print('Duck is ready')

    def where_is_live(self):
        print('Anywhere')

    def fly(self):
        print('Fly very high')

    def voice(self):
        print('kra-kra-kra')


peggy = Penguin('Ping')
peggy.where_is_live()
peggy.run()
peggy.swim()
peggy.voice()

duck = Duck('Donald')
duck.fly()
