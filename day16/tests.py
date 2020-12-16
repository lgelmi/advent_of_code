import unittest

from .day16 import *

simple_rules = [
    Rule("class", [(1, 3), (5, 7)]),
    Rule("row", [(6, 11), (33, 44)]),
    Rule("class", [(13, 40), (45, 50)]),
]

simple_nearby = [
    [7, 3, 47],
    [40, 4, 50],
    [55, 2, 20],
    [38, 6, 12],
]

valid_rules = [
    Rule("class", [(0, 1), (4, 19)]),
    Rule("row", [(0, 5), (8, 19)]),
    Rule("class", [(0, 13), (16, 19)]),
]

valid_nearby = [
    [3, 9, 18],
    [15, 1, 5],
    [5, 14, 9],
]


class TestDay16(unittest.TestCase):
    def test_obviously_invalid(self):
        self.assertEqual(
            [], get_ticket_obviously_invalid(simple_rules, simple_nearby[0])
        )
        self.assertEqual(
            [4], get_ticket_obviously_invalid(simple_rules, simple_nearby[1])
        )

    def test_all_obviously_invalid(self):
        self.assertEqual(
            [4, 55, 12], get_all_obviously_invalid(simple_rules, simple_nearby)
        )

    def test_valid_tickets(self):
        self.assertEqual([[7, 3, 47]], get_valid_tickets(simple_nearby, simple_rules))

    def test_rules_order(self):
        self.assertEqual(
            [valid_rules[1], valid_rules[0], valid_rules[2]],
            evaluate_rule_order(valid_rules, valid_nearby),
        )
