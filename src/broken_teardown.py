from test_case import TestCase


class TestCaseWithBrokenTearDown(TestCase):
    def __init__(self, name: str) -> None:
        TestCase.__init__(self, name)

    def test_method(self) -> None:
        pass

    def tear_down(self) -> None:
        raise Exception
