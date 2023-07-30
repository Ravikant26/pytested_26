

from selenium import webdriver
class Test_credence_001:

    def test_sum_001(self):
        a = 7
        b = 3
        sum = a + b
        print('the sum of a and b is the:', str(sum))
        if sum == 10:
            assert True
            print("the test case is passed")
        else:
            assert False
            print("the test case is failed")



class Test_my_selenium_002:
    def test_sum_002(self):
        a=10
        b=20
        sum = b + a
        print('the sum of the a and b is the:' + str(sum))
        if sum == 20:
            assert True
            print("test case is passed")
        else:
            assert False
            print("test case is failed")


class Test_my_selenium_003:
    def test_sub(self):
        a=50
        b=30
        sub= a - b
        print("the sub of a and b is the:",sub)

        if sub ==20:
            assert True
            print("the selenium test case is run properly")
        else:
            assert False
            print("the selenium test case is didn't work properly")

class Test_my_sele_004:
    def test_mul_004(self):
        a=5
        b=6
        mul= a * b
        print("the multiplication of a and b is:",str(mul))

        if mul==20:
            assert False
            print("test case is failed")
        else:
            assert True
            print("test case is passed")












