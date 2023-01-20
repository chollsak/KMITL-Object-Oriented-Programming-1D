def count_minus(str):  
  
  str = [int(digit) for digit in str.split()]
  result_list = [digit for digit in str if digit < 0]
  return (len(result_list))