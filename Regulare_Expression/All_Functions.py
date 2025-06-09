import re

s = 'GreeksforGreeks portal> for geeks'

m = re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',"rudrapatel@gmail.com")

print(m)
if m is None:
    print("email is not valid")

else:
    print("email is valid")

match = re.search('Greeks',s)
print('for',match.start())
print(match.end()) 

a = re.split('k',s)

a = re.sub('s',"hello world",s)

a = re.findall('Greeks',s)

a = re.escape('>')

a = re.search("Greeks",s)

print(a.start(),a.end())

a = re.compile('')
print(a.findall('rudra@gmail.com'))