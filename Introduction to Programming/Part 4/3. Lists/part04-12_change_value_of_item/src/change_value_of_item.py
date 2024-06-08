# Write your solution here
nums = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    
    if index == -1:
        break
    
    nums[index] = int(input("New value: "))
    print(nums)
