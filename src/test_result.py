class TestResult:
    """
    Stores the results of a test run. It keeps track of the number
    of tests that were run and the number of tests that failed.
    """

    def __init__(self) -> None:
        self.run_count = 0
        self.error_count = 0

    def test_started(self) -> None:
        """"
        Increments the number of tests that were run.
        """
        self.run_count = self.run_count + 1

    def test_failed(self) -> None:
        """
        Increments the number of tests that failed.
        """
        self.error_count = self.error_count + 1

    def summary(self):
        """
        Returns a string that summarizes the test run.
        """
        return f"{self.run_count} run, {self.error_count} failed"
