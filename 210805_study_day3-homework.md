## 210805 스터디 day3 - homework

#### SWEA

###### 문제번호 2027 / 1933 / 2019 / 1545 (difficult 1)

- 2027 대각선 출력하기

  ```python
  i = 0
  while i < 5:
      j = 0
      while j < 5:
          if i == j:
              print("#", end='')
          else:
              print("+", end='')
          j += 1
      print()
      i += 1
  ```

  - print문 end옵션과 줄바꿈에 주의

  

- 1933 간단한 N의 약수

  ```python
  N = int(input())
  
  for n in range(1, N+1):
      if N % n == 0:
          print(n, end = ' ')
  ```

  

- 2019 더블더블

  ```python
  N = int(input())
  num = 1
  print(1, end = ' ')
  for n in range(1, N + 1):
      num *= 2
      print(num, end = ' ')
  ```

  - 1부터 출력해야함에 유의

    - 문제 꼼꼼히 볼 것

      

- 1545 거꾸로 출력해 보아요

  ```python
  N = int(input())
  
  while N >= 0:
      print(N, end = ' ')
      N -= 1
  ```

  

