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

def warmup3(number, lst):
  return bool(number > len(lst))

def warmup4(number, lst):
  lst_warmup4 = lst
  for i in range(number):
    lst_warmup4[i] = lst_warmup4[i] - 1
  return lst_warmup4

def hh(lst):
  hh_lst = lst

  while(True):
    # Eliminate 0's
    warmup1(hh_lst)
    # If sequence is empty stop and return True
    if hh_lst == []:
      return True
    # Sort the sequence in descending order
    warmup2(hh_lst)
    # Remove the first answer and give it into N
    n = hh_lst[0]
    hh_lst.pop(0)
    if warmup3(n, hh_lst):
      return False  
    # Subtract 1 from each of N
    warmup4(n, hh_lst)