from test_suite import TestSuite


class TestCase:

    def __init__(self, name) -> None:
        self.name = name

    def set_up(self) -> None:
        pass

    def run(self, result) -> None:
        result.testStarted()

        try:
            self.set_up()
        except:
            result.testFailed()
            return result

        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()

        try:
            self.tear_down()
        except:
            result.testFailed()

    def tear_down(self) -> None:
        pass

    def get_test_names(self):
        testNames = [testName for testName in dir(
            self) if testName.startswith("test")]
        return testNames

    def as_suite(self):
        suite = TestSuite()
        testNames = self.get_test_names()
        for testName in testNames:
            suite.add(self.__class__(testName))
        return suite
