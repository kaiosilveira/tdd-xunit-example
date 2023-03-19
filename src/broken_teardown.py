from test_case import TestCase

class TestCaseWithBrokenTearDown(TestCase):
    def __init__(self, name: str) -> None:
        TestCase.__init__(self, name)

    def testMethod(self) -> None:
        pass

    def tearDown(self) -> None:
        raise Exception
