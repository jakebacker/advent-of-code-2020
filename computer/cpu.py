from typing import Union, List


class Computer:

    def op_acc(self, val):
        self.registers["acc"] += int(val)

    def op_nop(self, val):
        pass

    def op_jmp(self, val):
        self.ip += int(val) - 1

    ops = {"acc": op_acc, "nop": op_nop, "jmp": op_jmp}
    registers = {"acc": 0}
    ip = 0

    # [(instruction, value), (instruction, value)]
    instructions = []

    MARK_COMPLETED = False
    completed_instructions = []

    running = True

    def load(self, program: Union[str, List[str]]):
        data = ""

        if type(program) is str:
            with open(program, "r") as f:  # "../inputs/day8.txt"
                data = f.read().split("\n")
        else:
            data = program

        for d in data:
            s = d.split(" ")

            self.instructions.append((s[0], s[1]))

    def complete_on_loop(self):
        self.MARK_COMPLETED = True

    def step(self):
        if self.MARK_COMPLETED:
            self.completed_instructions.append(self.ip)

        pair = self.instructions[self.ip]
        ins = pair[0]
        val = pair[1]

        self.ops[ins](self=self, val=val)

        self.ip += 1

    def run(self):
        while self.running:
            if self.MARK_COMPLETED:
                if self.ip in self.completed_instructions:
                    self.running = False
                    break
            self.step()
