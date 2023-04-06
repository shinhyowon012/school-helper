c =  ['국어','수학','영어','사회','과학']
a = [0,1,2,3,4,5]
v = 0
b = 100
for i in range(0,5):
    a[i] = input(""+c[i]+"에 성적을 알려주세요 ")
    w = int(a[i])
    if w > v:
        v =w
    if w < b:
        b = w



sum = 0
for i in range(0,5):
    sum = sum + int(a[i])
sum = sum/5
print("평균은"+str(sum))
print("가장 큰 점수의 과목은")
print (v)
print("가장 부족한 점수의 과목은")
print (b)
print("그러므로 "+v+"는 조금 덜하고 "+b+"이 과목을 중점적으로 하십시오")