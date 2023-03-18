class TestSuite:
    def __init__(self) -> None:
        self.tests = []

    def add(self, test) -> None:
        self.tests.append(test)
