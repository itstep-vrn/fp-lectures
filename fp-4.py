######################### LIST TASK EXAMPLES #########################

######################################################################
# LIST LIBRARY

def cons(x, y): return x, y
def head(l):    return l[0]
def tail(l):    return l[1]

nil = None
def isnull(l): return l is None
def l(*args): return cons(args[0], l(*args[1:])) if args else nil

def foldl(f, a, l): return a if isnull(l) else foldl(f, f(a, head(l)), tail(l))

def reverse(l): return foldl(lambda a, x: cons(x, a), nil, l)

def show(l):
  def s(x):
    try: return show(x)
    except Exception as ex: return str(x)
  r = foldl(lambda a, x: a + " " + s(x), "", l)
  return '(' + r[1:] + ')'

def map(f, l): return nil if isnull(l) else cons(f(head(l)), map(f, tail(l)))

def filter(f, l):
  if isnull(l): return nil
  elif f(head(l)): return cons(head(l), filter(f, tail(l)))
  else: return filter(f, tail(l))

def range(a, b): return nil if (a>b) else cons(a, range(a+1, b))

######################################################################
# COIN CHANGE

coins = l(1, 5, 10, 25, 50)

def cc(s, l):
  if (s==0): return 1
  elif (s<0 or isnull(l)): return 0
  else:
    c = head(l)
    r = range(0, s//c)
    v = map(lambda n: cc(s-n*c, tail(l)), r)
    return foldl(lambda a, x: a+x, 0, v)

#print("COIN CHANGE", cc(100, coins))

def ccs(s, l):
  if (s==0): return 1
  elif (s<0 or isnull(l)): return 0
  else: return ccs(s-head(l), l) + ccs(s, tail(l))

#print("COIN CHANGE", ccs(100, coins))

######################################################################
# 8 QEENS
'''
def zipWith(f, l1, l2):
  if (isnull(l1) or isnull(l2)): return nil
  else: return cons(f(head(l1), head(l2)), zipWith(f, tail(l1), tail(l2)))

chessRange = range(1, 8)

def good(j, l):
  bs = zipWith(lambda x, y: y==j or y-x==j or y+x==j, chessRange, l)
  return isnull(filter(lambda x: x, bs))

#print(good(1, l(2,8)))

def addq(l):
  gs = filter(lambda j: good(j, l), chessRange)
  return map(lambda j: cons(j, l), gs)

#print(show(addq(l(2,8))))

def ntimes(n, f, a): return a if (n<=0) else ntimes(n-1, f, f(a))

def append(l1, l2): return l2 if isnull(l1) else cons(head(l1), append(tail(l1), l2))

#print(show(append(l(1,2), l(3,4))))

def concat(l): return nil if isnull(l) else append(head(l), concat(tail(l)))

#print(show(concat(l(l(1,2), l(3,4), l(5,6)))))

queens = ntimes(8, lambda ls: concat(map(addq, ls)), l(l()))

#print(show(queens))

def count(l): return foldl(lambda a, x: a+1, 0, l)

print("COUNT OF VARIANTS", count(queens))

chessLetters = l("A", "B", "C", "D", "E", "F", "G", "H")

def posToStr(l):
  z = zipWith(lambda c, j: c+str(j), chessLetters, l)
  return foldl(lambda a, x: a + x + " ", "", z)

#print(posToStr(l(5,7,2,6,3,1,4,8)))

queensStr = foldl(lambda a, x: a + posToStr(x) + "\n", "", queens)
print(queensStr)
'''