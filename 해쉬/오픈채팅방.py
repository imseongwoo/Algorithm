def solution(record):
    answer = []
    dict = {}
    id = []
    data = []
    for a in record:
        res = a.split()
        if res[0] == "Enter":
            dict[res[1]] = res[2]
            data.append(res[0])
            id.append(res[1])
        elif res[0] == "Leave":
            data.append(res[0])
            id.append(res[1])
        else:
            dict[res[1]] = res[2]

    for i in range(len(data)):
        if data[i]=="Enter":
            name = dict[id[i]]
            answer.append(name+"님이 들어왔습니다.")
        elif data[i] == "Leave":
            name = dict[id[i]]
            answer.append(name + "님이 나갔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))