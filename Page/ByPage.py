from Locator.Locator import Locator
from Page.base import base
import time
import random


class ByPage(base):
    def __init__(self, driver):
        super().__init__(driver)
        self.click_by         = Locator.Click_sp
        self.add_to           = Locator.Add_to_card
        self.continue_shoping = Locator.Continue_shopping
        self.Sl_sp            = Locator.text_sl_sp
        self.Checkout         = Locator.Button_check_out
        self.Button_checkout_1 = Locator.Button_check_out_summary
        self.id                = Locator.id_email
        self.password          = Locator.pass_word
        self.sg                = Locator.By_sign
        self.proceed           = Locator.Button_address_checkout
        self.button_agree      = Locator.Button_i_agree
        self.shiping           = Locator.Button_shiping_checkout
        self.mesr              = Locator.Mesenger_by
        self.add_card01        = Locator.Add_to_card_01
        self.continue01        = Locator.Continue_01
        self.add_card02        = Locator.Add_to_card_02
        self.continue02        = Locator.Continue_02
        self.cart              = Locator.Button_cart
        self.sl                = Locator.input_sl
        self.Clear_sp          = Locator.Button_clear_sp
        self.But_check_out     = Locator.Button_check_out_by
        self.But_4             = Locator.Button_4
        self.check_out_shipping = Locator.Button_check_out_shipping
        self.sum_sp_check_out  = Locator.Get_text_sp
        self.total_sp          = Locator.Get_text_sum_sp
        # self.sale_20 = Locator.get_20
        self.img               = Locator.Click_img
        self.img2              = Locator.Img2
        self.img_img           = Locator.img_im
        self.img03             = Locator.Img_003
        self.text_im1          = Locator.Text_img_1
        self.text_im2          = Locator.text_img_2
        self.Quanti_clear      = Locator.Quantity
        self.Button_ck         = Locator.But_toncheckkk
        self.null              = Locator.Null_quantity
        self.pay_py            = Locator.click_pay_py
        self.Buttub_cf         = Locator.But_ton_confirn
        self.check_mgr         = Locator.check_merseger
        self.close_quanitity   = Locator.cloed_mull
        self.buton_add_to      = Locator.But_ton_add_to
        self.twitter           = Locator.Button_twitter
        self.Bypage_sign       = Locator.Cm_sign
        self.Go_home           = Locator.Button_go_home
        self.Button_cmt        = Locator.But_ton_cmt
        self.text_cmt_title    = Locator.Cmt_title
        self.text_cmt          =Locator.Cmt_cmt
        self.Bt_send           = Locator.Button_send
        self.check_rv          = Locator.Mer_rv
        self.Sendto_fr         = Locator.Send_to_fr
        self.Ip_name           = Locator.input_name
        self.input_email_sendkey = Locator.input_email
        self.Button_send_eml   = Locator.Button_send_email
        self.mer_fr            =Locator.mer_sento_fr
        self.id_tw             = Locator.input_id_tw
        self.password_tw       = Locator.input_password
        self.button_sign_tw    = Locator.click_buton_tw


    # Hàm click mua hàng
    def click_sp(self):
        Click_sp_by = self.find_xpath_elt(self.click_by)
        self.Click(Click_sp_by)

    # Hàm click vào phần thanh toán mua hàng
    def click_add_to_card(self):
        Add_card = self.find_xpath_elt(self.add_to)
        self.Click(Add_card)

    # Hàm click quay lại tiếp tục mua hàng
    def Click_contiue(self):
        Contine = self.find_xpath_elt(self.continue_shoping)
        self.Click(Contine)

    # Hàm click thêm sản phẩm
    def Clear_sl_sp(self):
        sl = self.find_xpath_elt(self.Sl_sp)
        self.Clear_id(sl)

    # Hàm chọn sl sản phảm
    def senkeys_sp(self, values):
        sp = self.find_xpath_elt(self.Sl_sp)
        self.senkeys(sp, values)

    # Hàm click butbon checkout
    def click_button_checkout(self):
        bt = self.find_xpath_elt(self.Checkout)
        self.Click(bt)

    # Hàm click button checkout sumary
    def click_button_sumary(self):
        bt = self.find_xpath_elt(self.Button_checkout_1)
        self.Click(bt)

    # Hàm senkey đăng nhập id
    def senkeys_id_email(self, values):
        id = self.find_xpath_elt(self.id)
        self.senkeys(id, values)

    # Hàm senkey đăng nhập password
    def senkeys_password(self, values):
        password = self.find_xpath_elt(self.password)
        self.senkeys(password, values)

    # Hàm click đăng nhập
    def click_sign(self):
        sg = self.find_xpath_elt(self.sg)
        self.Click(sg)

    # Hàm click processAddress
    def click_process_Adress(self):
        pro = self.find_xpath_elt(self.proceed)
        self.Click(pro)

    def Click_buton_agree(self):
        elt = self.find_xpath_elt(self.button_agree)
        self.Click(elt)

    # Hàm click Button checkout Shiping
    def Click_process_shiping(self):
        shiping = self.find_xpath_elt(self.shiping)
        self.Click(shiping)

    # Kiểm tra mesenger mua hàng thành công hiển thị
    def Mesger(self):
        elt = self.find_xpath_elt(self.mesr)
        if elt is not None:
            print("true")
        else:
            print("flase")

    # Hàm thêm hàng vào giỏ
    def card_01(self):
        card = self.find_xpath_elts(self.add_card02)
        conu = self.find_xpath_elt(self.continue02)
        for i in range(0 ,5):
            rand = random.randint(0 , len(card))
            for index, elt in enumerate(card):
                if index == rand:
                    self.Click(elt)
                    time.sleep(3)
                    self.Click(conu)


    # Hàm click vào cart
    def click_cart(self):
        elt = self.find_xpath_elt(self.cart)
        self.Click(elt)

    # Hàm thay đổi sl.sp
    def sl_sp(self,values):
        elt = self.find_xpath_elt(self.sl)
        self.Clear_id(elt)
        self.senkeys(elt,values)

    #Hàm xóa đi sản phẩm
    def cler_sp(self):
        elt = self.find_xpath_elt(self.Clear_sp)
        self.Click(elt)

    #Hàm click button checkout
    def check_out(self):
        elt = self.find_xpath_elt(self.But_check_out)
        self.Click(elt)

    #Hàm click terms
    def click_4(self):
        elt = self.find_xpath_elt(self.But_4)
        self.Click(elt)

    #Hàm click checkout_shipping
    def click_button_check_out_shipping(self):
        elt = self.find_xpath_elt(self.check_out_shipping)
        self.Click(elt)

    #Hàm kiểm tra số tiền thanh toán
    def sum_sp(self):
        elt = self.find_xpath_elts(self.sum_sp_check_out)
        elt1 = self.find_xpath_elt(self.total_sp)
        list = []
        for i in elt:
            list.append(self.get_text(i))
        print(list)

        list_ = []
        for a in list:
            a_ = a[1:]
            list_.append(float(a_))
        print(list_)

        sum1 = sum(list_)
        b = self.get_text(elt1)
        c = float(b.replace('$',' '))
        print(c)
        if sum1 == c :
            print(" Thành công")
        else:
            print("flase")
    def click_button_pay(self):
        elt = self.find_xpath_elt(self.pay_py)
        self.Click(elt)

    def Click_but_ton_cf(self):
        elt = self.find_xpath_elt(self.Buttub_cf)
        self.Click(elt)

    def check_m(self):
        elt = self.find_xpath_elt(self.check_mgr)
        if elt is not None:
            print("true")
        else:
            print("flase")

