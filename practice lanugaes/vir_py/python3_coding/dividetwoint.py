def devidint(div,dir):
    print(div//dir    )
    print(div/dir)
    return (int(str(div/dir).split('.')[0]))

div = 7
dir = -3

div=-2147483648
dir=-1

print(devidint(div,dir))
