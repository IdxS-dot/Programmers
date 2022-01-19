import operator

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]	

def solution(genres, plays):

    total_plays_by_genre = {}
    genre_and_play = list(zip(genres, plays))

    # 장르 별 총 플레이 횟수
    for gp in genre_and_play:
        total_plays_by_genre[gp[0]] = total_plays_by_genre.get(gp[0], 0) + gp[1] #.get(__, {})도 되려나?

    # 가장 많이 플레이된 장르를 알아내기 위해 내림차순 정렬한 리스트가 total_pbg
    total_pbg = sorted(total_plays_by_genre.items(), key = operator.itemgetter(0), reverse=True)



    answer = []
    return answer

solution(genres, plays)