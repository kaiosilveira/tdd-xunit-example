from test_result import TestResult
from test_suite import TestSuite


class TestCase:
    """
    Base class for all test cases. It provides the basic
    functionality for running a test case. It also provides a method for
    creating a TestSuite from a TestCase class.
    """

    def __init__(self, name: str) -> None:
        """
        Stores the name of the test method to be run
        """
        self.name = name

    def set_up(self) -> None:
        """
        This method is called before each test method is run. It is
        intended to be overridden by subclasses.
        """

    def run(self, result: TestResult) -> None:
        """
        Runs the test case. It first calls the set_up method, then
        it runs the test method, and finally it calls the tear_down
        method. If any of these methods fail, the test case is marked
        as failed.
        """
        result.test_started()

        try:
            self.set_up()
        except:
            result.test_failed()

        try:
            method = getattr(self, self.name)
            method()
        except:
            result.test_failed()

        try:
            self.tear_down()
        except:
            result.test_failed()

    def tear_down(self) -> None:
        """
        This method is called after each test method is run. It is
        intended to be overridden by subclasses.
        """

    def get_test_names(self):
        """
        Returns a list of all test methods in the TestCase class.
        """
        test_names = [testName for testName in dir(
            self) if testName.startswith("test")]
        return test_names

    def as_suite(self):
        """
        Returns a TestSuite containing all test methods in the TestCase class.
        """
        suite = TestSuite()
        test_names = self.get_test_names()
        for test_name in test_names:
            suite.add(self.__class__(test_name))
        return suite
