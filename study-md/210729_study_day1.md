## 210729 스터디 (BEAKJOON, SWEA) _day1

#### BEAKJOON

###### 문제 > 단계별 > 1. 입출력과 사칙연산 : 완료

- 문제 번호 : 2257, 10718, 10171, 10172, 1000, 1001, 10998, 1008, 10869, 10430, 2588

- 2588번 : 곱셈문제

  ![image-20210730000148754](C:/Users/moon/AppData/Roaming/Typora/typora-user-images/image-20210730000148754.png)

  ```python
  A = int(input())
  B = int(input())
  
  print(A * (B % 10))
  print(A * (B % 100 // 10))
  print(A * (B % 1000 // 100))
  print(A * B)
  ```

  - 다른방법: 문자열 인덱싱 통해서 작성하는 방법이 더 간단하고 효율적으로 보임

    

#### SWEA

- 문제 번호 : 2047. 신문헤드라인 / 2058. 자릿수 더하기 / 1936. 1:1 가위바위보

- 2058 자릿수더하기

  ```python
  #최초작성
  #4자릿수만 가능하므로 적절한 코드가 아님 
  #테스트케이스로 1~3자리 숫자가 오는 경우 인덱스 에러 발생 예상
  n = input()
  
  print(int(n[0]) + int(n[1]) + int(n[2]) + int(n[3]))
  
  #재작성
  n = input()
   
  sumV = 0
  for i in n:
      sumV += int(i)
  print(sumV)
  ```

  - 다른 방법 : 입력받은 문자열을 리스트로 변환하여, 변환된 리스트를 map함수를 사용하여 정수형 숫자대로 나누어 반환하고(`list(map(int, number)`)  해당 리스트 내부의 값을 sum함수로 합산하여 구할 수도 있음
    - extend함수로도 구할 수 있지 않을까? 
      - iterable인 문자열을 나눠서 입력하므로 리스트 내부의 값을 sum함수로 합계를 구할 수 없음
        - 어차피 반복문을 사용해야해서 크게 효율적이지는 않은 것으로 보임

- 1936 1:1 가위바위보

  ```python
  a, b = map(int, input().split())
  
  if a == 1: 
  	if b == 2:
  		print('B')
  	elif b == 3:
  		print('A')
  elif a == 2:
  	if b == 1:
  		print('B')
  	elif b == 3:
  		print('A')
  elif a == 3:
  	if b == 1:
  		print('B')
  	elif b == 2:
  		print('A')
  ```

  - 다른 방법 :  A가 이기는 경우 / B가 이기는 경우, 두 가지 경우로 나누어서 각각의 해당하는 비교식을 and, or 논리 연산자를 통해 조건문을 작성해서 결과값을 출력할 수 있음

  - 다른 방법 2 : A가 이기는 경우 / B가 이기는 경우, 두 가지 경우의 숫자 대소비교를 통해 결과값을 출력할 수 있음

  - ''가위  = 1, 바위 = 2, 보 = 3'인데 숫자가 헷갈린다면 해당 숫자를 변수에 대입해서도 비교하는 것이 보기 편할 수도 있음

    ```python
    scissors = 1
    rock = 2
    paper = 3
    ```

    