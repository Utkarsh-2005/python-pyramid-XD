a=''
b=" "
x=int(input('write the length of pyramid:- '))
y=x-1
for j in range(1,x*2,2):
    b=b*y
    y-=1
    a=j*'*'
    print(b+a)
    b=' '
     
