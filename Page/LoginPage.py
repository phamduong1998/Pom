from Locator.Locator import Locator
from selenium import webdriver
from Page.base import base
import time
class LoginPage(base):
    def __init__(self, driver):
        super().__init__(driver)
    #Login locator
        self.Click_Sign1  = Locator.click_Sign
        self.Email1       = Locator.Email_addrees
        self.Create1      = Locator.Create_an_account
    # đăng kí account
        self.Title        = Locator.Title
        self.F_name       = Locator.First_name
        self.L_name       = Locator.Last_name
        self.Email12      = Locator.Email
        self.Password     = Locator.Password
        self.days         = Locator.Days
        self.click_day    = Locator.Click_days
        self.months       = Locator.Months
        self.click_months = Locator.Click_Months
        self.year         = Locator.Year
        self.click_year   = Locator.Click_year
        self.company      = Locator.compaly
        self.addrres      = Locator.adrres
        self.addrres02    = Locator.adrres02
        self.city         = Locator.City
        self.stat        = Locator.State
        self.stat01      = Locator.State01
        self.zip1         = Locator.zipcode
        self.Additi       = Locator.Additional
        self.H_phone      = Locator.Home_phone
        self.M_phone      = Locator.Mobile_phone
        self.Register1    = Locator.Register
        # self.text = Locator.text
# Click vào sign
    def SignIn(self):
        elt =  self.find_xpath_elt(self.Click_Sign1)
        time.sleep(2)
        self.Click(elt)
# Điền vào Email đăng kí
    def Get_Email(self,values):
        id = self.find_xpath_elt(self.Email1)
        self.senkeys(id,values)
# Click vào đăng kí email
    def Buttun(self):
        Create = self.find_xpath_elt(self.Create1)
        self.Click(Create)
        time.sleep(3)
# Hàm xóa email
    def clear_id(self):
        email_id = self.find_xpath_elt(self.Email1)
        self.Clear_id(email_id)

# Hàm click vào title
    def click_title(self):
        title = self.find_xpath_elt(self.Title)
        self.Click(title)

# Hàm nhập First name
    def first_name(self,values):
        first = self.find_xpath_elt(self.F_name)
        self.senkeys(first,values)

# Hàm nhập Last name
    def set_last_name(self,values):
        last = self.find_xpath_elt(self.L_name)
        self.senkeys(last,values)
#Hàm xóa email cũ
    def clear_em(self):
        cl_em = self.find_xpath_elt(self.Email12)
        self.Clear_id(cl_em)

# Hàm nhập eamil đăng kí
    def email(self,values):
        email = self.find_xpath_elt(self.Email12)
        self.senkeys(email,values)

# Hàm nhập password
    def passw(self,values):
        passwor = self.find_xpath_elt(self.Password)
        self.senkeys(passwor,values)

# Hàm nhập ngày tháng năm sinh
    def date_birth(self):
        day = self.find_xpath_elt(self.days)
        self.Click(day)
        time.sleep(3)
        click_day = self.find_xpath_elt(self.click_day)
        self.Click(click_day)
        time.sleep(2)

# Hàm nhập tháng sinh
    def Months(self):
        month = self.find_xpath_elt(self.months)
        self.Click(month)
        time.sleep(2)
        click_month = self.find_xpath_elt(self.click_months)
        self.Click(click_month)
        time.sleep(2)

# Hàm nhập năm sinh
    def years(self):
        years = self.find_xpath_elt(self.year)
        self.Click(years)
        time.sleep(2)
        click_years = self.find_xpath_elt(self.click_year)
        self.Click(click_years)

#Hàm nhập tên cty
    def compaly1(self,values):
        compa = self.find_xpath_elt(self.company)
        self.senkeys(compa,values)

#Hàm nhập địa chỉ cty
    def adrres(self,values):
        addrres = self.find_xpath_elt(self.addrres)
        self.senkeys(addrres,values)

#Hàm nhập địa chỉ 2
    def adrres02(self,values):
        addres02 = self.find_xpath_elt(self.addrres02)
        self.senkeys(addres02,values)

#Hàm nhập thành phố
    def citys(self,values):
        city = self.find_xpath_elt(self.city)
        self.senkeys(city,values)

#Hàm chọn tiểu bang
    def state01(self):
        sta = self.find_xpath_elt(self.stat)
        self.Click(sta)
        time.sleep(2)
        sta01 = self.find_xpath_elt(self.stat01)
        self.Click(sta01)
        time.sleep(2)

#Hàm nhập zip code
    def zip(self,valuse):
        zip_code = self.find_xpath_elt(self.zip1)
        self.senkeys(zip_code,valuse)

#Hàm nhập thông tin thêm
    def thongtin(self,valuse):
        addti = self.find_xpath_elt(self.Additi)
        self.senkeys(addti,valuse)

#Hàm nhập sđt
    def Phone(self,valuse):
        phone = self.find_xpath_elt(self.H_phone)
        self.senkeys(phone,valuse)

#Hàm nhập moblie phone
    def m_phone(self,valuse):
        Mb_phone = self.find_xpath_elt(self.M_phone)
        self.senkeys(Mb_phone,valuse)

#Hàm hoàn thành đăng kí
    def register(self):
        re = self.find_xpath_elt(self.Register1)
        self.Click(re)











