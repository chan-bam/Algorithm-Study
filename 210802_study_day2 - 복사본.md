## 210802 스터디 (BEAKJOON, SWEA) _day2

#### BEAKJOON

###### 문제 > 단계별 > 1. if문 : 완료

- 문제 번호 : 1330, 9498, 2753, 14681, 2884

- 2753 윤년

  ```python
  year = int(input())
  
  if year % 4 == 0 and year % 100 != 0:
      print(1)
  elif year % 4 == 0 and year % 400 == 0:
      print(1)
  else:
      print(0)
  ```

- 2884 알람 시계

  ```python
  h, m = map(int, input().split())
  
  if m - 45 < 0:
      if h >= 1:
          h -= 1
          m = 60 + m - 45 # + 15로 해도 됨
          print(h, m)
      else:
          h = 23
          m = 60 + m - 45 # + 15로 해도 됨
          print(h, m)
  else:
      m = m - 45
      print(h, m)
  ```

---------------------

#### SWEA

- 문제 번호 : 2047. 아주 간단한 계산기

------------------

#### 프로그래머스

- 위클리챌린지 1주차

  - 부족한 금액 계산하기

    ```markdown
    새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
    놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
    단, 금액이 부족하지 않으면 0을 return 하세요.
    ```

    ```python
    def solution(price, money, count):
        total = 0
        
        for c in range(1, count+1):
            moneyX = price * c
            total += moneyX 
    
        if money < total:
            return total - money
    
        return 0
    
    # print(solution(3, 20, 4))
    ```

    