# Write your solution here
nums = []

while True:
    num = int(input("New item: "))
    
    if num == 0:
        break
    else:
        nums.append(num)
    
    print("The list now:", nums)
    print("The list in order:", sorted(nums))
print("Bye!")