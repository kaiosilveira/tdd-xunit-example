from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from test_case import TestCase


class TestSuite:
    """
    A TestSuite is a Composite of Tests
    """

    def __init__(self) -> None:
        self.tests = []

    def add(self, test: 'TestCase') -> None:
        """
        Add a test to the suite
        """
        self.tests.append(test)

    def run(self, result) -> None:
        """
        Run all the tests in the suite
        """
        for test in self.tests:
            test.run(result)
