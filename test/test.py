from hamcrest import *
import unittest
import mock
import calculator.calc
from calculator import calc

calc1 = calculator.calc.Calculator(2, 3, 3.0, 8.4, "dwa", "razy")


class TestSum(unittest.TestCase):
    def testEquals(self):
        assert_that(calc1.summary(), equal_to(5.0))

    def testRevString(self):
        assert_that(calc1.concat(), equal_to("dwarazy"))

    def testLength(self):
        assert_that(calc1.concat(), has_length(7))

    def testInstance(self):
        assert_that(calc1, instance_of(object))

    def testCloseToValue(self):
        assert_that(calc1.multiply(), close_to(25.0, 0.3))

    def testHasString(self):
        assert_that(calc1.concat(), contains_string("razy"))

    def testRaiseValueError(self):
        calc2 = calculator.calc.Calculator(1, -1, 3.0, 8.4, "dwa", "razy")
        assert_that(calling(calc2.get_range()), raises(Exception))

    def testRaiseValueErrorMult(self):
        calc2 = calculator.calc.Calculator(1, -1, 3.0, 8.4, "dwa", "razy")
        assert_that(calling(calc2.negativeFunctionVal()), raises(Exception))



if __name__ == '__main__':
    unittest.main(verbosity=2)
