import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4242. 415-555-4243')
print(mo.groups())
print('Phone number found: ' + mo.group(0))