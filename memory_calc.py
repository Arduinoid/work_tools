from math import sqrt

quantities = []
dimms = 64
count = 2
step = 0

while dimms >= 1:
    dimms = dimms /2
    print dimms
    step += 1
print "step", step
'''
price = input("price for 2 dimms:  ")

while price != "exit":    
    if price != "exit":

        for i in range(count,dimms):
            quantities.append(count * (price / 2))
            count *= 2

    count = 2
    print quantities
    quantities = []
    price = input("price for 2 dimms:  ")
'''
