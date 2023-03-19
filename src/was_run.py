from test_case import TestCase


class WasRun(TestCase):
    def __init__(self, name) -> None:
        TestCase.__init__(self, name)

    def set_up(self) -> None:
        self.wasRun = None
        self.log = "setUp "

    def testMethod(self) -> None:
        self.wasRun = 1
        self.log = self.log + "testMethod "

    def tear_down(self) -> None:
        self.log = self.log + "tearDown "

    def testBrokenMethod(self) -> None:
        self.log = self.log + "testBrokenMethod "
        raise Exception
