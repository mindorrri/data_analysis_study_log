import numpy as np

#index
array1 = np.arange(start = 1, stop = 10)
print('array1:', array1)

value = array1[1] #index는 0부터 시작작
print('value:', value)
print(type(value))

print("맨 뒤의 값:",array1[-1])
print("맨 뒤에서 두번째 값:", array1[-2])

#index 이용해서 ndarray 내 데이터값 수정하기
array1[0] = 9
array1[8] = 0
print(array1)

#다차원 ndarray에서 indexing
array1d = np.arange(start=1 , stop=10)
array2d = array1d.reshape(3,3) #다차원으로 만들기기
print(array2d)

print('(row = 0 , col = 0) index:', array2d[0,0])
print(' (row =0, col=1) index:', array2d[0,1]) #1행2열
print('(row = 2, col=2) index:',array2d[2,2]) #3행3열

#-----------------------------------------------------------------------#
#슬라이싱 : 
array1 = np.arange(start=1, stop=10)
array3 = array1[0:3]
print(array3)
print(type(array3))

array1[:3] #처음부터 3번째까지 #마지막 숫자 포함 안함함
array1[:]
array1[2:] #3번째부터 끝까지지

array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3,3)
print('array2d:\n',array2d)

print('array2d[0:2,0:2]\n', array2d[0:2,0:2])
print('array2d[1:3,0:3]\n', array2d[1:3,0:3])
print('array2d[1:3,:]\n',array2d[1:3,:])

#----------------------------------------------------------------------#
#행렬의 정렬- sort(), agsort()
org_array = np.array([3,1,9,5])
print('원본 행렬:', org_array)

#np.sort()로 정렬
sort_array1 = np.sort(org_array)
print(sort_array1) #오름차순으로 정리
print(np.sort(sort_array1)[::-1]) #내림차순으로 정리: np.sort()[::-1]

#ndarray.sort()로 정렬 :원본 행렬 자체를 변경
sort_array2 = org_array.sort()
print(sort_array2)
print(org_array)

#axis=0: column, axis=1: row
array2d = np.array([[8,12],[7,1]])
array2d_axis0 = np.sort(array2d, axis= 0) #row 방향으로 정렬
print(array2d_axis0)
array2d_axis1 = np.sort(array2d,axis = 1)
print(array2d_axis1)

####선형대수의 연산- 행렬의 내적과 전치 행렬 구하기: np.dot()
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8],[9,10],[11,12]])
dot_product = np.dot(A,B)
print(dot_product)

#전치 행렬 구하기 :np.transpose()
A = np.array([[1,2],[3,4]])
transpose_mat = np.transpose(A)
print(transpose_mat) #A의 전치 행렬
print(A)

