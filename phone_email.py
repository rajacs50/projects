import pyperclip
import re

pn = re.compile(r'\d{3}.\d{3}.\d{4}')
# Enclosed the entire compile in parans because findall method only returns a matching group
ea = re.compile(r'([a-zA-Z0-9.]+@[a-zA-Z0-9]+\.(com))')

text = str(pyperclip.paste())

matches = []

for pnum in pn.findall(text):
    matches.append(pnum)

for mail in ea.finditer(text):
    matches.append(mail[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')