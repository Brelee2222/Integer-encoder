def encrint(integer):
  integer_ = hex(int(integer))
  integer = []
  for i in range(len(integer_)):
    if len(integer_) >= 2*(i+1)+1:
      try:
        print(integer_[2*(i+1)], integer_[2*(i+1)+1])
        integer.append('0x' + integer_[2*(i+1)] + integer_[2*(i+1)+1])
      except: 
          integer.append('0x' + '0' + integer_[2*(i+1)])
  integers = []
  for i in integer:
    i = int(i, 0)
    integers.append(chr(i))
  integer = ''.join([str(t) for t in integers])
  return integer
def decrint(string):
  value = '0x'
  for i in range(len(string)):
      value = value + str(hex(ord(string[i]))).replace('0x', '')
  value = int(value, 0)
  return value