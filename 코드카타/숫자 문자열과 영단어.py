def solution(s):
    num = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    answer = []

    temp = ""
    for a in s:
        if a.isdigit():
            answer.append(a)
            continue
        else:
            temp += a
            if temp in num:
                answer.append(num[temp])
                temp = ""
    return int(''.join(answer))


print(solution("one4seveneight"))
