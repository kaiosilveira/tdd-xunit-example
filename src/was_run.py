from test_case import TestCase


class WasRun(TestCase):
    def __init__(self, name) -> None:
        self.wasRun = None
        TestCase.__init__(self, name)

    def setUp(self) -> None:
        self.wasSetUp = 1

    def testMethod(self) -> None:
        self.wasRun = 1
