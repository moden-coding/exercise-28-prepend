#!/usr/bin/env python3

import contextlib
import io
import unittest

from src.prepend import Prepend


class PrependTest(unittest.TestCase):

    def test_first(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            p = Prepend("+++ ")
            p.write("Hello")
            p.write("Goodbye")
        result = buf.getvalue().strip('\n').split('\n')
        self.assertEqual(
            len(result), 2,
            msg="Two calls to write() should produce exactly two lines "
            "of output. Got %r." % (result,))
        self.assertEqual(
            result[0], "+++ Hello",
            msg="Prepend('+++ ').write('Hello') should print '+++ Hello'. "
            "Got %r." % (result[0],))
        self.assertEqual(
            result[1], "+++ Goodbye",
            msg="Prepend('+++ ').write('Goodbye') should print "
            "'+++ Goodbye'. Got %r." % (result[1],))

    def test_different_prefix(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            p = Prepend(">> ")
            p.write("one")
        result = buf.getvalue().strip('\n').split('\n')
        self.assertEqual(
            result[0], ">> one",
            msg="Prepend('>> ').write('one') should print '>> one', using "
            "whatever prefix was passed to the constructor, not a "
            "hard-coded one. Got %r." % (result[0],))

    def test_empty_prefix_prints_text_unchanged(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            p = Prepend("")
            p.write("bare")
        result = buf.getvalue().strip('\n').split('\n')
        self.assertEqual(
            result[0], "bare",
            msg="Prepend('').write('bare') should print 'bare' unchanged "
            "when the prefix is an empty string. Got %r." % (result[0],))


if __name__ == '__main__':
    unittest.main()
