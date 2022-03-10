# BOJ_1316 그룹 단어 체커

## 난이도
`실버5`

## 걸린시간
`20~30분`

## url
https://www.acmicpc.net/problem/1316

## 접근 방식

- 문자열이 그룹단어인지 체크하는 함수 `is_group` 만듬
  - 문자열 index 0을 `strs`에 넣고 순회 시작
  - 문자열이 연속 O: 그냥 지나감
  - 문자열이 연속 X: 문자가 `strs`에 있는지 확인, 없으면 `strs`에 추가. 있으면 return 0
  - 무사히 통과할 경우 return 1


- 모든 문자열에 대해 `is_group` 실행