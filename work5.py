numbers = []
fivehundreds = []
count = 0

print("5개의 세자리 정수를 입력하세요.")

while count < 5:
  num = int(input("%d번째 정수: " %(count+1)))

  numbers.append(num)

  if num // 100 == 5:
    fivehundreds.append(num)
  
  count += 1
    
print("\n===================\n")
print("입력받은 값 =", numbers)

numbers.sort()
print("정렬된 값 =", numbers)

print("500단위의 정수 개수 = {0}개".format(len(fivehundreds)))
print("500단위의 정수 합 =", sum(fivehundreds))
print("500단위의 정수 =", fivehundreds)
