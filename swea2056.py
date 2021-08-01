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