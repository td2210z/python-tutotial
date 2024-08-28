


from math import *




if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    cnt = 0
    min_vla =  min(a) 
    
    for x in a:
        if x == min_vla:
            cnt += 1
        print(cnt)
            
    
        

    
    
    
    

    