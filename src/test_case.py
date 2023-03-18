from test_result import TestResult


class TestCase:

    def __init__(self, name) -> None:
        self.name = name

    def setUp(self) -> None:
        pass

    def run(self) -> None:
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return TestResult()

    def tearDown(self) -> None:
        pass
