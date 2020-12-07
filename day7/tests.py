import unittest

from .day7 import *


class TestDay7(unittest.TestCase):
    def test_bag_counter(self):
        self.assertEqual(
            Counter(
                {"mirrored teal": 5, "shiny cyan": 5, "dull purple": 2, "light red": 1}
            ),
            parse_bag_count(
                "5 mirrored teal bags, 5 shiny cyan bags, 2 dull purple bags, 1 light red bag."
            ),
        )

    def test_count_shiny_gold_combination(self):
        self.assertEqual(
            4,
            count_shiny_gold_combination(
                parse_values(
                    """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
                )
            ),
        )

    def test_count_shiny_gold_content(self):
        self.assertEqual(
            126,
            count_shiny_gold_content(
                parse_values(
                    """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
                )
            ),
        )
        self.assertEqual(
            32,
            count_shiny_gold_content(
                parse_values(
                    """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
                )
            ),
        )
