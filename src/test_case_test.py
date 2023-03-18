from test_case import TestCase
from was_run import WasRun


class TestCaseTest(TestCase):
    def testRunning(self) -> None:
        test = WasRun("testMethod")
        assert (not test.wasRun)
        test.run()
        assert (test.wasRun)

    def testSetup(self) -> None:
        test = WasRun("testMethod")
        test.run()
        assert (test.wasSetUp)


TestCaseTest("testRunning").run()
TestCaseTest("testSetup").run()
