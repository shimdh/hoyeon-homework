sum = 0
count = 0

print("10개의 정수를 입력하세요.")

while count < 10:
  num = int(input("%d번째 정수: " %(count+1)))
  
  if num % 3 == 0:
    sum += num
  
  count += 1
    
print("\n===================\n")

print("3의 배수의 총합: {0}".format(sum))
