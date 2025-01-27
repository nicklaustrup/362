# Author: Nicholas Laustrup
# Onid: laustrun
# Date: 1/19/2025
# Assignment: Homework 1

import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    def test1(self):
        """
        !!!!BUG5!!!!
        Prefix: invalid
        Length: valid
        Checksum: valid
        returns False.
        Picked using Category Partition Testing.
        """
        string = '0503273146153783'  # prefix starts with 0
        self.assertFalse(credit_card_validator(string))

    def test2(self):
        """
        Prefix: valid
        Length: valid
        Checksum: invalid
        Returns False.
        Picked using Category Partition Testing.
        """
        string = '4716428794137777'  # Incorrect checksum
        self.assertFalse(credit_card_validator(string))

    def test3(self):
        """
        !!!!BUG1!!!!
        Prefix: invalid
        Length: invalid
        Checksum: invalid
        Returns False.
        Picked using Boundary Testing.
        """
        string = ''
        self.assertFalse(credit_card_validator(string))

    def test4(self):
        """
        Verifies that a Visa with incorrect length returns False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Boundary Partition Testing.
        """
        string = '471642879413770'  # Visa 15 digits
        self.assertFalse(credit_card_validator(string))

    def test5(self):
        """
        Verifies that a Visa with incorrect length returns False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Boundary Partition Testing.
        """
        string = '47164287941377216'  # Visa 17 digits
        self.assertFalse(credit_card_validator(string))

    def test6(self):
        """
        !!!!BUG2!!!!
        Verifies that an Amex with incorrect length returns False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Boundary Partition Testing.
        """
        string = '34947264751001'  # Amex 14 digits
        self.assertFalse(credit_card_validator(string))

    def test7(self):
        """
        !!!!BUG2!!!!
        Prefix: valid
        Length: invalid
        Checksum: valid
        Returns False.
        Picked using Boundary Partition Testing.
        """
        string = '34947264751200095'  # Amex 17 digits
        self.assertFalse(credit_card_validator(string))

    def test8(self):
        """
        !!!!BUG10!!!!
        A valid amex card that should return true.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '349472647512004'  # Amex 15 digits
        self.assertTrue(credit_card_validator(string))

    def test9(self):
        """
        !!!!BUG4!!!!
        Verifies that a Amex with incorrect length
            and incorrect checksum returns False.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Boundary Partition Testing.
        """
        string = '37947264751200099'  # Amex 17 digits
        self.assertFalse(credit_card_validator(string))

    def test10(self):
        """
        !!!!BUG2!!!!
        Verifies that a Amex with incorrect length returns False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Boundary Partition Testing.
        """
        string = '3794726475120006'  # Amex 16 digits
        self.assertFalse(credit_card_validator(string))

    def test11(self):
        """
        !!!!BUG2!!!!
        Verifies that a Amex with incorrect length returns False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Boundary Partition Testing.
        """
        string = '37947264751206'  # Amex 14 digits
        self.assertFalse(credit_card_validator(string))

    def test12(self):
        """
        !!!!BUG7!!!!
        Verifies that a Mastercard with incorrect checksum returns False.
        Prefix: valid
        Length: valid
        Checksum: invalid
        Picked using Category Partition Testing.
        """
        string = '5129547832910347'
        self.assertFalse(credit_card_validator(string))

    def test13(self):
        """
        Verifies that a Mastercard with incorrect length returns False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Category Partition Testing.
        """
        string = '512954783291031'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test14(self):
        """
        !!!!BUG8!!!!
        Verifies that a Mastercard with incorrect length returns False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Category Partition Testing.
        """
        string = '51295478329123033'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test15(self):
        """
        Verifies that a Visa with incorrect length returns False.
        Picked using Error Guessing.
        """
        string = '42'  # Visa 2 digits
        self.assertFalse(credit_card_validator(string))

    def test16(self):
        """
        !!!!BUG2!!!!
        Verifies that a Amex with incorrect length returns False.
        Picked using Error Guessing.
        """
        string = '349'  # Amex 2 digits
        self.assertFalse(credit_card_validator(string))

    def test17(self):
        """
        !!!!BUG2!!!!
        Verifies that a Amex with incorrect length returns False.
        Picked using Error Guessing.
        """
        string = '372'  # Amex 2 digits
        self.assertFalse(credit_card_validator(string))

    def test18(self):
        """
        Verifies that a Mastercard with incorrect length returns False.
        Picked using Error Guessing.
        """
        string = '513'  # Mastercard 3 digits
        self.assertFalse(credit_card_validator(string))

    def test19(self):
        """
        Verifies that a Mastercard with incorrect length returns False.
        Picked using Error Guessing.
        """
        string = '554'  # Mastercard 3 digits
        self.assertFalse(credit_card_validator(string))

    def test20(self):
        """
        Verifies that a Mastercard with incorrect length returns False.
        Picked using Error Guessing.
        """
        string = '22210'  # Mastercard 5 digits
        self.assertFalse(credit_card_validator(string))

    def test21(self):
        """
        Verifies that a Mastercard with incorrect length returns False.
        Picked using Error Guessing.
        """
        string = '27201'  # Mastercard 5 digits
        self.assertFalse(credit_card_validator(string))

    def test22(self):
        """
        !!!!BUG5!!!!
        Verifies that a Amex with incorrect prefix returns False.
        Picked using Error Guessing.
        """
        string = '3693847561924564'  # Mastercard 5 digits
        self.assertFalse(credit_card_validator(string))

    def test23(self):
        """
        Verifies that an invalid prefix with incorrect length returns False.
        Picked using Category Partition Testing.
        """
        string = '06938475619245622'  # invald prefix
        self.assertFalse(credit_card_validator(string))

    def test24(self):
        """
        !!!!BUG3!!!!
        Mastercard with invalid length and
            invalid checksum returns False.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Category Partition Testing.
        """
        string = '512954783291235'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test25(self):
        """
        Verifies that an invalid length returns False.
        Picked using Boundary Partition Testing.
        """
        string = '272047583237450'
        self.assertFalse(credit_card_validator(string))

    def test26(self):
        """
        !!!!BUG8!!!!
        Verifies that an invalid length returns False.
        Picked using Boundary Partition Testing.
        """
        string = '27204758323745026'
        self.assertFalse(credit_card_validator(string))

    def test27(self):
        """
        !!!!BUG5!!!!
        Verifies that an invalid prefix returns false.
        Picked using Boundary Partition Testing.
        """
        string = '2721475832374555'
        self.assertFalse(credit_card_validator(string))

    def test28(self):
        """
        Verifies that an invalid length returns False.
        Picked using Boundary Partition Testing.
        """
        string = '27204758323745025'
        self.assertFalse(credit_card_validator(string))

    def test29(self):
        """
        Verifies that a valid Mastercard returns true.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Error Guessing.
        """
        string = '2221458376543293'
        self.assertTrue(credit_card_validator(string))

    def test30(self):
        """
        Mastercard with incorrect checksum returns False.
        Picked using Error Guessing.
        """
        string = '379472647512005'
        self.assertFalse(credit_card_validator(string))

    def test31(self):
        """
        !!!!BUG6!!!!
        Valid Visa that should return true.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Error Guessing.
        """
        string = '4947264751200007'
        self.assertTrue(credit_card_validator(string))

    def test32(self):
        """
        !!!!BUG2!!!!
        Amex prefix with 16 length and correct checksum.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Error Guessing.
        """
        string = '3794726475120055'
        self.assertFalse(credit_card_validator(string))

    def test33(self):
        """
        !!!!BUG10!!!!
        Valid Amex that should return true.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Error Guessing.
        """
        string = '379472647512056'
        self.assertTrue(credit_card_validator(string))

    def test34(self):
        """
        Valid Mastercard that should return true.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Error Guessing.
        """
        string = '5534856920367843'
        self.assertTrue(credit_card_validator(string))

    def test35(self):
        """
        Valid Mastercard that should return true.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Error Guessing.
        """
        string = '2221856920367848'
        self.assertTrue(credit_card_validator(string))

    def test36(self):
        """
        Valid Mastercard that should return true.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Error Guessing.
        """
        string = '2720856920367844'
        self.assertTrue(credit_card_validator(string))

    def test37(self):
        """
        Testing only the prefix.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Returns False.
        Picked using Condition Partition Testing.
        """
        string = '4'
        self.assertFalse(credit_card_validator(string))

    def test38(self):
        """
        Testing only the prefix.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Returns False.
        Picked using Condition Partition Testing.
        """
        string = '51'
        self.assertFalse(credit_card_validator(string))

    def test39(self):
        """
        Testing only the prefix.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Returns False.
        Picked using Condition Partition Testing.
        """
        string = '55'
        self.assertFalse(credit_card_validator(string))

    def test40(self):
        """
        Testing only the prefix.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Returns False.
        Picked using Condition Partition Testing.
        """
        string = '34'
        self.assertFalse(credit_card_validator(string))

    def test41(self):
        """
        Testing only the prefix.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Returns False.
        Picked using Condition Partition Testing.
        """
        string = '37'
        self.assertFalse(credit_card_validator(string))

    def test42(self):
        """
        Testing only the prefix.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Returns False.
        Picked using Condition Partition Testing.
        """
        string = '2221'
        self.assertFalse(credit_card_validator(string))

    def test43(self):
        """
        Testing only the prefix.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Returns False.
        Picked using Condition Partition Testing.
        """
        string = '2720'
        self.assertFalse(credit_card_validator(string))

    def test44(self):
        """
        Prefix 38 but correct length and correct checksum.
        Prefix: invalid
        Length: valid
        Checksum: valid
        Picked using Boundary Testing.
        """
        string = '389472647512377'
        self.assertFalse(credit_card_validator(string))

    def test45(self):
        """
        Visa with correct length and prefix but wrong checksum.
        Prefix: valid
        Length: valid
        Checksum: invalid
        Picked using Partition Condition Guessing.
        """
        string = '4947264751200006'
        self.assertFalse(credit_card_validator(string))

    def test46(self):
        """
        Amex prefix with 16 length and incorrect checksum.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Guessing.
        """
        string = '3794726475120056'
        self.assertFalse(credit_card_validator(string))

    def test47(self):
        """
        Amex with incorrect check bit should return false.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Error Guessing.
        """
        string = '3794726475128'
        self.assertFalse(credit_card_validator(string))

    def test48(self):
        """
        Valid Mastercard with invalid check bit that should return False.
        Prefix: valid
        Length: valid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '5534856920367842'
        self.assertFalse(credit_card_validator(string))

    def test49(self):
        """
        Valid Mastercard with invalid check bit that should return False.
        Prefix: valid
        Length: valid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '2221856920367842'
        self.assertFalse(credit_card_validator(string))

    def test50(self):
        """
        Valid Mastercard with invalid check bit that should return False.
        Prefix: valid
        Length: valid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '2720856920367844'
        self.assertTrue(credit_card_validator(string))

    def test51(self):
        """
        Mastercard with invalid prefix that should return False.
        Prefix: invalid
        Length: valid
        Checksum: valid
        Picked using Boundary Testing.
        """
        string = '5620856920367848'
        self.assertFalse(credit_card_validator(string))

    def test52(self):
        """
        Mastercard with invalid prefix and invalid checksum
            that returns False.
        Prefix: invalid
        Length: valid
        Checksum: invalid
        Picked using Boundary Testing.
        """
        string = '5620856920367847'
        self.assertFalse(credit_card_validator(string))

    def test53(self):
        """
        Mastercard with invalid prefix and invalid length
            that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: valid
        Picked using Boundary Testing.
        """
        string = '56208569203678475'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test54(self):
        """
        Mastercard with invalid prefix, invalid checksum, and invalid
            length that should return False.
        Prefix: invalid
        Length: valid
        Checksum: invalid
        Picked using Boundary Testing.
        """
        string = '562085692036472'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test55(self):
        """
        Valid Mastercard that should return True.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '5220856920364724'
        self.assertTrue(credit_card_validator(string))

    def test56(self):
        """
        Valid Mastercard that should return True.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '5320856920364723'
        self.assertTrue(credit_card_validator(string))

    def test57(self):
        """
        Valid Mastercard that should return True.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '5320856920364723'
        self.assertTrue(credit_card_validator(string))

    def test58(self):
        """
        Valid Mastercard that should return True.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '5420856920364722'
        self.assertTrue(credit_card_validator(string))

    def test59(self):
        """
        Mastercard with invalid checksum that should return false.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '5220856920364723'
        self.assertFalse(credit_card_validator(string))

    def test60(self):
        """
        Mastercard with invalid checksum that should return false.
        Prefix: valid
        Length: valid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '5320856920364722'
        self.assertFalse(credit_card_validator(string))

    def test61(self):
        """
        Mastercard with invalid checksum that should return False.
        Prefix: valid
        Length: valid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '5420856920364721'
        self.assertFalse(credit_card_validator(string))

    def test62(self):
        """
        Mastercard with invalid length that should return False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '522085692036478'
        self.assertFalse(credit_card_validator(string))

    def test63(self):
        """
        Mastercard with invalid length and invalid checksum
            that should return False.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '522085692036477'
        self.assertFalse(credit_card_validator(string))

    def test64(self):
        """
        Mastercard with invalid checksum that should return false.
        Prefix: valid
        Length: valid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '5320856920364721'
        self.assertFalse(credit_card_validator(string))

    def test65(self):
        """
        Mastercard with invalid length and invalid checksum
            that should return false.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '532085692036476'
        self.assertFalse(credit_card_validator(string))

    def test66(self):
        """
        Mastercard with invalid length that should return False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '542085692036474'
        self.assertFalse(credit_card_validator(string))

    def test67(self):
        """
        Mastercard with invalid length and invalid
            checksum that should return False.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '542085692036473'
        self.assertFalse(credit_card_validator(string))

    def test68(self):
        """
        Mastercard with invalid prefix that should return False.
        Prefix: invalid
        Length: valid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '222020856920364'
        self.assertFalse(credit_card_validator(string))

    def test69(self):
        """
        Mastercard with invalid prefix and checksum
            that should return False.
        Prefix: invalid
        Length: valid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '2202085692034733'
        self.assertFalse(credit_card_validator(string))

    def test70(self):
        """
        Mastercard with invalid prefix, invalid checksum,
            and invalid length that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '220208569203673'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test71(self):
        """
        Mastercard with invalid prefix, invalid checksum,
            and invalid length that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '2202085692420366'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test72(self):
        """
        Mastercard with invalid prefix and
            invalid length that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '220208569203675'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test73(self):
        """
        Mastercard with invalid prefix and
            invalid length that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '22020856924203677'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test74(self):
        """
        Mastercard with invalid length and
            invalid check bit that should return False.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '27202085692420366'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test75(self):
        """
        !!!!BUG8!!!!
        Mastercard with invalid length that should return False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '27202085692420367'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test76(self):
        """
        !!!!BUG7!!!!
        Mastercard with invalid check bit that should return False.
        Prefix: valid
        Length: valid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '2720208569242038'
        self.assertFalse(credit_card_validator(string))

    def test77(self):
        """
        Valid Mastercard with that should return True.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '2720208569242039'
        self.assertTrue(credit_card_validator(string))

    def test78(self):
        """
        !!!!BUG3!!!!
        Mastercard with invalid length and
            invalid check bit that should return false.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '272020856924236'
        self.assertFalse(credit_card_validator(string))

    def test79(self):
        """
        Mastercard with invalid length that should return False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '272020856924237'
        self.assertFalse(credit_card_validator(string))

    def test80(self):
        """
        0 that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '0'
        self.assertFalse(credit_card_validator(string))

    def test81(self):
        """
        Visa with invalid length and
            invalid check bit that should return False.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '49472647512000071'
        self.assertFalse(credit_card_validator(string))

    def test82(self):
        """
        Visa with wrong check bit that should return False.
        Prefix: valid
        Length: valid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '4947264751274357'
        self.assertFalse(credit_card_validator(string))

    def test83(self):
        """
        Amex with invalid length and
            wrong check bit that should return False.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '34472647512748'  # 14 digits
        self.assertFalse(credit_card_validator(string))

    def test84(self):
        """
        Amex with invalid length and
            wrong check bit that should return False.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '3447264755124332'
        self.assertFalse(credit_card_validator(string))

    def test85(self):
        """
        Amex with wrong check bit that should return False.
        Prefix: valid
        Length: valid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '344726475127482'
        self.assertFalse(credit_card_validator(string))

    def test86(self):
        """
        Amex with wrong check bit that should return False.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '34472647512748'  # 14 digits
        self.assertFalse(credit_card_validator(string))

    def test87(self):
        """
        Mastercard with wrong check bit that should return False.
        Prefix: valid
        Length: valid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '514726475127485'
        self.assertFalse(credit_card_validator(string))

    def test88(self):
        """
        Mastercard with incorrect length and
            wrong check bit that should return False.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '51472647512748559'
        self.assertFalse(credit_card_validator(string))

    def test89(self):
        """
        Mastercard with invalid length that should return False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '553485692036787'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test90(self):
        """
        Mastercard with invalid length and
            invalid check bit that should return False.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '553485692036786'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test91(self):
        """
        Mastercard with invalid length that should return False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '55348569203678650'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test92(self):
        """
        Mastercard with invalid length and
            invalid check bit that should return False.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '55348569203678651'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test93(self):
        """
        Valid Mastercard with invalid length that should return False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '222185692036784'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test94(self):
        """
        Valid Mastercard with invalid length and
            invalid check bit that should return False.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '222185692036785'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test95(self):
        """
        Mastercard with invalid length that should return False.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '22218569203678541'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test96(self):
        """
        Mastercard with invalid length and
            invalid check bit that should return False.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '22218569203678542'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test97(self):
        """
        Valid Mastercard in middle of range should return true.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Error Guessing.
        """
        string = '2500856920367857'
        self.assertTrue(credit_card_validator(string))

    def test98(self):
        """
        Mastercard in middle of range with
            invalid check bit should return false.
        Prefix: valid
        Length: valid
        Checksum: invalid
        Picked using Error Guessing.
        """
        string = '2500856920367856'
        self.assertFalse(credit_card_validator(string))

    def test99(self):
        """
        Valid Mastercard in middle of range with
            invalid length should return false.
        Prefix: valid
        Length: invalid
        Checksum: valid
        Picked using Error Guessing.
        """
        string = '250085692036781'  # 5 digits
        self.assertFalse(credit_card_validator(string))

    def test100(self):
        """
        Valid Mastercard in middle of range with
            invalid length should return false.
        Prefix: valid
        Length: invalid
        Checksum: invalid
        Picked using Error Guessing.
        """
        string = '250085692036782'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test101(self):
        """
        Valid Mastercard should return true.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Boundary Partition Testing.
        """
        string = '2222856920367326'
        self.assertTrue(credit_card_validator(string))

    def test102(self):
        """
        Valid Mastercard should return true.
        Prefix: valid
        Length: valid
        Checksum: valid
        Picked using Boundary Partition Testing.
        """
        string = '2719856920367458'
        self.assertTrue(credit_card_validator(string))

    def test103(self):
        """
        Mastercard with invalid prefix and
            invalid length returns false.
        Prefix: invalid
        Length: invalid
        Checksum: valid
        Picked using Boundary Partition Testing.
        """
        string = '500000000000005'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test104(self):
        """
        Mastercard with invalid prefix and
            invalid length returns false.
        Prefix: invalid
        Length: invalid
        Checksum: invalid
        Picked using Boundary Partition Testing.
        """
        string = '500000000000004'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test105(self):
        """
        Mastercard with invalid prefix returns false.
        Prefix: invalid
        Length: valid
        Checksum: valid
        Picked using Boundary Partition Testing.
        """
        string = '5000000000000009'
        self.assertFalse(credit_card_validator(string))

    def test106(self):
        """
        Mastercard with invalid prefix and
            invalid checksum returns false.
        Prefix: invalid
        Length: valid
        Checksum: invalid
        Picked using Boundary Partition Testing.
        """
        string = '5000000000000008'
        self.assertFalse(credit_card_validator(string))

    def test107(self):
        """
        Mastercard with invalid prefix,
            invalid checksum, and invalid length returns false.
        Prefix: invalid
        Length: invalid
        Checksum: valid
        Picked using Boundary Partition Testing.
        """
        string = '50000000000000005'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test108(self):
        """
        Mastercard with invalid prefix,
            invalid checksum, and invalid length returns false.
        Prefix: invalid
        Length: invalid
        Checksum: invalid
        Picked using Boundary Partition Testing.
        """
        string = '50000000000000004'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test109(self):
        """
        Mastercard with invalid prefix and invalid
            length that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '562085692036479'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test110(self):
        """
        Mastercard with invalid prefix, invalid checksum, and invalid length
            that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: invalid
        Picked using Boundary Testing.
        """
        string = '56208569203678474'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test111(self):
        """
        Mastercard with invalid prefix and
            invalid length that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '222000000000002'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test112(self):
        """
        Mastercard with invalid prefix, invalid length,
             and invalid checksum that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '222000000000003'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test113(self):
        """
        Mastercard with invalid prefix and
            invalid length that should return False.
        Prefix: invalid
        Length: valid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '2220000000000000'
        self.assertFalse(credit_card_validator(string))

    def test114(self):
        """
        Mastercard with invalid prefix and
            invalid checksum that should return False.
        Prefix: invalid
        Length: valid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '2220000000000001'
        self.assertFalse(credit_card_validator(string))

    def test115(self):
        """
        Mastercard with invalid prefix, invalid length,
            and invalid checksum that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '22200000000000001'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test116(self):
        """
        Mastercard with invalid prefix and
            invalid length that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '22200000000000002'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test117(self):
        """
        Mastercard with invalid prefix and
            invalid length that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '27210000000000009'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test118(self):
        """
        Mastercard with invalid prefix and
            invalid length that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '27210000000000008'  # 17 digits
        self.assertFalse(credit_card_validator(string))

    def test119(self):
        """
        Mastercard with invalid prefix, invalid checksum,
            invalid length that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '272100000000008'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test120(self):
        """
        Mastercard with invalid prefix and
            invalid length that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: valid
        Picked using Condition Partition Testing.
        """
        string = '272100000000009'  # 15 digits
        self.assertFalse(credit_card_validator(string))

    def test121(self):
        """
        Mastercard with invalid prefix and
            invalid checksum that should return False.
        Prefix: invalid
        Length: invalid
        Checksum: invalid
        Picked using Condition Partition Testing.
        """
        string = '2721000000000003'
        self.assertFalse(credit_card_validator(string))


if __name__ == '__main__':
    unittest.main(verbosity=2)
