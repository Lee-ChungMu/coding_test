#모험가 길드 문제
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
result=0 #그룹 수
cnt=0#현재 그룹에 포함된 모험가의수

for i in arr:#공포도가 낮은 것부터 하나씩 확인
    cnt+=1#현재 그룹에 해당 모험가를 포함
    if cnt >= i:#현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면 그룹결성
        result+=1#총그룹의 수 증가시키기
        cnt=0#현재그룹에 포함된 모험가의 수 초기화


print(cnt)