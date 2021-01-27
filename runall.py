import unittest

from qyyx.HTMLTestReportCN import HTMLTestRunner

suite=unittest.defaultTestLoader.discover('./case')
# suite=unittest.TestSuite()
# suite.addTest(test_demo1('test_query'))
f = open("./report/report.html", 'wb') # 二进制写格式打开要生成的报告文件
HTMLTestRunner(stream=f,title="Api Test",description="全员自动化1期api测试",tester='大鹏').run(suite)
f.close()