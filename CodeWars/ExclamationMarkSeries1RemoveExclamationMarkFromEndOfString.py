import unittest


def remove(s):
    return s[:-1] if s != '' and s[-1] == '!' else s


class Tests(unittest.TestCase):
    TESTS = [
        # [input, [expected]],
        ["Hi!", "Hi"],
        ["Hi!!!", "Hi!!"],
        ["!Hi", "!Hi"],
        ["!Hi!", "!Hi"],
        ["Hi! Hi!", "Hi! Hi"],
        ["Hi", "Hi"],
    ]

    def test_run_all_tests(self):
        for start, finish in self.TESTS:
            self.assertEqual(remove(start), finish)


if __name__ == '__main__':
    unittest.main()