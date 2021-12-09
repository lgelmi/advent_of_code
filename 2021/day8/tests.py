from .challenge import *

base_input = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]
base_entries = [parse_row(row) for row in base_input]
base_code = {
    0: set("cagedb"),
    1: set("ab"),
    2: set("gcdfa"),
    3: set("fbcad"),
    4: set("eafb"),
    5: set("cdfbe"),
    6: set("cdfgeb"),
    7: set("dab"),
    8: set("acedgfb"),
    9: set("cefabd"),
}
base_decoder = SevenDigitDecoder(base_code)


def test_can_count_naive():
    assert count_naive(base_entries) == 26


def test_can_decode():
    assert base_decoder.decode(["cdfeb", "fcadb", "cdfeb", "cdbaf"]) == 5353


def test_can_get_code():
    assert SevenDigitDecoder.code_from_random_entry(
        [
            "acedgfb",
            "cdfbe",
            "gcdfa",
            "fbcad",
            "dab",
            "cefabd",
            "cdfgeb",
            "eafb",
            "cagedb",
            "ab",
        ]
    ) == base_code
