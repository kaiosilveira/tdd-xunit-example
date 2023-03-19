from test_result import TestResult


class TestSuite:
    def __init__(self) -> None:
        self.tests = []

    def add(self, test) -> None:
        self.tests.append(test)

    def run(self, result) -> None:
        for test in self.tests:
            test.run(result)
