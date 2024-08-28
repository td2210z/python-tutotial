from math import *




if __name__ == '__main__':
    #a = [1 , 2 ,3 ,"python" , 5]
    #print(len(a)) # in ra độ dài của list
    # truy cập chỉ số
    #print(a[1])
    # duyệt list





    # for i in range(0 , len(a)):
    #     print(a[i] , end= '')
    # print()
    # for i in range(len(a) -1 , -1 , -1):
    #     print(a[i] , end = ' ')
    # print() # duyệt foreach
    # for item in a:
    #     print(item)


    # thay đổi chỉ số::
    # a[2] = 'thang ngueyn'
    # print(a)


    # thêm phần tử vào list

    # a.append(10)
    # print(a)
    # a.append('thang ngueyn')
    # print(a)

    # # chèn phàn tử
    # a.insert(2 , 100) 

    # # xóa 1 phần tử thông qua giá trị 
    # a.pop()

    # xóa giá trị 


    # a = [0] * 20
    # print(a)


    #copylist
    # a = [1 , 2 ,3 , 4, 5, 6]
    # b = a.copy()
    # b[0] = 123
    # print(a)
    # print(b)

    # a = [1 , 2 ,3 , 4, 5, 6]
    # b = a[::-1]
    # print(b)

    # a = [1 , 2 ,3 , 4, 5, 6]
    # a[2 : 5] = [100 , 200 , 1100]
    # print(a)
    


    # HẦM LAMDA
    
    # t = lambda x : x *2
    # n = int(input())
    # print(t(n))

    #xe
    a = [1 , 2 ,3 , 4, 5]
    b = [x + 3 for x in a]
    print(b)
    