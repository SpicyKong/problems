def solution(genres, plays):
    answer = []
    N = len(genres)
    dict_plays = {i:plays[i] for i in range(N)}
    dict_genres = {i:genres[i] for i in range(N)}
    list_songs = [i for i in range(N)]
    list_songs.sort(key=lambda a:dict_plays[a],reverse=True)
    genres_index = {}
    list_genres = []
    count = 0
    for song in list_songs:
        if dict_genres[song] in genres_index:
            list_genres[genres_index[dict_genres[song]]].append(song)
            list_genres[genres_index[dict_genres[song]]][0] += dict_plays[song]
        else:
            genres_index[dict_genres[song]] = count
            list_genres.append([dict_plays[song], song])
            count+=1
    list_genres.sort(key=lambda a:a[0],reverse=True)
    for genre in list_genres:
        count = 0
        for song in genre:
            if count:
                answer.append(song)
            count += 1
            if count>=3:
                break
    return answer
genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
solution(genres, plays)
