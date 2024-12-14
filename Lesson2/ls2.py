# Khi def nằm trong class thì sẽ đc hiểu là phương thức của class đó
# self python sẽ tự động lấy ra tên đối tượng được khởi tạo và gán vào self
# Phương thức __init__ chỉ được gọi khi khai báo đủ tham số đầu vào
class Car:
    def __init__(self, loai_xe, so_cho_ngoi, so_banh_xe, gia_tien):
        self.LoaiXe = loai_xe
        self.SoChoNgoi = so_cho_ngoi
        self.SoBanhXe = so_banh_xe
        self.GiaTien = gia_tien
Oto_con = Car("Xe con", 6, 4, 205000)
Oto_tải = Car("Xe tải", 2, 8, 405000)
print(Oto_con.LoaiXe)