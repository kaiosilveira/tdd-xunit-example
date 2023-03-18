from test_result import TestResult


class TestSuite:
    def __init__(self) -> None:
        self.tests = []

    def add(self, test) -> None:
        self.tests.append(test)

    def run(self) -> None:
        result = TestResult()
        for test in self.tests:
            test.run(result)
        return result
