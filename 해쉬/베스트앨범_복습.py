def solution(genres, plays):
    answer = []
    music = {}
    for i in range(len(genres)):
        music[genres[i]] = music.get(genres[i], 0) + plays[i]

    while music:
        max_genre = max(music, key=music.get)
        print(max_genre)
        max_play = music[max_genre]

        res = [(plays[i], i) for i, genre in enumerate(genres) if genre == max_genre]
        res.sort(reverse=True, key=lambda x: (x[0], -x[1]))

        if len(res) >= 2:
            answer.extend([res[0][1], res[1][1]])
        else:
            answer.extend(a[1] for a in res)

        del music[max_genre]
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))