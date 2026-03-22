def sqNo():
    i=0
    while True:
        yield i*i
        i +=1

if __name__=="__main__":
    for s in sqNo():
        if s>10:
            break
        print(s)
