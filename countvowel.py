
vowels=['a','e','i','o','u']
ad=input("Enter the string: ")
count=0
for i in ad:
    if i in vowels:
        count+=1
print("Number of vowels in the string:", count)


