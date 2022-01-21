import operator

genres = ["classic", "pop", "classic", "classic", "pop", "rock", "k-pop", "k-pop", "rock", "rnb"]
plays = [500, 600, 150, 800, 2500, 400, 1200, 5800000, 3400, 200, 1540]	

def solution(genres, plays):

    answer = []
    result_dict = {}
    total_plays_by_genre = {}
    genre_and_play = list(zip(genres, plays))
    

    # 장르 별 총 플레이 횟수
    for gp in genre_and_play:
        total_plays_by_genre[gp[0]] = total_plays_by_genre.get(gp[0], 0) + gp[1] #.get(__, {})도 되려나? -> 된다!
        result_dict[gp[0]] = dict()

    # print(result_dict)
    # 가장 많이 플레이된 장르를 알아내기 위해 내림차순으로 다시 정렬
    total_plays_by_genre = dict(sorted(total_plays_by_genre.items(), key = operator.itemgetter(1), reverse = True))

    for i in range(len(genre_and_play)):
        temp_dict = {}
        temp_dict[i] = genre_and_play[i][1] # 고유번호:재생횟수를 데이터로 갖는 temp_dict
        result_dict[genre_and_play[i][0]].update(temp_dict)  #update를 써보자
        result_dict[genre_and_play[i][0]] = dict(sorted(result_dict[genre_and_play[i][0]].items(), key = operator.itemgetter(1), reverse= True))

    # print('\ngenre_and_play: ', genre_and_play)
    # print('\ntotal_plays_by_genre: ', total_plays_by_genre)
    # print('\nresult_dict: ', result_dict)
    # print('\nresult_dict_keys: ', list(result_dict.keys()))
    # print()

    for genre in total_plays_by_genre.keys():
        answer.append(list(result_dict[genre].keys())[0])
        try:
            answer.append(list(result_dict[genre].keys())[1])
        except:
            pass


    
    return answer

print(solution(genres, plays))

