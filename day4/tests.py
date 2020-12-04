import unittest

from .day4 import *


class TestDay4(unittest.TestCase):
    def test_byr(self):
        self.assertTrue(StrictPassportScanner.validate_byr("2002"))
        self.assertFalse(StrictPassportScanner.validate_byr("2003"))

    def test_hgt(self):
        self.assertTrue(StrictPassportScanner.validate_hgt("60in"))
        self.assertTrue(StrictPassportScanner.validate_hgt("190cm"))
        self.assertFalse(StrictPassportScanner.validate_hgt("190in"))
        self.assertFalse(StrictPassportScanner.validate_hgt("190"))

    def test_ecl(self):
        self.assertTrue(StrictPassportScanner.validate_ecl("brn"))
        self.assertFalse(StrictPassportScanner.validate_ecl("wat"))

    def test_pid(self):
        self.assertTrue(StrictPassportScanner.validate_pid("000000001"))
        self.assertFalse(StrictPassportScanner.validate_pid("0123456789"))

    def test_valid_passport(self):
        hacked_scanner = HackedStrictPassportScanner()
        passports = [
            """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f
    """,
            """eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm""",
            """hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022""",
            """iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719""",
        ]

        for passport in passports:
            self.assertTrue(hacked_scanner.validate_fields(parse_passport(passport)))

    def test_invalid_passport(self):
        hacked_scanner = HackedStrictPassportScanner()
        passports = [
            """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
""",
            """iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946""",
            """hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277""",
            """hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""",
        ]

        for passport in passports:
            self.assertFalse(hacked_scanner.validate_fields(parse_passport(passport)))
