import computer.cpu as cpu

cmp = cpu.Computer()

cmp.load("inputs/day8.txt")

cmp.complete_on_loop()

cmp.run()

print(cmp.registers["acc"])