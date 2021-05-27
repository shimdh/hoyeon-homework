sum_odd = 0
sum_even = 0

print("10개의 정수를 입력하세요.")

for count in range(1, 11):
  num = int(input("%d번째 정수: " %(count)))
  
  if num % 2 == 0:
    sum_even += num
  else:
    sum_odd += num
    
print("\n===================\n")

print("홀수의 총합: {0}".format(sum_odd))
print("짝수의 총합: {0}".format(sum_even))