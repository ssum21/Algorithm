import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    H = list(map(int, input().split()))
    W = list(map(int, input().split()))

    MAXH = 200000  # 문제 조건
    width_at = [0] * (MAXH + 2)

    for hi, wi in zip(H, W):
        width_at[hi] += wi

    ans = 0
    suffix = 0  # 현재까지의 sum_{v>=h} width_at[v]

    for h in range(MAXH, 0, -1):
        suffix += width_at[h]
        area = h * suffix
        if area > ans:
            ans = area

    print(ans)

if __name__ == "__main__":
    main()
