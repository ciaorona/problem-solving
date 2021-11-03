# psd code
# n,m <= input
# if n%m or m%n =0
# out( multiples)
# else
# out(no multiple)


n,m = map(int,input().split())
if n%m ==0 or m%n == 0:
    print('Multiples')
else:
    print('No Multiples')