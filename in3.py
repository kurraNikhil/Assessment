l = ["X", 20, "Y", 10, "Z", 30]
cnt = 0
st =" "
inc = 0
for c in range(1, 6, 2):
  cnt = cnt + c
  st = st + l[c-1]+"@"
  inc = inc + l[c]
  
  print(cnt, st, inc)

    