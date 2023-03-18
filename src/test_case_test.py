from test_case import TestCase
from was_run import WasRun


class TestCaseTest(TestCase):
    def setUp(self) -> None:
        self.test = WasRun("testMethod")

    def testTemplateMethod(self) -> None:
        self.test.run()
        assert ("setUp testMethod " == self.test.log)


TestCaseTest("testTemplateMethod").run()
