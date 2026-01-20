def sockMerchant(n, ar):
    count = 0
    a = set(ar)
    for v in a:
        count += ar.count(v)//2
    print(count)

sockMerchant(7,[1,2,1,2,1,3,2])
