from test_case import TestCase


class WasRun(TestCase):
    def __init__(self, name) -> None:
        TestCase.__init__(self, name)

    def setUp(self) -> None:
        self.wasRun = None
        self.log = "setUp "

    def testMethod(self) -> None:
        self.wasRun = 1
        self.log = self.log + "testMethod "

    def tearDown(self) -> None:
        self.log = self.log + "tearDown "
