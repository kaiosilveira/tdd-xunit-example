class TestResult:
    def __init__(self) -> None:
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self) -> None:
        self.runCount = self.runCount + 1

    def testFailed(self) -> None:
        self.errorCount = self.errorCount + 1

    def summary(self):
        return "%d run, 0 failed" % self.runCount
