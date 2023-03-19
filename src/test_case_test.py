from test_case import TestCase
from was_run import WasRun
from test_result import TestResult
from broken_setup import TestCaseWithBrokenSetup
from test_suite import TestSuite

class TestCaseTest(TestCase):
    def setUp(self) -> None:
        self.result = TestResult()

    def testTemplateMethod(self) -> None:
        test = WasRun("testMethod")
        test.run(self.result)
        assert ("1 run, 0 failed" == self.result.summary())

    def testFailedResult(self) -> None:
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert ("1 run, 1 failed" == self.result.summary())

    def testFailedResultFormatting(self) -> None:
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert ("1 run, 1 failed" == result.summary())

    def testFailedSetUp(self) -> None:
        test = TestCaseWithBrokenSetup("testMethod")
        test.run(self.result)
        assert ("1 run, 1 failed" == self.result.summary())

    def testSuite(self) -> None:
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert ("2 run, 1 failed" == self.result.summary())

    def testFailedTearDown(self) -> None:
        test = TestCaseWithBrokenTearDown("testMethod")
        test.run(self.result)
        assert ("1 run, 1 failed" == self.result.summary())


suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedSetUp"))
suite.add(TestCaseTest("testSuite"))
suite.add(TestCaseTest("testFailedTearDown"))

result = TestResult()
suite.run(result)
print(result.summary())
