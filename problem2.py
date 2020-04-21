fibonacci =[]
even_fibbonacci = []
a = 1
b = 2

fibonacci.append(a)
fibonacci.append(b)
even_fibbonacci.append(b)

#Added a comment here to check some Magit features

for jj in range(100)[2:]:

    fibonacci.append(fibonacci[jj-1]+fibonacci[jj-2])
    if fibonacci[jj]%2==0:
        even_fibbonacci.append(fibonacci[jj])
    if fibonacci[jj] > 4000000:
        print "fibbonacci number exceeded 4000000 at index number {}".format(jj)
        break


print even_fibbonacci
print "sum of een fibbonacci numbers = {}".format(sum(even_fibbonacci))    

#while fibbonacci <= 4000000:
    
