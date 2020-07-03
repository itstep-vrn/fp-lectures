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