#for loop can be infinite if the value is appended in the same iterator
seq2 = []
seq = [1,2,3,4,5]

for no in seq:
    no += 100

    if no > 3:
        no += 30
        seq2.append(no)
    elif no == 2:
        print(no, "received value = 2")
    elif no ==3:
        print(no, "received value = 3")
    else:
        print(no, 'none condition is getting passed')

print(seq2)