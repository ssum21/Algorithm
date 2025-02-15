from collections import defaultdict
import operator

def solution(genres, plays):
    music = defaultdict(list)
    total_play_music = defaultdict(int)
    
    for i in range(len(genres)):
        genre = genres[i]
        play_count = plays[i]
        
        total_play_music[genre] += play_count   
        music[genre].append((play_count,i))
        
    sorted_genres = sorted(total_play_music.keys(), key=lambda x : total_play_music[x], reverse=True)
    
    answer = []
    
    for genre in sorted_genres:
        sorted_songs = sorted(music[genre], key=lambda x:(-x[0],x[1]))
        answer.extend([song[1] for song in sorted_songs[:2]])
    
    return answer