# Hàm click vào ảnh bất kì
    def Click_img(self):
        elt = self.find_xpath_elts(self.img)
        rand = random.randint(0, len(elt))
        for index, el in enumerate(elt):
            if index == rand:
                self.Click(el)
                time.sleep(3)

#Hàm click vào ảnh
    def Click_img2(self):
        elt = self.find_xpath_elt(self.img2)
        self.Click(elt)
# Hàm so sánh ảnh

    def img_img_height(self):
        elt = self.find_xpath_elt(self.img_img)
        a= self.get_height(elt)
        return a

    def imgimg_03_height(self):
        elt = self.find_xpath_elt(self.img03)
        b = self.get_height(elt)
        return b

# Hàm gettext dưới ảnh
    def text_img1(self):
        elt = self.find_xpath_elt(self.text_im1)
        a = self.get_text(elt)
        return a

# Hàm gettex tên sản phẩm
    def text_img02(self):
        elt = self.find_xpath_elt(self.text_im2)
        b = self.get_text(elt)
        return b

#Hàm xóa Quantity
    def Clear_quantity(self):
        elt = self.find_xpath_elt(self.Quanti_clear)
        self.Clear_id(elt)

    def sen_keys_quantity(self,valuse):
        elt = self.find_xpath_elt(self.Quanti_clear)
        self.senkeys(elt,valuse)

