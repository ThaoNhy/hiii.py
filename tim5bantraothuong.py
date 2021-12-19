# tạo list
sinhvien, diemrenluyen, diemquatrinh, diemTong = [], [], [], [] 

mon = ["Toán cao cấp", "Giới thiệu ngành", "Tư duy lập trình "," Kinh tế vi mô", " Tư tưởng HCM"] 

tinchi = [3, 2, 3, 3, 2]


def _input():
    # Tên sinh viên
    sinhvien.append(str(input("Tên sinh viên: ")))

    # Điểm từng môn
    arr_scores = [] 
    for i in range(0, len(mon)):
        arr_scores.append(float(input(f'Nhập điểm môn {mon[i]}: ')))
    
    diemquatrinh.append(arr_scores)
    
    # Điểm rèn luyện
    drl = float(input(f'Điểm rèn luyên: '))
    diemrenluyen.append(drl)
    diemTong.append(tinhDiemTB(arr_scores, tinchi, drl))
    
    
def tinhDiemTB(diemQT, tinchi, drl):
    res = 0
    for i in range(0, len(mon)):
        res += diemQT[i] * tinchi[i]   
        
    # Tổng tín chỉ
    tongTC = 0
    for value in tinchi:
         tongTC += value
    return (res / tongTC) + (drl * 0.2)
    
    
def findMax(diem_tong, arr_except):
    max = -1
    idx = 0
    
    for i in range(0, len(diem_tong)):
        if max < diem_tong[i] and i not in arr_except:
            max = diem_tong[i]
            idx = i
            
    return idx
     
if __name__ == '__main__':
    n = int(input('Nhập vào số lượng sinh viên: '))
    for i in range(0, n):
        _input()
        print('\n')
    
    arr_idx_sv = []
    
    for i in range(0, n):
        idx = findMax(diemTong, arr_except=arr_idx_sv)
        arr_idx_sv.append(idx)
    
    
    # Xuất danh sách sinh viên và điểm tổng kết tương ứng:
    for i in range(0, n):
        print(f"{sinhvien[i]}: {diemTong[i]}\n")
  
    # Xuất ra danh sách diểm sinh viên từ cao đến thấp -> 5 người đầu là 5 người cần tìm 
    _i = 1
    for i in arr_idx_sv:
        print(f"Sinh viên thứ {_i}: {sinhvien[i]}")
        _i += 1
        