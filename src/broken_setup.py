from test_case import TestCase


class TestCaseWithBrokenSetup(TestCase):
    def __init__(self, name) -> None:
        TestCase.__init__(self, name)

    def setUp(self) -> None:
        raise Exception

    def testMethod(self) -> None:
        result = self.run()
        assert ("1 run, 1 failed" == result.summary())
