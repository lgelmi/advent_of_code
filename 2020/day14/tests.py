import unittest

from .day14 import *


class TestDay14(unittest.TestCase):
    def test_mask(self):
        self.assertEqual(
            73, BitMaskSystem("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X").masked_value(11)
        )

    def test_address_generation(self):
        self.assertEqual(
            [26, 27, 58, 59], list(DecoderV2System("X1001X").generate_addresses(42))
        )
        DecoderV2System("X0XX").update_memory(26, 1)
        self.assertEqual(
            [16, 17, 18, 19, 24, 25, 26, 27],
            list(DecoderV2System("X0XX").generate_addresses(26)),
        )
