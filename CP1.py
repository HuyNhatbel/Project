# Trắc nghiệm: 1D 2A 3C 4A 5A 6A 7B 8A 9D 10 11A 12B 13A 14 15A 16B 17A 18C 19D 20C
# Tự  luận:
# Câu 1:    
class HinhVuong:
    def __init__(self, dodaicanh):
        self.dodaicanh = float(dodaicanh)
    def tinh_chu_vi(self):
        return self.dodaicanh * 4
# Câu 2:
class HocSinh:
    def __init__(self, hoten, diachi, chieucao, cannang, hocluc):
        self.hoten = hoten
        self.diachi = diachi
        self.chieucao = chieucao
        self.cannang = cannang
        self.hocluc = hocluc
    def add_student(self):
        self.newest_hoten = input("Nhập họ và tên học sinh: "),
        self.newest_diachi = input("Nhập địa chỉ: "), 
        self.newest_chieucao = input("Nhập chiều cao: "),
        self.newest_cannang = input("Nhập cân nặng: "),
        self.newest_hocluc = input("Nhập học lực: ")
        self.newest_hoten = self.hoten
        self.newest_diachi = self.diachi
        self.newest_chieucao = self.chieucao
        self.newest_cannang = self.cannang
        self.newest_hocluc = self.hocluc
    def change_address(self):
        self.new_address = input("Nhập địa chỉ nhà mới: ")
        self.diachi = self.new_address
    def change_height_weight(self):
        self.new_height = input("Nhập chiều cao mới: ")
        self.new_weight = input("Nhập cân nặng: ")
        self.chieucao = self.new_height
        self.cannang = self.new_weight
    def display(self):
        print("Họ và tên", student1.hoten, "Địa chỉ", student1.diachi, "Chiều cao", student1.chieucao, "Cân nặng", student1.cannang, "Học lực", student1.hocluc)
student1 = HocSinh("Nguyễn Văn A", "Phường A", "1.7m", "49 kg", "Giỏi")
out  = True
while out == True:
    print("Các lựa chọn:")
    print("1. Thêm học sinh")
    print("2. Đổi địa chỉ")
    print("3. Cập nhật chiều cao, cân nặng")
    print("4. Hiển thị thông tin học sinh")
    choice = int(input())
    if choice == 1:
        student1.add_student()
    elif choice == 2:
        student1.change_address()
    elif choice == 3:
        student1.change_height_weight()
    elif choice == 4:
        student1.display()
    else:
        print("Lỗi")