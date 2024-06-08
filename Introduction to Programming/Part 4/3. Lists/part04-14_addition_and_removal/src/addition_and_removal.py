# Write your solution here
nums = []

num = 1
while True:
    print("The list is now", nums)
    choice = input("a(d)d, (r)emove, or e(x)it: ")
    
    if choice == 'd':
        nums.append(num)
        num += 1
    elif choice == 'r':
        num = nums.pop()
    elif choice == 'x':
        break
print("Bye!")