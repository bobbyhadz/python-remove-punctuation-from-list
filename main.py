# Remove punctuation from a List of strings in Python

import string

a_list = ['b.o.b.by', 'h,adz', '', 'c:om']

new_list = [''.join(char for char in item
                    if char not in string.punctuation)
            for item in a_list]

print(new_list)  # 👉️ ['bobby', 'hadz', '', 'com']