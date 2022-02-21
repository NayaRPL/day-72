print("mengecek indeks")
def sequentialsearch(alist, value):  
    pos=0
    found=False
    while pos < (len(alist))and not found :
        if alist[pos]== value:
            found=True
        else:
            pos+=1
    if found : 
        return pos 
    else :
        return -1
data=[1,7,8,3,5]
nilai=sequentialsearch(data,5)
print(nilai)
        
    