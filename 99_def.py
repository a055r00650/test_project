#產生範圍內數字
def generate_numbers(start, end):
    if start > end: 
        return [] #if 成立回傳 空list
    return [start] + generate_numbers(start + 1, end)

numbers = generate_numbers(2, 9)
print(f"numbers = {numbers}")
for i in numbers:
    for j in numbers:
        print(f"{i}*{j}={i*j}", end="\t")
    print()