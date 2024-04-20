"""
Programming exercise:
Name and address

Please write a program which asks for the user's name and address.
The program should also print out the given information, as follows:

Sample output:
Given name: Steve
Family name: Sanders
Street address: 91 Station Road
City and postal code: London EC05 6AW
Steve Sanders
91 Station Road
London EC05 6AW
"""
# Write your solution here
given_name = input("Given name: ")
family_name = input("Family name: ")
st_address = input("Street address: ")
city_postal_code = input("City and postal code: ")
print(given_name + " " + family_name)
print(st_address)
print(city_postal_code)