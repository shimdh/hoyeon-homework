input_temp = int(input("현재 기온을 입력해주세요: "))

if input_temp <= 10:
  print("날씨가 춥습니다.")
  print("두꺼운 외투를 챙기세요.")
elif input_temp <= 15:
  print("날씨가 신선하네요.")
  print("가벼운 외투를 챙기세요.")
elif input_temp <= 19:
  print("생활하기 좋은 기온입니다.")
  print("가볍게 입으세요.")
else:
  print("덥게 느껴지는 날씨입니다.")
  print("반팔티도 괜찮습니다.")
