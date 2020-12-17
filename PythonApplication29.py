print("지금부터 두 개의 양의 정수를 입력할 겁니다. \n\"?부터 $까지 더할 거야\"")
a=int(input("?에 들어갈 양의 정수를 입력하세요. "))
b=int(input("$에 들어갈 양의 정수를 입력하세요. "))
result=0
i=a

for x in range(a, b+1):
    result+=i
    i+=1
print("당신은 \"{}부터 {}까지 더할 거야\"라고 이야기했고 그 결과는 {}입니다. " .format(a, b, result))