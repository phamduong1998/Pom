import threading
from  threading import Thread
from cv2.gapi.ie import params
from selenium import webdriver
import pytest
import unittest
import time
from Page.LoginPage import LoginPage
from Page.Homepage import HomePage
from Locator.Locator import Locator
from Page.ByPage import ByPage
import cv2


class Login_Test(unittest.TestCase):
    # @pytest.fixture(params=["chrome", "firefox"], scope="class")
    def setUp(self):
        # if request.params == "chrome":
        self.driver = webdriver.Chrome(executable_path="G:\selenium\chromedriver.exe")
        self.driver.get("http://automationpractice.com/index.php")
        # elif request.params == "firefox":
        #     self.driver = webdriver.Firefox(executable_path="G:\selenium\geckodriver-v0.29.0-win64 (1)\geckodriver.exe")
        # pass

        # @pytest.fixture(params=["chrome", "firefox"], scope="class")
        # def driver_init(request):
        #     if request.param == "chrome":
        #         self.driver = webdriver.Chrome(executable_path="G:\selenium\chromedriver.exe")
        #         self.driver.get("http://automationpractice.com/index.php")
        #     if request.param == "firefox":
        #         self.driver = webdriver.Firefox(executable_path="G:\selenium\geckodriver-v0.29.0-win64 (1)\geckodriver.exe")

        #     # request.cls.driver = web_driver
        #     # yield
        #     # web_driver.close()
        #
        # elif params == "firefox":
        #     self.driver = webdriver.Firefox(executable_path="G:\selenium\geckodriver-v0.29.0-win64 (1)\geckodriver.exe")
        # self.driver = webdriver.Chrome(executable_path="G:\selenium\chromedriver.exe")
        # self.driver = webdriver.Firefox(executable_path="G:\selenium\geckodriver-v0.29.0-win64 (1)\geckodriver.exe")
        # if params == "chrome":
        #     self.driver = webdriver.Chrome(executable_path="G:\selenium\chromedriver.exe")
        # elif params == "firefox":
        #     self.driver = webdriver.Firefox(executable_path="G:\selenium\geckodriver-v0.29.0-win64 (1)\geckodriver.exe")
        # self.driver.get("http://automationpractice.com/index.php")



    # TestCae01: Lỗi khi nhập 1 email adress không hợp lệ
    def login(self):
        Login = LoginPage(self.driver)
        Login.SignIn()
        Login.Get_Email("abc123")
        Login.Buttun()
        Messengerbox = self.driver.find_element_by_xpath(Locator.Mesenger01)
        if Messengerbox is not None:
            print('True')
        else:
            print('False')
        self.driver.quit()



    # t Test 02 tạo account
    def test_Account(self):
        Lg = LoginPage(self.driver)
        Lg.SignIn()
        # Lg.clear_em()
        # time.sleep(2)
        Lg.Get_Email("du58on6d655st6565dfgdg7g65@gmail.com")
        Lg.Buttun()
        Lg.click_title()
        Lg.first_name("Dương")
        Lg.set_last_name("phạm")
        # Lg.email("duong055689@gmail.com")
        Lg.passw("anhduong")
        Lg.date_birth()
        Lg.Months()
        Lg.years()
        Lg.compaly1("Lqa")
        Lg.adrres("Nguyen co thach, Ha noi")
        Lg.adrres02("Hai duong, Binh giang")
        Lg.citys("Ha noi")
        Lg.state01()
        Lg.zip("00000")
        Lg.thongtin("khong co gi")
        Lg.Phone("0978454157")
        Lg.m_phone("03569445")
        Lg.register()
        # time.sleep(50)
        my_account = self.driver.find_element_by_xpath(Locator.My_account)
        if my_account is not None:
            print('Đăng kí thành công')
        else:
            print('False')

    # Testcase03 Submit a newsletter
    def test_03(self):
        Ts03 = HomePage(self.driver)
        Ts03.Newslet("anc99b@gmail.com")
        Ts03.enter_em()

        newsletter = self.driver.find_element_by_xpath(Locator.newlet)
        if newsletter is not None:
            print(" Thành công")
        else:
            print('false')

    # test04: Submit a contact form
    def test_04(self):
        Ts04 = HomePage(self.driver)
        Ts04.Conta()
        Ts04.Head()
        Ts04.E_mail("anmmc@gmail.com")
        Ts04.oder_pr("duong")
        Ts04.File("G:\IMG_0948.JPG")
        Ts04.mess("khong")
        Ts04.send_click()
        th = self.driver.find_element_by_xpath(Locator.th)
        if th is not None:
            print('Thành công')
        else:
            print('Flase')

    # Test05
    def test_05(self):
        Ts05 = HomePage(self.driver)
        Ts05.search("abcdl")
        Ts05.Scree("1.png")
        time.sleep(3)
        Ts05.clea_sear()
        Ts05.Scree("2.png")
        img1 = cv2.imread("1.png")
        img2 = cv2.imread("2.png")

    # test_06
    def test_06(self):
        Ts06 = HomePage(self.driver)
        Ts06.search("Dress")
        time.sleep(5)
        lt = Ts06.get_list()
        for a in lt:
            if 'Dress' in a:
                print('true')
                # self.assertTrue(True)
            else:
                print('flase')
                # self.assertTrue(False)
        print(lt)

    def test_07(self):
        Ts07 = HomePage(self.driver)
        Ts07.search("Dress")
        time.sleep(3)
        Ts07.Click_ser()
        a = Ts07.srt_lits_sp()
        for i in a:
            if 'Dress' in i:
                print('true')
            # self.assertTrue(True)
            else:
                print('false')
                # self.assertTrue(False)

    def test_08(self):
        Ts08 = HomePage(self.driver)
        Ts08.search("Dress")
        Ts08.Click_ser()
        a = Ts08.srt_lits_sp()
        b = len(a)
        c = Ts08.get_te_sl()
        b1 = str(b)
        b2 = str(c)
        for b1 in b2:
            if b1 in b1:
                print('true')
            else:
                print('flase')

    # Gía cả hiển thị với sản phẩm
    def test_09(self):
        Ts09 = HomePage(self.driver)
        Ts09.search("Dress")
        Ts09.Click_ser()
        Ts09.check_gia()

    # Nhập sai sản phẩm, message sai sản phẩm hiển thị
    # def test_10(self):
    #     Ts10 = HomePage(self.driver)
    #     Ts10.search("dreSSSsss")
    #     Ts10.Click_ser()
    #     Ts10.check_mes_sear()
    #
    # # Mua hàng thành công
    # def test_11(self):
    #     Ts11 = ByPage(self.driver)
    #     Ts11.click_sp()
    #     Ts11.click_add_to_card()
    #     time.sleep(3)
    #     Ts11.Click_contiue()
    #     Ts11.Clear_sl_sp()
    #     Ts11.senkeys_sp("3")
    #     Ts11.click_add_to_card()
    #     time.sleep(3)
    #     Ts11.click_button_checkout()
    #     Ts11.click_button_sumary()
    #     Ts11.senkeys_id_email("duong055689@gmail.com")
    #     Ts11.senkeys_password("anhduong1")
    #     Ts11.click_sign()
    #     Ts11.click_process_Adress()
    #     # Ts11.Click_buton_agree()
    #     # time.sleep(600)
    #     Ts11.Click_process_shiping()
    #     time.sleep(3)
    #     Ts11.Mesger()
    #
    # # Thay đổi thông tin mua hàng
    # def test_12(self):
    #     Ts_12 = ByPage(self.driver)
    #     Ts_12.card_01()
    #     Ts_12.click_cart()
    #     time.sleep(3)
    #     Ts_12.sl_sp("3")
    #     Ts_12.cler_sp()
    #     Ts_12.check_out()
    #     Ts_12.senkeys_id_email("duong055689@gmail.com")
    #     Ts_12.senkeys_password("anhduong1")
    #     Ts_12.click_sign()
    #     Ts_12.click_process_Adress()
    #     Ts_12.click_4()
    #     Ts_12.click_button_check_out_shipping()
    #     Ts_12.sum_sp()
    #     Ts_12.click_button_pay()
    #     Ts_12.Click_but_ton_cf()
    #     Ts_12.check_m()
    #     # time.sleep(300)
    #     #
    #     # time.sleep(1000)
    #
    # # tìm hàng khuyến mại 20%
    # def test_13(self):
    #     TS_13 = ByPage(self.driver)
    #
    # # Kiểm tra chức năng View large, và tên sản phẩm ở dưới ảnh
    # def test_14(self):
    #     Ts_14 = ByPage(self.driver)
    #     # time.sleep(3)
    #     Ts_14.Click_img()
    #     text1 = Ts_14.text_img02()
    #     Ts_14.Click_img2()
    #     time.sleep(5)
    #     Ts_14.img_img_height()
    #     Ts_14.imgimg_03_height()
    #     a = Ts_14.img_img_height()
    #     b = Ts_14.imgimg_03_height()
    #     if a == b:
    #         print("False")
    #     else:
    #         print("true")
    #     text2 = Ts_14.text_img1()
    #     if text1 == text2:
    #         print("true")
    #     else:
    #         print("flase")
    #
    # # Add to cart với Quantity =0
    # def test_15(self):
    #     Ts15 = ByPage(self.driver)
    #     Ts15.Click_img()
    #     Ts15.Clear_quantity()
    #     Ts15.sen_keys_quantity("0")
    #     Ts15.click_add_to_card()
    #     time.sleep(3)
    #     Ts15.check_null()
    #     # Add to cart với Quantity > 0
    #     Ts15.Clear_quantity()
    #     Ts15.sen_keys_quantity("1")
    #     Ts15.close_null()
    #     Ts15.click_bt_add()
    #
    # # Share to TWitter
    # def test_16(self):
    #     driver = self.driver
    #     Ts16 = ByPage(driver)
    #     Ts16.Click_img()
    #     # get the window handle after the window has opened
    #     window_before = driver.window_handles[0]
    #
    #     # window_before_title = driver.title
    #     # print(window_before_title)
    #
    #     Ts16.click_bt_twitter()
    #     time.sleep(2)
    #     # get the window handle after a new window has opened
    #     window_after = driver.window_handles[1]
    #
    #     # switch on to new child window
    #     driver.switch_to.window(window_after)
    #     time.sleep(10)
    #
    #     # window_after_title = driver.title
    #     # print(window_after_title)
    #     # time.sleep(3)
    #     Ts16.send_keys_tw("Dng74437507")
    #     Ts16.send_keys_pass_tw("anhduong1")
    #     Ts16.click_login_tw()
    #
    #     # driver.switch_to.window(window_before)
    #     # time.sleep(500)
    #
    # # Comment
    # def test_17(self):
    #     Ts17 = ByPage(self.driver)
    #     Ts17.Click_button_sn()
    #     time.sleep(3)
    #     Ts17.senkeys_id_email("duong055689@gmail.com")
    #     Ts17.senkeys_password("anhduong1")
    #     Ts17.click_sign()
    #     time.sleep(3)
    #     Ts17.Click_button_home()
    #     Ts17.Click_img()
    #     Ts17.Click_button_cmt()
    #     Ts17.sen_keys_cmt_title("Bình luận")
    #     Ts17.sen_keys_cmt("Sản phẩm tốt")
    #     Ts17.click_bt_send()
    #     Ts17.check_review()
    #
    # # Send to friend
    #
    # def test_18(self):
    #     Ts18 = ByPage(self.driver)
    #     Ts18.Click_img()
    #     Ts18.click_sento_fr()
    #     Ts18.senkeys_name("Dương")
    #     Ts18.senkey_email("Duong055689@gmail.com")
    #     Ts18.click_send_enail()
    #     Ts18.check_sento_el()
    #     # TODO
    #
    # # def test_action(self):
    # #     browsers = ["chrome", "firefox"]
    # #     for browser in browsers:
    # #         Thread(target=self.login, args=(browser,)).start()
    #


    def tearDown(self):
        self.driver.quit()
        print('tearDown')


if __name__ == '__main__':
    unittest.main()
