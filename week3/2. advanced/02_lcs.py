"""
[동적 계획법 - 최장 공통 부분수열 (Longest Common Subsequence, LCS)]

▣ 문제 배경
- 두 문자열에서 동시에 등장하면서 "원래 순서를 유지" 하는 가장 긴 부분수열의 길이를
  구하는 표준 DP 문제입니다. (DNA 정렬, diff 알고리즘 등 응용 많음)
- 본 지문과 테스트 케이스는 본 학습 자료를 위해 자체적으로 작성되었습니다.

▣ 작은 예시
  s1 = "ABCBDAB"
  s2 = "BDCABA"

  공통 부분수열 후보: "B", "BCB", "BDAB", "BCAB", ...
  가장 긴 공통 부분수열의 길이: 4   (예: "BDAB" 또는 "BCAB")

▣ 구현할 함수
lcs_length(s1: str, s2: str) -> int
  - 두 문자열의 가장 긴 공통 부분수열의 길이를 정수로 반환합니다.
  - 어느 한쪽이라도 빈 문자열이면 0 을 반환합니다.

▣ 제약
- 0 <= len(s1), len(s2) <= 500 정도면 충분합니다 (O(m*n) 2차원 DP).

"""


def lcs_length(s1: str, s2: str) -> int:
    """
    s1, s2 의 가장 긴 공통 부분수열의 길이를 반환.
    어느 한쪽이라도 비어 있으면 0 을 반환합니다.
    """
    if len(s1)>500 or len(s1)<=0 or len(s2)>500 and len(s2)<=0:
      return 0
    
    max_length = 0
    long_str = ""
    short_str = ""
    if len(s2) < len(s1):
      long_str = s1
      short_str = s2
    else:
      long_str = s2
      short_str = s1
      
    max_list = []
    for i in range(len(short_str)):
      length = 0
      long_static_index = 0
      short_static_index = i
      long_index = long_static_index
      while short_static_index < len(short_str):
        if long_index < len(long_str):
          if long_str[long_index] == short_str[short_static_index]:
            long_index += 1
            long_static_index = long_index
            short_static_index += 1
            length += 1
          else:
            long_index += 1
        else:
          short_static_index += 1
          long_index = long_static_index
        
            
      max_list.append(length)   
      
    max_length = max(max_list)
    
    return max_length
    

if __name__ == "__main__":
    print("[테스트 1] 한쪽이 빈 문자열")
    print(f'  s1="", s2="abc" -> LCS 길이={lcs_length("", "abc")}')
    print()

    print("[테스트 2] 두 문자열이 동일")
    print(f'  s1="abc", s2="abc" -> LCS 길이={lcs_length("abc", "abc")}')
    print()

    print("[테스트 3] 공통 원소가 전혀 없음")
    print(f'  s1="abc", s2="xyz" -> LCS 길이={lcs_length("abc", "xyz")}')
    print()

    print("[테스트 4] 표준 예시 1")
    print(f'  s1="abcde", s2="ace" -> LCS 길이={lcs_length("abcde", "ace")}')
    print()

    print("[테스트 5] 표준 예시 2")
    print(f'  s1="AGGTAB", s2="GXTXAYB" -> LCS 길이={lcs_length("AGGTAB", "GXTXAYB")}')
    print()

    print("[테스트 6] 두 LCS 후보가 길이가 같은 경우")
    print(f'  s1="ABCBDAB", s2="BDCABA" -> LCS 길이={lcs_length("ABCBDAB", "BDCABA")}')
