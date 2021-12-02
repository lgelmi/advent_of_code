import copy
import dataclasses
import logging
from pathlib import Path
from typing import List


@dataclasses.dataclass
class GameState:
    acc: int = 0
    row: int = 0


class GameInstruction:

    ROW_INCREMENT = 1

    def execute(self, state: GameState) -> GameState:
        raise NotImplementedError

    def __str__(self):
        return f"{self.__class__.__name__}"

    def __repr__(self):
        return self.__str__()


class NoOperation(GameInstruction):
    def execute(self, state: GameState) -> GameState:
        return copy.deepcopy(state)


class Accumulate(GameInstruction):
    def __init__(self, increment):
        self.increment = increment

    def __str__(self):
        return f"{super().__str__()}({self.increment})"

    def execute(self, state: GameState) -> GameState:
        return GameState(state.acc + self.increment, state.row)


class Jump(GameInstruction):

    ROW_INCREMENT = 0

    def __init__(self, increment):
        self.increment = increment

    def __str__(self):
        return f"{super().__str__()}({self.increment})"

    def execute(self, state: GameState) -> GameState:
        return GameState(state.acc, state.row + self.increment)


class InstructionBuilder:
    @classmethod
    def from_str(cls, string: str) -> GameInstruction:
        builders = {
            "acc": cls.acc_from_str,
            "jmp": cls.jmp_from_str,
            "nop": cls.nop_from_str,
        }
        instruction, content = string.split(maxsplit=1)
        # noinspection PyArgumentList
        return builders[instruction](content)

    @classmethod
    def acc_from_str(cls, content: str) -> Accumulate:
        return Accumulate(int(content))

    @classmethod
    def jmp_from_str(cls, content: str) -> Jump:
        return Jump(int(content))

    @classmethod
    def nop_from_str(cls, _: str) -> NoOperation:
        return NoOperation()


class GameEngine:
    def __init__(self, instructions: List[GameInstruction]):
        self.state = GameState()
        self.instructions = instructions
        self.history: List[GameState] = []
        self.instruction_history: List[GameInstruction] = []

    def run(self):
        while True:
            self.history.append(self.state)
            instruction = self.instructions[self.state.row]
            if instruction in self.instruction_history:
                raise RuntimeError(f"Infinite loop found at {self.state} when runnning {instruction}.")
            self.instruction_history.append(instruction)
            logging.debug(f"Running instruction {instruction} at row {self.state.row}.")
            self.execute(instruction)


    def execute(self, instruction: GameInstruction):
        self.state = instruction.execute(self.state)
        self.state.row += instruction.ROW_INCREMENT


def read_input() -> List[GameInstruction]:
    with open(Path(Path(__file__).parent, "input")) as f:
        return parse_values(f.read())


def parse_values(content: str) -> List[GameInstruction]:
    return list(map(InstructionBuilder.from_str, content.split("\n")))


def solve_1(values):
    print("--------------- 1 ---------------")
    try:
        GameEngine(values).run()
    except RuntimeError as e:
        print(e)


def solve_2(values):
    print("--------------- 2 ---------------")
    values[298] = NoOperation()
    engine = GameEngine(values)
    try:
        engine.run()
    except (RuntimeError, IndexError) as e:
        print(e)
        print(*zip(engine.history, engine.instruction_history))


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
