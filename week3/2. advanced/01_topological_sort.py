"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]


"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
   
    # queue = deque()
    # result = []
    # nums = {}
    # for i in range(vertices):
    #     nums[i] = 0
    # for edge in edges:
    #     nums[edge[1]] +=1
    
    # while nums:
    #     for i in nums:
    #         if nums[i] == 0:
    #             queue.append(i)
        
    #     vertice = queue.popleft()
    #     if nums[vertice]:
    #         del nums[vertice]
    #     result.append(vertice)
    #     removeIndex = []
    #     for i in range(len(edges)):
    #         if edges[i][0] == vertice:
    #             nums[edges[i][1]] -= 1
    #             removeIndex.append(i)
    #     for i in removeIndex:
    #         edges.pop(i)
        
                
            

    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
