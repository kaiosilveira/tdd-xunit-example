class WasRun:
    def __init__(self, name) -> None:
        self.wasRun = None

    def testMethod(self) -> None:
        self.wasRun = 1

    def run(self) -> None:
        self.testMethod()
