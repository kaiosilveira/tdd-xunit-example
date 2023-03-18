from test_case import TestCase
from was_run import WasRun
from test_result import TestResult


class TestCaseTestWithBrokenSetup(TestCase):
    def __init__(self, name) -> None:
        TestCase.__init__(self, name)

    def setUp(self) -> None:
        raise Exception

    def testFailedSetUp(self) -> None:
        result = self.run()
        assert ("1 run, 1 failed" == result.summary())


class TestCaseTest(TestCase):
    def testTemplateMethod(self) -> None:
        test = WasRun("testMethod")
        result = test.run()
        assert ("1 run, 0 failed" == result.summary())

    def testFailedResult(self) -> None:
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert ("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self) -> None:
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert ("1 run, 1 failed" == result.summary())


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testFailedResultFormatting").run()
TestCaseTest("testFailedResult").run()
TestCaseTestWithBrokenSetup("testFailedSetUp").run()
