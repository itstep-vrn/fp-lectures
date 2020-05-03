############################ FINITE LISTS ############################

######################################################################
# CONS / HEAD / TAIL

# 1-st variant
def cons(x, y): return x, y
def head(l):    return l[0]
def tail(l):    return l[1]
'''
# 2-nd variant
class ConsList:
  def __init__(self, x, y): self.head, self.tail = x, y

def cons(x, y): return ConsList(x, y)
def head(l):    return l.head
def tail(l):    return l.tail

# 3-rd variant
def cons(x, y): return lambda f: f(x, y)
def head(l):    return l(lambda x, y: x)
def tail(l):    return l(lambda x, y: y)

# 4-th variant
def cons(x, y): return lambda c: x if (c == 0) else y
def head(l):    return l(0)
def tail(l):    return l(1)
'''

######################################################################
# SERVICE FUNCTIONS & HELPERS

nil = None

def isnull(l): return l is None

def l(*args): return cons(args[0], l(*args[1:])) if args else nil

######################################################################
# STANDARD LIBRARY LIST FUNCTIONS - MAP, FILTER, REDUCE

def foldl(f, a, l): return a if isnull(l) else foldl(f, f(a, head(l)), tail(l))

def reverse(l): return foldl(lambda a, x: cons(x, a), nil, l)

def show(l):
  def s(x):
    try:
      return show(x)
    except Exception as ex:
      return str(x)
  r = foldl(lambda a, x: a + " " + s(x), "", l)
  return '(' + r[1:] + ')'

#a = l()
#a = l(1)
#a = l(1, 2)
#a = l(1, l(2, 3), l(4, l(5, 6, l(7), 8), 9), 10)
#print("RAW        ", a)
#print("SHOW       ", show(a))

def map(f, l): return nil if isnull(l) else cons(f(head(l)), map(f, tail(l)))

def filter(f, l):
  if isnull(l):
    return nil
  elif f(head(l)):
    return cons(head(l), filter(f, tail(l)))
  else:
    return filter(f, tail(l))

def range(a, b): return nil if (a>b) else cons(a, range(a+1, b))

#a = range(1, 5)
#print("RAW        ", a)
#print("SHOW       ", show(a))
#print("MAP (*10)  ", show(map(lambda x: x*10, a)))
#print("FILTER EVEN", show(filter(lambda x: x%2 == 0, a)))
#print("REVERSE    ", show(reverse(a)))
#print("LEFT FOLD  ", foldl(lambda a, x: str(x) + '-' + a, '>', a))
#print("SUM        ", foldl(lambda a, x: a + x, 0, a))
