import re

text1 = "Hello beautiful ... World"
text2 = "Hello beautiful ... Dietzenbach"

# regex = "Hello(.*)World"
regex = "([a-zA-Z]+)(\s)([a-zA-Z]+)(\s)([.]+)(\s)([a-zA-Z]+)"
matchobj = re.match(regex, text2)

print(type(matchobj), matchobj)

matchobj = re.match(regex, text1)
print(type(matchobj), matchobj)

print(matchobj.groups())

pattobj = re.compile(regex)
type(matchobj), type(pattobj)

matchobj = pattobj.match(text1)
print(matchobj.groups())

results = re.findall(regex, text1)
print(results, type(results))
