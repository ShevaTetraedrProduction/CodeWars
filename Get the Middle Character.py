def middle_c(s):
  z = (len(s) + 1)  % 2  # if 1 - pair, else odd
  m = len(s) // 2
  print (s[m - z : m + 1])

middle_c('test')
middle_c('testing')
middle_c('a')


'''
'test'(4)  [1:3]
'testing'(7)  [3:4] 
'A'  []
'''