# check hiển bị Null Quantity
    def check_null(self):
        elt = self.find_xpath_elt(self.null)
        if elt is not None:
            print("hiển thị null quantity")
        else:
            print("flase")

# Hàm click close Null Quantity
    def close_null(self):
        elt = self.find_xpath_elt(self.close_quanitity)
        self.Click(elt)

# Hàm click mua hàng
    def click_bt_add(self):
        elt = self.find_xpath_elt(self.buton_add_to)
        self.Click(elt)

# Hàm share twitter
    def click_bt_twitter(self):
        elt = self.find_xpath_elt(self.twitter)
        self.Click(elt)

# Hàm click sign
    def Click_button_sn(self):
        elt = self.find_xpath_elt(self.Bypage_sign)
        self.Click(elt)

# Hàm về home
    def Click_button_home(self):
        elt = self.find_xpath_elt(self.Go_home)
        self.Click(elt)

# Hàm click button cmt
    def Click_button_cmt(self):
        elt = self.find_xpath_elt(self.Button_cmt)
        self.Click(elt)

# Hàm senkey title
    def sen_keys_cmt_title(self,valuse):
        elt = self.find_xpath_elt(self.text_cmt_title)
        self.senkeys(elt,valuse)

# Hàm senkey cmt
    def sen_keys_cmt(self,valuse):
        elt = self.find_xpath_elt(self.text_cmt)
        self.senkeys(elt,valuse)

# Hàm click button send
    def click_bt_send(self):
        elt = self.find_xpath_elt(self.Bt_send)
        self.Click(elt)

# Kiểm tra rivew thành công
    def check_review(self):
        elt = self.find_xpath_elt(self.check_rv)
        if elt is not None:
            print("True")
        else:
            print("flase")

# Hàm click send to fr
    def click_sento_fr(self):
        elt = self.find_xpath_elt(self.Sendto_fr)
        self.Click(elt)

#Hàm senkey name
    def senkeys_name(self,valuse):
        elt = self.find_xpath_elt(self.Ip_name)
        self.senkeys(elt,valuse)

#Hàm senkys email
    def senkey_email(self,valuse):
        elt = self.find_xpath_elt(self.input_email_sendkey)
        self.senkeys(elt,valuse)

# Hàm click send
    def click_send_enail(self):
        elt = self.find_xpath_elt(self.Button_send_eml)
        self.Click(elt)

# Hàm check gửi về email thành công
    def check_sento_el(self):
        elt = self.find_xpath_elt(self.mer_fr)
        if elt is not None:
            print("true")
        else:
            print("flase")


# Hàm senkeys_id_tt
    def send_keys_tw(self,values):
        elt = self.find_xpath_elt(self.id_tw)
        self.senkeys(elt,values)

# Hàm senkeys password
    def send_keys_pass_tw(self,valuse):
        elt = self.find_xpath_elt(self.password_tw)
        self.senkeys(elt,valuse)

#  Hàm login tw
    def click_login_tw(self):
        elt = self.find_xpath_elt(self.button_sign_tw)
        self.Click(elt)






































