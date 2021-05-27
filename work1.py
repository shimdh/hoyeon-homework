input_number = int(input("숫자를 입력하세요: "))

if input_number % 2 == 0:
  print("{}은 2의 배수입니다.".format(input_number))
else:
  print("{}은 2의 배수가 아닙니다.".format(input_number))

if input_number % 3 == 0:
  print("{}은 3의 배수입니다.".format(input_number))
else:
  print("{}은 3의 배수가 아닙니다.".format(input_number))
  
if input_number % 5 == 0:
  print("{}은 5의 배수입니다.".format(input_number))
else:
  print("{}은 5의 배수가 아닙니다.".format(input_number))