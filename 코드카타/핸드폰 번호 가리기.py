def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-4):
        answer = answer + '*'
    for i in range(len(phone_number)-4, len(phone_number)):
        answer += phone_number[i]
    return answer

solution("01033334444")