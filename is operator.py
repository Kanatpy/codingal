x=5
if(type(x) is int):
  print("true")
else:
  print("false")
x=20
y=20
if ( x is y):
  print("x & y same identity")
y = 30
if (x is not y):
  print("x & y different identity")