from test_case import TestCase


class TestCaseWithBrokenSetup(TestCase):
    def __init__(self, name: str) -> None:
        TestCase.__init__(self, name)

    def set_up(self) -> None:
        raise Exception

    def test_method(self) -> None:
        pass
