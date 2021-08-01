## 210731 스터디 (BEAKJOON, SWEA) _주말과제1-2

#### SWEA

- 문제번호: 2068. 최대수 구하기 / 2063 중간값 찾기 / 2056 연월일 달력

- 2068 최대수 구하기

  ```python
  T = int(input())
  # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
  for test_case in range(1, T + 1):
      t_case = list(map(int, input().split()))
      print(f'#{test_case} {max(t_case)}')
  ```

  - 오타로 인한 에러가 계속 발생해서 시간이 많이 소요되었음

    - 신중하게 작성할 것

    

- 2063 중간값 찾기

  ```python
  T = int(input())
  # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
  
  t_case = list(map(int, input().split()))
  t = sorted(t_case)
              
  print(t[T//2])
  ```

  - 입력 받는 부분 파악이 잘 안되어서 시간이 오래 걸렸음

  - 제시된 for구문 삭제하고 작성함 

  - sorted 사용하지 않고 정렬하는 법은 모르겠음

    

- 2056 연월일 달력

  ```python
  T = int(input())
  for test_case in range(1, T + 1):
  	t = input()
  
  	lst31 = ['01', '03', '05', '07', '08', '10', '12']
  	lst30 =  ['04', '06', '09', '11']
  
  	if 1 <= int(t[4:6]) <= 12:
          
  		if t[4:6] in lst31:
  			if 1 <= int(t[6:8]) <= 31:
  				print(f'#{test_case} {t[0:4]}/{t[4:6]}/{t[6:8]}')
  			else:
  				print('#', test_case, ' -1', sep='')
                  
  		elif t[4:6] in lst30:
  			if 1 <= int(t[6:8]) <= 30:
  				print(f'#{test_case} {t[0:4]}/{t[4:6]}/{t[6:8]}')
  			else:
  				print('#', test_case, '-1', sep='')
  		
  		elif t[4:6] == '02':
  			if 1 <= int(t[6:8]) <= 28:
  				print(f'#{test_case} {t[0:4]}/{t[4:6]}/{t[6:8]}')
  			else:
  				print('#', test_case, ' -1', sep='')
                  
  		else:
  			print('#', test_case, ' -1', sep='')
              
  	else:
  		print('#', test_case, ' -1', sep='')
  ```
  
  - identation 에러가 많이 발생하여 시간이 굉장히 지체되었음
    - 번거롭더라도 vscode에서 작성하고 옮기는 것이 나을 듯 함
  - 문자열 슬라이싱에서 인덱스 착오가 있어 에러가 많이 발생하였음
    - 연습이 필요함
  - 프린트문 작성에 착오가 많이 발생하여 시간이 많이 지체되었음

