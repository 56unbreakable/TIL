from collections import deque

# dfs
# 입력 그래프는 인덱스가 노드번호인 리스트 형태로 들어감
# depth를 반환하며, 연결되지 않았을 경우에는 -1을 반환
def dfs(graph,root,dest):
    stack_s = deque()
    stack_s.append(root)
    visited = deque()
    depth = 0
    depth_chart = [-1]*(len(graph))
    depth_chart[root] = 0
    while stack_s:
        curr = stack_s.pop()
        visited.append(curr)
        if depth_chart[curr] == -1:
            depth += 1
        else:
            depth = depth_chart[curr]
        # 노드를 순서대로 방문하고싶다면 여기서 정렬을 사용하면됨
        # 작은 노드부터 방문하고 싶을 시 graph[curr].sort(reverse = True)
        # 큰 노드부터 방문하고 싶을  시 graph[curr].sort()
        for node in graph[curr]:
            if node not in visited and node not in stack_s:
                stack_s.append(node)
                depth_chart[node] = depth + 1
    result_depth = depth_chart[dest]
    # 방문 순서를 반환하고싶다면 visited를 반환하면 됨
    return result_depth