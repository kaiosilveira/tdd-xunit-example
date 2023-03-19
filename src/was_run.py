from test_case import TestCase


class WasRun(TestCase):
    def __init__(self, name: str) -> None:
        TestCase.__init__(self, name)

    def set_up(self) -> None:
        self.wasRun = None
        self.log = "set_up "

    def test_method(self) -> None:
        self.wasRun = 1
        self.log = self.log + "test_method "

    def tear_down(self) -> None:
        self.log = self.log + "tear_down "

    def test_broken_method(self) -> None:
        self.log = self.log + "test_broken_method "
        raise Exception
