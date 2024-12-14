# Đối với phương thức muốn truy cập vào các thuộc tính ta cần tham số self
'''class Infor_User:
    def __init__(self, taikhoan, matkhau, diachi):
        self.taikhoan = taikhoan
        self.matkhau = matkhau
        self.diachi = diachi
    def GetInfo(self):
        print(self.taikhoan, self.diachi)
    def UpdateInfo(self):
        new_account = input("Cập nhật tài khoản: ")
        new_address = input("Cập nhật địa chỉ: ")
        self.taikhoan = new_account
        self.diachi = new_address
user2 = Infor_User("user2","1234","urmamagay1@gmail.com")
user = Infor_User("user1","123","urmamafat1@gmail.com")
user.GetInfo()
user.UpdateInfo()
user.GetInfo()
B1:
class Student:
    def __init__(self, ten, tuoi, diemtoan, diemvan):
        self.ten = ten
        self.tuoi = tuoi
        self.diemtoan = diemtoan
        self.diemvan = diemvan
    def average_scr(self):
        print(self.diemtoan + self.diemvan)
student1 = Student("Vũ Văn A", 14, 8, 9.75)
student1.average_scr()'''
'''B2:
class Product:
    def __init__(self, ten, giaca, soluong):
        self.ten = ten
        self.giaca = giaca
        self.soluong = soluong
    def amount_prdct(self):
        print(self. soluong)
khachhang1 = Product("Nguyễn Thái B", 40000, 1)
khachhang1.amount_prdct
print(f"Kho hàng của {khachhang1.ten} đang có {khachhang1.soluong} sản phẩm")
if khachhang1.soluong > 0:
    print("Tình trạng: Còn hàng")
else:
    print("Tình trạng: Hết hàng")'''
'''B3:
class BankAccount:
    def __init__(self, cardname, cardnumber, coems):
        self.cardname = cardname
        self.cardnumber = cardnumber
        self.coems = coems
    def InputCoems(self):
        added_coems = int(input("Hãy nhập số tiền muốn nạp vào(VND): "))
        new_coems = self.coems + added_coems
        self.coems = new_coems
customer1 = BankAccount("0 biết", "12345678", 40000)
customer1.InputCoems()
print(f"Người dùng {customer1.cardname} có số tiền là {customer1.coems}")'''
