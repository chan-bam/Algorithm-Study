## 210731 스터디 (BEAKJOON, SWEA) _주말과제1-1

#### SWEA

- 문제번호: 2072. 홀수만 더하기 / 2071. 평균값 구하기 / 2070. 큰 놈 작은 놈 같은 놈

- 2072 홀수만 더하기

  ```python
  T = int(input())
  # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
  
  for test_case in range(1, T + 1):
      t_case = list(map(int, input().split()))
      sum_odd = 0
      for t in t_case:
      	if t % 2:
              sum_odd += t
      print(f'#{test_case} {sum_odd}')
  ```

  - 테스트케이스를 입력 받는 부분이 반복문의 어느 부분에 들어가야 적절히 실행되는지 판단하는 것이 어려웠음

    

- 2071 평균값 구하기

  ```python
  T = int(input())
  # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
  for test_case in range(1, T + 1):
      t_case = list(map(int, input().split()))
      totalV = 0
      for t in t_case:
          totalV += t
      print(f'#{test_case} {int(round(totalV / len(t_case), 0))}')
  ```

  - 결과값의 자료형과 동일하게 나오도록 처리하는 부분에서 약간 주의가 필요했음
  - 반올림 함수의 사용법은 엑셀과 동일함

- 2070 큰 놈, 작은 놈, 같은 놈

  ```python
  T = int(input())
  # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
  for test_case in range(1, T + 1):
      t_case = list(map(int, input().split()))
      if t_case[0] == t_case[1]:
          print(f'#{test_case} =')
      elif t_case[0] < t_case[1]:
          print(f'#{test_case} <')
      else:
          print(f'#{test_case} >')
  ```

  - 더 간단한 방법은 없을까 궁금함

