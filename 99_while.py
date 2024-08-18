start = 2
end = 9
numbers = []
while start <= end:
    numbers.append(start)
    start += 1
for i in numbers:
    for j in numbers:
        print(f"{i}*{j}={i*j}",end="\t")
    print()