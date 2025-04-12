import numpy as np

array1 = np.array([1,2,3])   #array는 튜플 형태로 나타낸다
print('array1 type:', type(array1))
print('array1 array 형태:', array1.shape) #(3,)  =>1차원 데이터터

array2 = np.array([[1,2,3],[2,3,4]])
print('array2 type:', type(array2))
print('array2array형태:',array2.shape) #(2,3) 2row 3column

array3 = np.array([[1,2,3]])
print('array3 type:', type(array3))
print('array3 array 형태: ',array3.shape) #(1,3) =>2차원 데이터



###ndarray.ndim : array의 차원 확인
array1.ndim #1
array2.ndim #2
array3.ndim #2


###ndarray.dtype :데이터 타입 확인 ex)int32
list1 = [1,2,3]
print(type(list1))

array1 = np.array(list1)
print(type(array1))
array1.dtype #int64
print(array1, array1.dtype)



###리스트에 데이터 타입이 섞여있는 경우
list2 = [1, 2, 'test'] #int와 string이 섞인 경우
array2 = np.array(list2)
print(array2, array2.dtype) #=>'1','2' int=>str로 변경됨됨

list3 = [1, 2, 3.0]
array3 = np.array(list3)
print(array3, array3.dtype) #=>1.,2.,3. int=>float로 변경됨



###ndarray 내 데이터값의 타입 변경 : astype()
array_int = np.array([1,2,3])
array_float = array_int.astype('float64')
print(array_float, array_float.dtype) #[1. 2. 3.] float64

array_int1 = array_float.astype('float64')
print(array_int1, array_int1.dtype) #[1. 2. 3.]float64

array_float1 = np.array([1.1, 2.2, 3.3])
array_int2 = array_float1.astype('int32')
print(array_int2, array_int2.dtype)

#----------------------------------------------------------------------#
###ndarray 편리하게 생성하기 - arrange, zeros, ones

######1.arranye(첫값 포함, 끝값 미포함, 간격)
sequence_array = np.arange(10) #0부터 9까지지
print(sequence_array)
print(sequence_array.dtype, sequence_array.shape)

######2. zeros() : 모든 값을 0으로 채움  dtype을 정하지 않으면 default값은 float64
zero_array = np.zeros((3,2), dtype = 'int32')
print(zero_array)
print(zero_array.dtype, zero_array.shape)

######3. ones(): 모든 값을 1로 채움
one_array = np.ones((3,2))
print(one_array)
print(one_array.dtype, one_array.shape)  #dtype 미지정으로 float64가 나옴!

#------------------------------------------------------------------------------#
#ndarray의 차원과 크기 변경: reshape()

array1 = np.arange(10)
print('array1:\n', array1)

array2 = array1.reshape(2,5) #2행5열로
print('array2 : \n', array2)

array3 = array1.reshape (5,2)
print('array3 : \n', array3)

#-1을 인자로 적용하는 경우
array1 = np.arange(10)
print(array1)

array2 = array1.reshape(-1,5) #칼럼을 5개로 고정하고 로우는 자동으로 변환해
print(array2)
print('array2 shape:', array2.shape)

array3 = array1.reshape(5,-1)
print(array3)
print('array3 shape:' , array3.shape)

array3.reshape(-1,1) #열을 1개로 고정 =>무조건 2차원 데이터

#tolist(): array를 list로 변환
array1 = np.arange(8)
print(array1)
array3d = array1.reshape((2,2,2))
print('array3d :\n', array3d.tolist())

#3차원 array를 2차원 array로 변환
array5 = array3d.reshape(-1,1)
print(array5)
print(array5.tolist())
print(array5.shape)

#1차원 ndarray를 2차원 ndarray로 변환
array6 = array1.reshape(-1,1)
print(array6.reshape(-1,1))
print(array6.shape)

#----------------------------------------------------------------#
#####지피티와 함께 연습하기#####
array1 = np.arange(1,10).reshape(-1,3)
print(array1)

array2 = np.linspace(1,99,9).reshape(-1,3) #linspace(시작,끝,갯수) 갯수를 지정해주면 범위 안에서 같은 간격으로 나눠준다. 끝 포함
print(array2) 

print(array1 + array2) #두 배열 더하기

print(array1 * array2) #두 배열 곱하기

print(np.mean(array1)) #array1의 평균

######실습#####
x = np.array([[1,2],[3,4]]).reshape(-1,2)
y = np.array([[5,6],[7,8]]).reshape(-1,2)

print( x + y)
print( x * y)
print(np.sum(x))   #np.sum 과 sum 은 다르다! np.sum은 행렬 전체를 전해줌. sum은 열로 더해줌!
print(np.max(y))