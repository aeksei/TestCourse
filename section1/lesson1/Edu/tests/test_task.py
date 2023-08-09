import time

import unittest

from task import sum


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_assertTrue(self):
        time.sleep(10)
        self.assertTrue(
            True,
            msg="Тест прошел успешно"
        )

    # def test_assertFalse(self):
    #     self.assertTrue(
    #         False,
    #         msg="Тест не прошел успешно. Описание в чем ошибка."
    #     )
