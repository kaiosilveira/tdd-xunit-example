from test_case import TestCase
from was_run import WasRun
from test_result import TestResult
from broken_setup import TestCaseWithBrokenSetup
from test_suite import TestSuite
from broken_teardown import TestCaseWithBrokenTearDown
from no_op_test_case import NoOpTestCase


class TestCaseTest(TestCase):
    def set_up(self) -> None:
        self.result = TestResult()

    def test_template_method(self) -> None:
        test = WasRun("test_method")
        test.run(self.result)
        assert ("1 run, 0 failed" == self.result.summary())

    def test_failed_result(self) -> None:
        test = WasRun("test_broken_method")
        test.run(self.result)
        assert ("1 run, 1 failed" == self.result.summary())

    def test_failed_result_formatting(self) -> None:
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert ("1 run, 1 failed" == result.summary())

    def test_failed_set_up(self) -> None:
        test = TestCaseWithBrokenSetup("test_method")
        test.run(self.result)
        assert ("1 run, 1 failed" == self.result.summary())

    def test_suite(self) -> None:
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        suite.run(self.result)
        assert ("2 run, 1 failed" == self.result.summary())

    def test_failed_tear_down(self) -> None:
        test = TestCaseWithBrokenTearDown("test_method")
        test.run(self.result)
        assert ("1 run, 1 failed" == self.result.summary())

    def test_tear_down_called_even_if_test_fails(self) -> None:
        test = WasRun("test_broken_method")
        test.run(self.result)
        assert ("set_up test_broken_method tear_down " == test.log)

    def test_collect_all_test_names(self) -> None:
        test = NoOpTestCase('testMethod')
        assert (test.get_test_names() == ["testMethod", "testMethod2"])

    def test_returns_test_suite(self) -> None:
        suite = NoOpTestCase('testMethod').as_suite()
        assert (len(suite.tests) == 2)

        result = TestResult()
        suite.run(result)
        assert (result.summary() == "2 run, 0 failed")


suite = TestCaseTest('anything').as_suite()
result = TestResult()
suite.run(result)
print(result.summary())
