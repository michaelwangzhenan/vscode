import unittest
from py1_basic import test_ut
from py5_class import FirstClass


class testUnitCase(unittest.TestCase):
    def testCase1(self):
        result = test_ut('a', 'z')
        self.assertEqual(result, "a:z")

    def testCase2(self):
        result = test_ut('www.xxx.com', '8080')
        self.assertNotEqual(result, "www.xxxx.com:8080")

    def testCase3(self):
        result = test_ut("你好", "端口")
        self.assertTrue(result == "你好:端口")

    def testxxxxx_Case4(self):  # 测试用例好像必须 是以 "test" 开头的，其它名字将不会在 main() 里运行
        result = test_ut("你好", "端口")
        self.assertFalse(result == "hello:port")

    def testCase5(self):
        list_result = ["a:z", "b:d"]
        result = test_ut('a', 'z')
        self.assertIn(result, list_result)

    def testCase6(self):
        list_result = ["a:z", "b:d"]
        result = test_ut('c', 'z')
        self.assertNotIn(result, list_result)


class testFirstClass(unittest.TestCase):
    def setUp(self):
        self.obj = FirstClass()
        self.a = [1, 2, 3]
        self.b = [100, 200, 300]
        self.ret = [101, 202, 303]

    def test1(self):
        for i in range(3):
            self.assertEqual(self.ret[i], self.obj.sum(self.a[i], self.b[i]))

    def testvar1(self):
        self.var1 = 1
        self.assertEqual(self.var1, 1)
        self.assertEqual(FirstClass.var1, 0)

    def testvar2(self):
        self.var2 = 'abc'
        self.assertTrue(self.var2 == 'abc')
        self.assertTrue(FirstClass.var2 == 'First')


if __name__ == '__main__':
    unittest.main()
