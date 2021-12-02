from collections import Counter
import re
from pathlib import Path
from typing import List, Set, Dict


def read_input() -> Dict[str, Counter]:
    with open(Path(Path(__file__).parent, "input")) as f:
        return parse_values(f.read())


def parse_values(content: str) -> Dict[str, Counter]:
    return {
        match["key"]: parse_bag_count(match["bags"])
        for match in re.finditer(
            "(?P<key>\w+\s\w+) bags contain (?P<bags>.*)", content, flags=re.MULTILINE
        )
    }


def parse_bag_count(bags: str) -> Counter:
    if bags.startswith("no"):
        return Counter()

    return Counter(
        {
            match["key"]: int(match["amount"])
            for match in re.finditer("(?P<amount>\d) (?P<key>\w+\s\w+) bags?[,.]", bags)
        }
    )


def count_shiny_gold_combination(bags: Dict[str, Counter]):
    return sum(can_contain_gold(bag, bags) for bag in bags)


def can_contain_gold(bag: str, bags: Dict[str, Counter]):
    bag_content = bags[bag]
    if "shiny gold" in bag_content:
        return True
    return any(can_contain_gold(sub_bag, bags) for sub_bag in bag_content)


def count_shiny_gold_content(bags: Dict[str, Counter]):
    return count_content(bags["shiny gold"], bags)


def count_content(bag: Counter, bags: Dict[str, Counter]):
    return sum(
        count * (1 + count_content(bags[sub_bag], bags))
        for sub_bag, count in bag.items()
    )


def solve_1(values):
    print("--------------- 1 ---------------")
    print(count_shiny_gold_combination(values))


def solve_2(values):
    print("--------------- 2 ---------------")
    print(count_shiny_gold_content(values))


if __name__ == "__main__":
    values = read_input()
    print(values["shiny gold"])
    solve_1(values)
    solve_2(values)
