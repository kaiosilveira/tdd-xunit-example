from test_case import TestCase
from was_run import WasRun


class TestCaseTest(TestCase):
    def testTemplateMethod(self) -> None:
        test = WasRun("testMethod")
        test.run()
        assert ("setUp testMethod tearDown " == test.log)


TestCaseTest("testTemplateMethod").run()
