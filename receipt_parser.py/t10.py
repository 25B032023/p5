#1
import re

s = input()

if re.fullmatch(r"ab*", s):
    print("Match")
else:
    print("No match")

#2
import re

s = input()

if re.fullmatch(r"ab{2,3}", s):
    print("Match")
else:
    print("No match")

#3
import re

s = input()

r = re.findall(r"[a-z]+_[a-z]+", s)

for i in r:
    print(i)

#4
import re

s = input()

r = re.findall(r"[A-Z][a-z]+", s)

for i in r:
    print(i)

#5
import re

s = input()

if re.fullmatch(r"a.*b", s):
    print("Match")
else:
    print("No match")

#6
import re

s = input()

result = re.sub(r"[ ,.]", ":", s)

print(result)

#7
s = input()

parts = s.split("_")

result = parts[0]

for word in parts[1:]:
    result += word.capitalize()

print(result)

#8
import re

s = input()

result = re.split(r'(?=[A-Z])', s)

for i in result:
    print(i)

#9
import re

s = input()

result = re.sub(r'(?=[A-Z])', ' ', s).strip()

print(result)

#10
import re

s = input()

result = re.sub(r'([A-Z])', r'_\1', s).lower().lstrip('_')

print(result)
