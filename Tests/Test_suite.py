import unittest
from Tests.LoginTest import Login_Test
from Tests.FirefoxTs import Test
from threading import Thread
# class test_suite(Thread):
def suite1():
    tc1 = unittest.TestLoader().loadTestsFromTestCase(Login_Test)
    smokeTest = unittest.TestSuite([tc1])
    unittest.TextTestRunner(verbosity=2).run(smokeTest)
def suite2():
    tc2 = unittest.TestLoader().loadTestsFromTestCase(Test)
    smokeTest2 = unittest.TestSuite([tc2])
    unittest.TextTestRunner(verbosity=2).run(smokeTest2)

t1 = Thread(target=suite1)
t2 = Thread(target=suite2)
t1.start()
t2.start()
t1.join()
t2.join()






if __name__ == '__main__':
    unittest.main()
