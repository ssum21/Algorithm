from collections import defaultdict

def solution(genres, plays):
    genre_play_count = defaultdict(int)  # 장르별 총 재생 횟수 저장
    genre_songs = defaultdict(list)  # 장르별 노래 목록 저장

    # 데이터 저장
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_count[genre] += play
        genre_songs[genre].append((play, i))

    # 1. 장르별 총 재생 횟수를 기준으로 정렬
    sorted_genres = sorted(genre_play_count, key=genre_play_count.get, reverse=True)

    answer = []

    # 2. 각 장르별 노래를 정렬하여 수록
    for genre in sorted_genres:
        # (재생 횟수 내림차순, 고유 번호 오름차순) 정렬 후 최대 2곡 선택
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))[:2]
        answer.extend(idx for _, idx in sorted_songs)

    return answer

