# 1. CÁC KIẾN THỨC CƠ BẢN

![alt text](https://logos-world.net/wp-content/uploads/2021/10/Python-Symbol.png)





- [1. CÁC KIẾN THỨC CƠ BẢN](#1-các-kiến-thức-cơ-bản)
  - [1.1. Sytax và chú thích](#11-sytax-và-chú-thích)
    - [1.1.1. Sytax:](#111-sytax)
    - [1.1.2. Comment](#112-comment)
    - [1.1.3. câu lệnh print()](#113-câu-lệnh-print)
        - [1.1.3.0.1. printf(obj , sep = seprttor (phân cách giữ các đồi tượng), end = end)](#11301-printfobj--sep--seprttor-phân-cách-giữ-các-đồi-tượng-end--end)
  - [1.2. Kiểu dữ liêu  \&\& Toán tử](#12-kiểu-dữ-liêu---toán-tử)
    - [1.2.1. LT](#121-lt)
    - [](#)
  - [1.3. Cấu Trúc Rẽ Nhánh](#13-cấu-trúc-rẽ-nhánh)
  - [1.4. Vòng Lặp](#14-vòng-lặp)
  - [1.5. HÀM](#15-hàm)



## 1.1. Sytax và chú thích
### 1.1.1. Sytax:
Các câu lệnh trong python không có kết thúc bằng dấu chấm phẩy , và sử dụng thụt lề để chỉ ra khối lệnh mới
### 1.1.2. Comment 
Sử dụng dấu # để chú thích 1 dòng , vd #print('hello')
Sử dụng dấu ''' ''' để cmt nhiều dòng

### 1.1.3. câu lệnh print()

##### 1.1.3.0.1. printf(obj , sep = seprttor (phân cách giữ các đồi tượng), end = end)
Trong Đó:
obj : là các đối tượng
tham số sep = nếu không có mặc định sẽ là khoảng trắng , cp : sep = "#"
tham số end = nếu không có mặc định sẽ là xuống dòng  end = '!\n' **

VD : print("hello word)

## 1.2. Kiểu dữ liêu  && Toán tử

### 1.2.1. LT
Biến là vùng chứa dữ liệu phục vụ bài toán

Trong python các bạn không cần phải khai báo biến, biến sẽ được tạo và xác định kiểu tự động(dynamic typing) khi bạn gán giá trị cho nó

Để biết kiểu dữ liệu của một biến bạn có thể sử dụng hàm **type()**
vd:
a = int(intput())
print(type(a)) 

==> màn hình console sẽ hiện ra là  class < int>
**CHÚ Ý**
-- tên biến python phân biệt in hoa in thường , không được đặt tên biến có chứa đáu cách , kí tự đặc biệt , kí hiệu bằng số


###
KIỂU DỮ LIỆU

Kiểu dữ liệu số: Trong Python có 3 kiểu dữ liệu số: Số
nguyên (Integer), Số thực dấu phẩy động (Floatingpoint numbers) và Số phức (Complex numbers)

a = 14 (kiểu số nguyên)
b = 15.3 (kiểu số thực)
c = 5 + 3 (kiểu số phức)

**SỐ NGUYÊN**
Trong python thì các số nguyên thường được in ra dưới dạng cơ sô 10 nhưng bạn cũng có thể in ra các số ở hệ 2 , 16 , 8

|Tiền Tố(prefix)|Ý Nghĩa| Cơ Số|
|---------------|-------|------|
|'0b' Hoặc '0B'| Hệ nhị phân| 2|
|'0o' hoặc '0O'| Hệ bát phân|8|
|'0x' Hoặc '0X'| Hệ 16| 16|


**Kiểu Đúng Sai**
kiểu bool sẽ lưu 2 giá trị là true hoặc false
**Kiểu Xâu Kí Tự**
Xâu kí tự trong py đc đặt trong nháy đơn hoặc nháy kép trên 1 dòng trong th xâu có nhiều dòng ta đặt giữa 3 nháy kép


**Ép Kiểu**
vd: a = int(12.44)


**Toán Tử**
*Toán Tử Gán* 
a = b : gán giá trị của b cho a
*Toán tử toán học*
Gồm: + , - , * , / , //(chia nguyên) , %(chia dư) , **(lũy thừa)

*Toán tử so sánh*
== , >  , <= , <  , !=
*Toán Tử Logic*
1. toán tử **and** (toán tử và) 1 trong 2 số là 0 , sẽ trả về 0 , hoặc 1 trong 2 đk đều bằng 0 sẽ trả về 0
2. toán tử **or** (toán tử hoặc) 1 trong 2 giá trị đúng sẽ trả về đúng
3. toán tử **not** (toán tử phủ định)

*Toán Tử Nhận Dạng*
1. **is** : trả về true nếu 2 đối tượng giống nhau
2. **is not** : Trả  về True nếu 2 đối tượng là khác nhau

## 1.3. Cấu Trúc Rẽ Nhánh
**if**
cú pháp : if condition: #code
If đc sử dụng khi bạn cần kiểm tra điều kiện nào đó trc khi thực hiện một hoặc nhiều câu lệnh. **các câu lệnh bên trong if đc thụt lề so với
 if**

**else**
Được sử dụng trong th condition bên trong if là sai 

**elif**
Được sử dụng bên dưới if để kiểm tra thêm điều kiện bổ sung nếu điều kiện bên trên sai 

**shorthand if và toán tử ba ngôi**
vd:
a , b=100 , 200
if a < b: print(a , 'be hon' , b)

a , b = 100 , 200
res = 'a lon hon b' if a < b else 'a nho hon b'


## 1.4. Vòng Lặp

**For**
1. Thay vì duyệt qua các giá trị số thì Py sẽ lặp qua các iterable(list , tuple , string , set) , thứ tự duyệt sẽ theo thứ tự xuất hiện trong iterable , để thực hiện vòng lặp for ta sử dụng  built-in fuction là range()
2. Cấu trúc :
--range(start , stop , step)
Các tham số : start là bắt đầu , stop , giá trị cuối cùng trong dãy (cận này sẽ không đc lấy) , step là bước nhảy (mặc định sẽ là 1)
vd for i in range(5): print("hê lô")

**for lồng nhau**
xuất hiện khi một câu lệnh trong vòng for này lại là 1 vòng for khác 
Cách chạy của 2 vòng for : mỗi vòng for bên ngoài thì toàn bộ vòng for bên trong sẽ đc thực thi 


**Câu lệnh break**
đc sử dụng để kết thúc vòng for ngay lập tức , vòng lặp for sẽ kết thúc ngay tại thời điểm  gặp câu lệnh break và tiếp tục các câu lệnh dưới vòng for. Thông thường break đi kèm vs câu lênh đk

**Câu lệnh continue**
đùng để bỏ qua lần lặp hiện tại và trở lại luôn vòng lặp tiếp theo . Các câu lệnh bên dưới continue sẽ đc bỏ qua


**While**

đc sử dụng khi bạn muôn thực hiện 1 tác vụ vô hạn thời gian , cho đến khi 1 dk cụ thể đc đáp ứng . Đây là một vòng lặp đc kiểm soát theo điều kiện và thường sử dụng khi chưa biết trc số lượng vòng lặp

Vòng Lặp Vĩnh Viện:
While True: 

## 1.5. HÀM

1. Hàm giúp các ltv có thế sử dụng lại code của mình (code reuse) , chúng cho phép bạn định nghĩa một khối lệnh và có thể thực hiện đi lại nhiều lần 
2. PY  cũng cung cấp các hàm có sẵn (built-in fuction) như print() , max().. Giờ đây bạn có thể tụ xây dụng hàm riêng
3. Để xây dựng hàm ta sử dụng từ khóa **def** , trc khi xây dựng  cần xác định các tham số (gt mà bạn truyền cho hàm) , câu lệnh return nếu mong muốn hàm trả về gt
4. Hàm chỉ đc chạy khi nó đc gọi


**keyword argument**
khi thực hiện hàm thì thứ tự của đối số bạn truyển cho hàm rất là quan trọng

**defaut**
bạn có thể chỉ định các giá trị mặc định cho các đối số khi xây dựng 1 hàm

## LIST


