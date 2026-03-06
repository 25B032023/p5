#1
import re

text = open("raw.txt", encoding="utf-8").read()

prices = re.findall(r'\d{1,3}(?: \d{3})*,\d{2}', text)

for p in prices:
    print(p)

#2
import re

text = open("raw.txt", encoding="utf-8").read()

products = re.findall(r'\d+\.\s*\n(.+)', text)

for p in products:
    print(p.strip())


#3
import re

text = open("raw.txt", encoding="utf-8").read()

prices = re.findall(r'\d{1,3}(?: \d{3})*,\d{2}', text)

total = 0
for p in prices:
    p = p.replace(" ", "").replace(",", ".")
    total += float(p)

print(round(total, 2))


#4
import re

text = open("raw.txt", encoding="utf-8").read()

dt = re.search(r'\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}', text)

if dt:
    print(dt.group())

#5
import re

text = open("raw.txt", encoding="utf-8").read()

payment = re.search(r'(Банковская карта|Наличные)', text)

if payment:
    print(payment.group())

#6
import re
import json

text = open("raw.txt", encoding="utf-8").read()

products = re.findall(r'\d+\.\s*\n(.+)', text)
prices = re.findall(r'\d{1,3}(?: \d{3})*,\d{2}', text)

dt = re.search(r'(\d{2}\.\d{2}\.\d{4})\s(\d{2}:\d{2}:\d{2})', text)
payment = re.search(r'(Банковская карта|Наличные)', text)

data = {
    "products": products,
    "prices": prices,
    "date": dt.group(1) if dt else None,
    "time": dt.group(2) if dt else None,
    "payment_method": payment.group() if payment else None
}

print(json.dumps(data, ensure_ascii=False, indent=4))
