
def solution(s):
    # {{, }}를 제거 후 },{ 으로 나누기
    data = s[2:-2].split("},{")         # split으로 여러개 기준으로 나누기가 가능하네
    print(data)
    # 길이 별로 오름차순 정렬
    data = sorted(data, key=lambda x: len(x))
    answer = []
    for item in data:
        # 각각의 원소로 분류 후
        item = list(map(int, item.split(",")))
        for value in item:
            # 포함되어 있지 않으면 input
            if value not in answer:
                answer.append(value)
    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")