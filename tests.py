from nose.tools import eq_
from unittest import TestCase

from kata import chop


class TestChop(TestCase):

    def test_not_found(self):
        eq_(-1, chop(3, []))
        eq_(-1, chop(3, [1]))

        eq_(0,  chop(1, [1]))
        eq_(0,  chop(1, [1, 3, 5]))
        eq_(1,  chop(3, [1, 3, 5]))
        eq_(2,  chop(5, [1, 3, 5]))

        eq_(-1, chop(0, [1, 3, 5]))
        eq_(-1, chop(2, [1, 3, 5]))
        eq_(-1, chop(4, [1, 3, 5]))
        eq_(-1, chop(6, [1, 3, 5]))

        eq_(0,  chop(1, [1, 3, 5, 7]))
        eq_(1,  chop(3, [1, 3, 5, 7]))
        eq_(2,  chop(5, [1, 3, 5, 7]))
        eq_(3,  chop(7, [1, 3, 5, 7]))
        eq_(-1, chop(0, [1, 3, 5, 7]))
        eq_(-1, chop(2, [1, 3, 5, 7]))
        eq_(-1, chop(4, [1, 3, 5, 7]))
        eq_(-1, chop(6, [1, 3, 5, 7]))
        eq_(-1, chop(8, [1, 3, 5, 7]))

        eq_(-1, chop(8, [1, 3, 5, 7, 9, 10, 12, 14]))
        eq_(7, chop(14, [1, 3, 5, 7, 9, 10, 12, 14]))

