from Locator.Locator import Locator
from Page.base import base
import time
class HomePage(base):
    def __init__(self,driver):
        super().__init__(driver)
        self.News       = Locator.Newsletter
        self.Enter      = Locator.Enter_email
        self.Conta_us   = Locator.contact
        self.Heading    = Locator.Subjec_Heading
        self.Heading01  = Locator.Subjec_Heading01
        self.Home_email = Locator.Home_email_add
        self.Oder       = Locator.Order_reference
        self.actack     = Locator.Attach
        self.send       = Locator.Send
        self.Message    = Locator.Mensenger
        self.sear       = Locator.Search
        self.text1      = Locator.text_ser
        self.But_ton    =Locator.But_ton_sea
        self.sp         = Locator.li_sp
        self.slsp         = Locator.so_sp
        self.gia        = Locator.gia_sp
        self.meserger_sear = Locator.Mensenger_sear

# Hàm điền email vào Newsletter
    def Newslet(self,valuse):
        newslette = self.find_xpath_elt(self.News)
        self.senkeys(newslette,valuse)

# Hàm click enter_email
    def enter_em(self):
        enter_el = self.find_xpath_elt(self.Enter)
        self.Click(enter_el)

# Hàm click vào Contact us
    def Conta(self):
        Con_us = self.find_xpath_elt(self.Conta_us)
        self.Click(Con_us)
#Hàm chọn Heading
    def Head(self):
        Hea = self.find_xpath_elt(self.Heading)
        self.Click(Hea)

        Hea01 = self.find_xpath_elt(self.Heading01)
        self.Click(Hea01)

#Hàm điềm email
    def E_mail(self,values):
        Em = self.find_xpath_elt(self.Home_email)
        self.senkeys(Em,values)
# Hàm điền Order reference
    def oder_pr(self,values):
        oder_p = self.find_xpath_elt(self.Oder)
        self.senkeys(oder_p,values)
# Hàm Attach File
    def File(self,values):
        At_file = self.find_xpath_elt(self.actack)
        self.senkeys(At_file,values)

#Hàm click send
    def send_click(self):
        Click_send = self.find_xpath_elt(self.send)
        self.Click(Click_send)

# Hàm điền vào mesenger
    def mess(self,values):
        messr = self.find_xpath_elt(self.Message)
        self.senkeys(messr,values)

# Hàm điền vào tìm kiếm
    def search(self,values):
        sea = self.find_xpath_elt(self.sear)
        self.senkeys(sea,values)
# Hàm xóa tìm kiếm
    def clea_sear(self):
        clea = self.find_xpath_elt(self.sear)
        self.Clear_id(clea)
# Hàm chụp ảnh
    def Scree(self,values):
        Scr = self.find_xpath_elt(self.sear)
        self.screenshot(Scr,values)
# Lấy tên gợi ý khi tìm kiếm
    def get_list(self):
        list = []
        elt = self.find_xpath_elts(self.text1)
        for  elt1 in elt:
            # print(self.get_text(elt1))
            list.append(self.get_text(elt1))

        return list
# Hàm click vào ô tìm kiếm
    def Click_ser(self):
        But_ton_sea = self.find_xpath_elt(self.But_ton)
        self.Click(But_ton_sea)
# Hàm lấy tên sản phẩm sau khi tìm kiếm
    def srt_lits_sp(self):
        list_sp = []
        all_sp = self.find_xpath_elts(self.sp)

        for sp_li in all_sp:
            list_sp.append(self.get_text(sp_li))
        print(list_sp)
        return list_sp
#lấy text của số lượng sản phẩm
    def get_te_sl(self):

        sl_sp = self.find_xpath_elt(self.slsp)
        print(self.get_text(sl_sp))
#Hàm check  thông tin giá cả
    def check_gia(self):
        che_gia =self.find_xpath_elt(self.gia)
        #self.get_text(che_gia)
        if che_gia is not None:
            print('thành công')
        else:
            print('flase')
# check message khi tìm kiếm sai hiển thị
    def check_mes_sear(self):
        check_mes = self.find_xpath_elt(self.meserger_sear)
        if check_mes is not None:
            print('true')
        else:
            print('flase')










