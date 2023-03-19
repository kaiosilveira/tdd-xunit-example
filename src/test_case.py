class TestCase:

    def __init__(self, name) -> None:
        self.name = name

    def setUp(self) -> None:
        pass

    def run(self, result) -> None:
        result.testStarted()

        try:
            self.setUp()
        except:
            result.testFailed()
            return result

        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()

        try:
            self.tearDown()
        except:
            result.testFailed()

    def tearDown(self) -> None:
        pass

    def getTestNames(self):
        testNames = [testName for testName in dir(
            self) if testName.startswith("test")]
        return testNames
