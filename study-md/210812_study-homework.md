# 210812 study _ homework 코드 정리

- SWEA 1989. 초심자의 회문검사

  ```python
  import sys
  sys.stdin = open("input1989.txt", "r")
  
  T = int(input())
  
  for tc in range(1, T+1):
      wrd = input()
      # print(wrd)
      result = '1'
      for w in range(len(wrd)//2):
          if wrd[w] != wrd[-w-1]:
              result = '0'
  
      print('{} {}'.format(tc, result))
  ```

  - 사소한 실수로 코드 작성이 오래 걸렸음(if문)

- SWEA 1984. 중간 평균값 구하기

  ```python
  import sys
  sys.stdin = open("input1984.txt", "r")
  
  T = int(input())
  
  for tc in range(1, T+1):
  
      nums = list(map(int, input().split()))
      # print(T, tc, nums)
  
      maxV = nums[0]
      minV = nums[0]
  
      for n in nums:
  
          if n > maxV:
              maxV = n
  
          if minV > n:
              minV = n
  
      # print(maxV, minV)
  
      new_nums = []
      for n in nums:
          if n != maxV and n != minV: #이부분이 이해가 잘 안됨...단축평가때문에 영향을 주는 것 같음
                                      # or로 작성하면 오답임  # elif로 조건 따로 적어도 오답임
              new_nums.append(n)
          
      # print(new_nums)
  
  
      sumV = 0
      avgV = 0
      for n in new_nums:
          sumV += n
      avgV = round(sumV / len(new_nums))
  
      print('#{} {}'.format(tc, avgV))
  
  ```

  - 기존 리스트에서 maxV, minV를 삭제하고 새로운 리스트를 반환하는 부분에서 시간이 많이 소요되었음
    - idx값을 반환하여 pop으로 제거하니 제대로 된 답이 나오지 않았음
    - if문으로 maxV, minV를 제외한 값만 추가하는 리스트를 작성할 때에도, or로 작성했더니 제대로 된 답이 나오지 않았음
      - 아직 왜 and인지 정확히 모르겠음
      - elif문으로 조건을 따로 작성해도 오답이 나오는데 왜 오답인지 정확히 모르겠음
  - 반올림 하는 부분에서도 오답이 나왔음(몫을 반환했더니 짝수,홀수 반올림 기준이 달라 오답이 나왔음)