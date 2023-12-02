def solution(genres, plays):
    answer = []
    music = {}
    for i in range(len(genres)):
        music[genres[i]] = music.get(genres[i], 0) + plays[i]

    while music:
        maxval = -1
        maxgenre = ""

        for a in music:
            if music[a] > maxval:
                maxval = music[a]
                maxgenre = a
        res = []
        for i in range(len(genres)):
            if genres[i] == maxgenre:
                res.append((plays[i],i))

        res.sort(reverse=True,key=lambda x: (x[0],-x[1]))

        if len(res) >= 2:
            answer.append(res[0][1])
            answer.append(res[1][1])
        else:
            for a in res:
                answer.append(a[1])

        del music[maxgenre]

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
