class Computer:
    def __init__(self, cpu, memory, hdd):
        self.__cpu = cpu
        self._memory = memory
        self.hdd = hdd

    def print_comp(self):
        print('CPU {}GHz\nMemory: {}GB\nhdd: {}Gb'.format(
            self.__cpu / 1000,
            self._memory,
            self.hdd
        ))

comp = Computer(2300, 16, 2000)
comp.print_comp()

print(comp._Computer__cpu)
comp._Computer__cpu = 2400
print(comp._memory)
comp.print_comp()