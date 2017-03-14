dim_count = (2,4,6,8,12,16,18,24,32,34)
mem_price = {'1': 3, '2': 4, '4': 6, '8': 12, '16': 60, '32': 360}

for i in mem_price:
    #print 'i =',i
    for j in dim_count:
        #print 'j =',j
        print dim_count[j], '=', dim_count[j]*mem_price[i]
        

