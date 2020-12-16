import dataclasses
import functools
import itertools
import operator
from pathlib import Path
from typing import List, Tuple


@dataclasses.dataclass
class Rule:
    name: str
    limits: List[Tuple[int, int]]

    @classmethod
    def from_str(cls, body: str) -> "Rule":
        name, intervals = body.split(":")
        limits = [cls.interval_from_str(interval) for interval in intervals.split("or")]
        return Rule(name, limits)

    @staticmethod
    def interval_from_str(body: str) -> Tuple[int, int]:
        left, right = body.strip().split("-")
        return int(left), int(right)

    def validate(self, value: int) -> bool:
        return any(left <= value <= right for left, right in self.limits)


def read_input():
    with open(Path(Path(__file__).parent, "input")) as f:
        return parse_values(f.read())


def parse_values(content: str) -> Tuple[List[Rule], List[int], List[List[int]]]:
    rules_body, your_body, near_bodies = content.split("\n\n")
    rules = [Rule.from_str(rule_body) for rule_body in rules_body.split("\n")]
    your = parse_value_list(your_body.split("\n")[1])
    nears = [parse_value_list(near_body) for near_body in near_bodies.split("\n")[1:]]

    return rules, your, nears


def parse_value_list(body: str) -> List[int]:
    return list(map(int, body.split(",")))


def get_ticket_obviously_invalid(ticket, rules):
    return [
        value for value in ticket if not any(rule.validate(value) for rule in rules)
    ]


def get_all_obviously_invalid(rules: List[Rule], nearby: List[List[int]]) -> List[int]:
    return list(
        itertools.chain(
            *[get_ticket_obviously_invalid(ticket, rules) for ticket in nearby]
        )
    )


def get_valid_tickets(nearby: List[List[int]], rules: List[Rule]) -> List[List[int]]:
    return [ticket for ticket in nearby if is_ticket_valid(ticket, rules)]


def is_ticket_valid(ticket, rules):
    return not bool(get_ticket_obviously_invalid(ticket, rules))


def evaluate_rule_order(rules: List[Rule], tickets: List[List[int]]) -> List[Rule]:
    rules = rules.copy()
    ordered_rules: List[Rule] = [Rule("invalid", [])] * len(rules)
    rules_values = list(map(list, zip(*tickets)))
    values_indexes = list(range(len(rules_values)))
    while values_indexes:
        for index in values_indexes.copy():
            valid_rules = get_valid_rules(rules, rules_values[index])
            if len(valid_rules) == 1:
                ordered_rules[index] = rules.pop(rules.index(valid_rules[0]))
                values_indexes.remove(index)
    return ordered_rules


def get_valid_rules(rules, field_values):
    return [
        rule for rule in rules if all(rule.validate(value) for value in field_values)
    ]


def get_ticket_fields(rules, your, nearby):
    return {
        rule.name: your[index]
        for index, rule in enumerate(
            evaluate_rule_order(rules, get_valid_tickets(nearby, rules))
        )
    }


def solve_1(values):
    print("--------------- 1 ---------------")
    rules, _, nearby = values
    print(sum(get_all_obviously_invalid(rules, nearby)))


def solve_2(values):
    print("--------------- 2 ---------------")
    print(
        functools.reduce(
            operator.mul,
            [
                value
                for field, value in get_ticket_fields(*values).items()
                if field.startswith("departure")
            ],
            1,
        )
    )


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
