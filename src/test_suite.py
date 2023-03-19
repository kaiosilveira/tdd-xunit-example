from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from test_case import TestCase


class TestSuite:
    def __init__(self) -> None:
        self.tests = []

    def add(self, test: 'TestCase') -> None:
        self.tests.append(test)

    def run(self, result) -> None:
        for test in self.tests:
            test.run(result)
