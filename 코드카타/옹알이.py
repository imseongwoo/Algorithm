def solution(babbling):
    answer = 0
    speak = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        i = 0
        valid = True
        previous_speak_word = ""

        while i < len(word) and valid:
            match_found = False

            for a in speak:
                if word[i:i + len(a)] == a and a != previous_speak_word:
                    match_found = True
                    previous_speak_word = a
                    i += len(a)
                    break

            if not match_found:
                valid = False

        if valid and i == len(word):
            answer += 1

    return answer

def solution2(babbling):
    answer = 0
    for babb in babbling:
        for bab in ["aya", "ye", "woo", "ma"]:
            if bab * 2 not in babb:
                babb=babb.replace(bab,' ')
        if len(babb.strip()) == 0:
            answer+=1

    return answer

test_babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(test_babbling))
