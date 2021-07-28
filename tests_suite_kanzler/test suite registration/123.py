import random
import string
word = ''
for i in range(1,246):
  word+='в'
  i+=1
def random_char(char_num):
  return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
print(random_char(246)+"@gmail.com")