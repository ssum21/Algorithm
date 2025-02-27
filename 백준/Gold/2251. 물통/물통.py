import sys

input=sys.stdin.readline

A, B, C = map(int, input().split())

visited = set()
result = set()

sizeA= A
sizeB = B
sizeC = C
total = C


def BFS(a, b, c):
    """
    (a, b, c): 현재 A물통에 a, B물통에 b, C물통에 c 리터가 들어있는 상태.
    """
    # 이미 방문했거나 범위를 벗어나면 중단
    if (a, b, c) in visited or a < 0 or b < 0 or c < 0 or a > sizeA or b > sizeB or c > sizeC:
        return

    # 방문하지 않은 상태면 방문 처리
    visited.add((a, b, c))
    
    # 디버깅 등을 위해 상태를 출력 (필요 없으면 주석 처리 가능)
    # print(a, b, c)

    # 첫 번째 물통(A)이 비어있고, 전체 물 양이 처음과 같다면 C물통 양을 결과에 추가
    # (실제로 a+b+c는 항상 total이므로, 여기서는 `if a == 0:` 만 검사해도 됩니다)
    if a == 0 and a + b + c == total:
        result.add(c)

    # ----------------------
    # 1) B -> A (B물통에서 A물통으로 물 옮기기)
    # ----------------------
    if b > 0 and a < sizeA:
        # 실제로 옮길 수 있는 양
        transfer = min(b, sizeA - a)
        BFS(a + transfer, b - transfer, c)

    # ----------------------
    # 2) A -> B (A물통에서 B물통으로 물 옮기기)
    # ----------------------
    if a > 0 and b < sizeB:
        transfer = min(a, sizeB - b)
        BFS(a - transfer, b + transfer, c)

    # ----------------------
    # 3) C -> A (C물통에서 A물통으로 물 옮기기)
    # ----------------------
    if c > 0 and a < sizeA:
        transfer = min(c, sizeA - a)
        BFS(a + transfer, b, c - transfer)

    # ----------------------
    # 4) A -> C (A물통에서 C물통으로 물 옮기기)
    # ----------------------
    if a > 0 and c < sizeC:
        transfer = min(a, sizeC - c)
        BFS(a - transfer, b, c + transfer)

    # ----------------------
    # 5) C -> B (C물통에서 B물통으로 물 옮기기)
    # ----------------------
    if c > 0 and b < sizeB:
        transfer = min(c, sizeB - b)
        BFS(a, b + transfer, c - transfer)

    # ----------------------
    # 6) B -> C (B물통에서 C물통으로 물 옮기기)
    # ----------------------
    if b > 0 and c < sizeC:
        transfer = min(b, sizeC - c)
        BFS(a, b - transfer, c + transfer)

    # ----------------------
    # 6) B -> C (B물통에서 C물통으로 물 옮기기)
    # ----------------------
    if b > 0 and c < sizeC:
        transfer = min(b, sizeC - c)
        BFS(a, b - transfer, c + transfer)


BFS(0, 0, C)
result = sorted(result)
for i in result:
    print(i, end=' ')