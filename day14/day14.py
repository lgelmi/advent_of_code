from pathlib import Path
from typing import List


def read_input():
    with open(Path(Path(__file__).parent, "input")) as f:
        return parse_values(f.read())


def parse_values(content: str) -> List[str]:
    return content.split("\n")


class BitMaskSystem:
    def __init__(self, mask: str = "X" * 36, bit_architecture: int = 36):
        self.bits = bit_architecture
        self.update_mask(mask)
        self.memory = {}

    # noinspection PyAttributeOutsideInit
    def update_mask(self, mask: str):
        self._or_mask = int(mask.replace("X", "0"), 2)
        self._and_mask = int(mask.replace("X", "1"), 2)

    def update_memory(self, address: int, value: int):
        self.memory[address] = self.masked_value(value)

    def masked_value(self, value: int):
        return (value & self._and_mask) | self._or_mask


def execute_program(content: List[str], v=1):
    system = BitMaskSystem() if v == 1 else DecoderV2System()
    commands = {"mask": execute_mask, "mem": execute_mem}
    for line in content:
        left, right = line.split(" = ")
        for command, executor in commands.items():
            if line.startswith(command):
                executor(system, left, right)
    return system


def execute_mask(system: BitMaskSystem, _: str, value: str):
    system.update_mask(value)


def execute_mem(system: BitMaskSystem, command: str, value: str):
    system.update_memory(int(command[4:-1]), int(value))


def solve_1(values):
    print("--------------- 1 ---------------")
    system = execute_program(values)
    print(sum(system.memory.values()))


class DecoderV2System:
    def __init__(self, mask: str = "0" * 36, bit_architecture: int = 36):
        self.bits = bit_architecture
        self.update_mask(mask)
        self.memory = {}

    # noinspection PyAttributeOutsideInit
    def update_mask(self, mask: str):
        self._floating_mask = int(mask.replace("1", "0").replace("X", "1"), 2)
        self._or_mask = int(mask.replace("X", "0"), 2)

    def update_memory(self, address: int, value: int):
        for addr in self.generate_addresses(address):
            self._update_memory(addr, value)

    def generate_addresses(self, address):
        yield from self._generate_addresses(
            (address | self._or_mask) & ~self._floating_mask,
            self._floating_mask,
            self.bits,
        )

    @staticmethod
    def _generate_addresses(address: int, mask: int, bits):
        bits -= 1
        if bits < 0:
            yield address
            return
        target_bit = 1 << bits
        if mask & target_bit:
            yield from DecoderV2System._generate_addresses(
                address & ~target_bit, mask, bits
            )
            yield from DecoderV2System._generate_addresses(
                address | target_bit, mask, bits
            )
        else:
            yield from DecoderV2System._generate_addresses(address, mask, bits)

    def _update_memory(self, address: int, value: int):
        self.memory[address] = value


def solve_2(values):
    print("--------------- 2 ---------------")
    system = execute_program(values, 2)
    print(sum(system.memory.values()))


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
