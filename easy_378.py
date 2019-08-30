# Challenge 378 Easy
# The Havel-Hakimi algorithm for graph realization

def warmup1(lst):
  # Warmup 1: eliminating 0's
  lst_warmup1 = lst  
  zero_count = lst.count(0)
  for i in range(zero_count):
      lst_warmup1.remove(0)

  return lst_warmup1

def warmup2(lst):
  #lst_warmup2 = warmup1(lst)
  lst_warmup2 = lst
  lst_warmup2.sort(reverse=True)
  return lst_warmup2
