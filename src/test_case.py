from test_result import TestResult


class TestCase:

    def __init__(self, name) -> None:
        self.name = name

    def setUp(self) -> None:
        pass

    def run(self) -> None:
        result = TestResult()
        result.testStarted()
        self.setUp()

        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()

        self.tearDown()
        return result

    def tearDown(self) -> None:
        pass
