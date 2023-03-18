from test_case import TestCase
from was_run import WasRun


class TestCaseTest(TestCase):
    def testTemplateMethod(self) -> None:
        test = WasRun("testMethod")
        result = test.run()
        assert ("1 run, 0 failed" == result.summary())


TestCaseTest("testTemplateMethod").run()
