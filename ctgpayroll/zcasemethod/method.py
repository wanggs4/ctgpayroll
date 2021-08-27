# encoding=utf8
"""
一个unittest的demo，按函数声明的顺序执行测试用例
"""
import unittest

class TestCasesOrder(unittest.TestCase):
    def test_b(self):
        print('test_b success')

    def test_a(self):
        print('test_a success')

    def test_c(self):
        print('test_c success')


class SequentialTestLoader(unittest.TestLoader):
    def getTestCaseNames(self, testCaseClass):
        test_names = super().getTestCaseNames(testCaseClass)
        testcase_methods = list(testCaseClass.__dict__.keys())
        test_names.sort(key=testcase_methods.index)
        return test_names

if __name__ == '__main__':
    unittest.main(testLoader=SequentialTestLoader())