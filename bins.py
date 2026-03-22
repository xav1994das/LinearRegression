def binarysearch(list, target):
    res=[]
    l=0
    r=len(list)-1
    while(l<=r):
        m=(l+r)//2
        if target==list[m]:
            res.append(m)
            if list[m-1]==target:
                i=m-1
                while(i>0 and list[i]==target):
                    res.append(i)
                    i=i-1
            elif list[m+1]==target:
                i=m+1
                while(i<r and list[i]==target):
                    res.append(i)
                    i=i+1
                break
            else:
                break
       
        elif target<list[m]:
            r=m-1
        else:
            l=m+1
    
    return res

if __name__=="__main__":
    list=[1,4,6,9,11,15,15,15,17,34,34,56]
    target=34

    pos=binarysearch(list, target)
    print(pos)
    
        