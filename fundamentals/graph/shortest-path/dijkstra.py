import heapq  # Built-in mean-heap

INF = int(1e9)


def print_path(start, end, parent):
    if start == end:
        print(start, end="")
        return
    print_path(start, parent[end], parent)
    print(f" -> {end}", end="")


def dijkstra(start, end, graph, distance, parent):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0 으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for to_other in graph[now]:
            # to_other[0] is the node, to_other[1] is the distance
            peek_node, peek_cost = to_other

            subtotal_cost = dist + peek_cost  # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리
            if subtotal_cost < distance[peek_node]:  # 현재 알려진 최단 거리보다 짧은 경우
                distance[peek_node] = subtotal_cost
                parent[peek_node] = now  # Track the parent
                heapq.heappush(q, (subtotal_cost, peek_node))  # 우선순위 큐에 삽입

    # 큐가 비었을 때 == 모든 노드의 최단 경로 확정
    print("distance: ", distance)
    print("parent: ", parent)

    # 최단 경로 출력
    print_path(start, end, parent)
    print(f" = {distance[end]}")


if __name__ == "__main__":
    # Representation of the graph in the video: https://www.youtube.com/watch?v=71Z-Jpnm3D4

    # 시작 및 터미널 노드 번호 입력받기
    start = "A"
    end = "F"

    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = {
        "A": INF,
        "B": INF,
        "C": INF,
        "D": INF,
        "E": INF,
        "F": INF,
    }

    graph = {
        "A": [("B", 5), ("C", 2)],
        "B": [("C", 1), ("E", 2), ("D", 4)],
        "C": [("E", 7)],
        "D": [("E", 6), ("F", 3)],
        "E": [("F", 1)],
        "F": [],  # Terminal node
    }

    # Initialize parent dictionary
    parent = {
        "A": None,
        "B": None,
        "C": None,
        "D": None,
        "E": None,
        "F": None,
    }

    # 다익스트라 알고리즘 수행
    dijkstra(start, end, graph, distance, parent)
