# [BOJ_11723] 집합

## 문제정보
- 실버5
- 60분
- https://www.acmicpc.net/problem/11723

## 문제설명
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

* add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
* remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
* check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
* toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
* all: S를 {1, 2, ..., 20} 으로 바꾼다.
* empty: S를 공집합으로 바꾼다. 

## 풀이방법
### 비트 마스크(Bit mask)
* 메모리를 아끼기 위해 집합에 숫자가 있는지 여부를 이진수로 표현  
* 문제풀이에서는 0이 항상 포함되어 있다고 가정함.  
예를 들어, S = {1, 2, 3}이라면 0까지 포함시켜서 2\*\*3 + 2\*\*2 + 2\*\*1 + 2\*\*0 = 0b1111 = 15
* 101011 = 43

### 비트 연산자(Bitwise Operators)
* AND 연산 (&)  
대응하는 두 비트가 모두 1일 때 1을 반환


* OR 연산 (|)  
대응하는 두 비트가 하나라도 1이면 1을 반환


* XOR 연산 (^)  
대응하는 두 비트가 다르면 1을 반환, 같으면 0을 반환


* 보수 연산 (~)  
비트의 값을 반전하여 반환


* 시프트 연산(<<, >>)  
왼쪽 또는 오른쪽으로 비트를 옮긴다.
