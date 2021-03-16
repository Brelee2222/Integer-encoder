def encrint(integer):
  integer_ = hex(int(integer))
  integer = []
  for i in range((len(integer_)-2+(2*(len(integer_) % 2))) // 2):
      print(i)
      try:
        integer.append(int('0x' + integer_[len(integer_)-(2*(i))-2] + integer_[len(integer_)-(2*(i))-1], 0))
      except: 
          integer.append(int('0x' + integer_[2], 0))
          print('0x' + integer_[2])
  integers = []
  for i in range(len(integer)):
    integers.append(integer[len(integer)-i-1])
  integer = integers
  integers = []
  for i in integer:
    integers.append(chr(i))
  integer = ''.join([str(t) for t in integers])
  return integer
def decrint(string):
  value = '0x'
  for i in range(len(string)):
      value = value + str(hex(ord(string[i]))).replace('0x', '')
  value = int(value, 0)
  return value