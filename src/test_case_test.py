from test_case import TestCase
from was_run import WasRun
from test_result import TestResult
from broken_setup import TestCaseWithBrokenSetup
from test_suite import TestSuite
from broken_teardown import TestCaseWithBrokenTearDown
from no_op_test_case import NoOpTestCase


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

    def testTearDownCalledEvenIfTestFails(self) -> None:
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert ("setUp testBrokenMethod tearDown " == test.log)

    def testCollectAllTestNames(self) -> None:
        test = NoOpTestCase('testMethod')
        assert (test.getTestNames() == ["testMethod", "testMethod2"])

    def testReturnsTestSuite(self) -> None:
        suite = NoOpTestCase('testMethod').asSuite()
        assert (len(suite.tests) == 2)

        result = TestResult()
        suite.run(result)
        assert (result.summary() == "2 run, 0 failed")


suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedSetUp"))
suite.add(TestCaseTest("testSuite"))
suite.add(TestCaseTest("testFailedTearDown"))
suite.add(TestCaseTest("testTearDownCalledEvenIfTestFails"))
suite.add(TestCaseTest("testCollectAllTestNames"))
suite.add(TestCaseTest("testReturnsTestSuite"))

result = TestResult()
suite.run(result)
print(result.summary())
