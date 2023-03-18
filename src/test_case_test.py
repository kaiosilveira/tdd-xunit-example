from test_case import TestCase
from was_run import WasRun


class TestCaseTest(TestCase):
    def setUp(self) -> None:
        self.test = WasRun("testMethod")

    def testRunning(self) -> None:
        self.test.run()
        assert (self.test.wasRun)

    def testSetup(self) -> None:
        self.test.run()
        assert ("setUp " == self.test.log)


TestCaseTest("testRunning").run()
TestCaseTest("testSetup").run()
