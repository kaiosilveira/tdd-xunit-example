from test_case import TestCase


class TestCaseWithBrokenSetup(TestCase):
    def __init__(self, name) -> None:
        TestCase.__init__(self, name)

    def set_up(self) -> None:
        raise Exception

    def testMethod(self) -> None:
        pass
