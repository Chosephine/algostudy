# 이코테 기출 30 가사 검색
# 2020 KAKAO BLIND RECRUITMENT
# https://school.programmers.co.kr/learn/courses/30/lessons/60060

# 키워드와 매칭하는 가사 개수 찾는 함수
def cnt_match(lyrics, keyword, idx_dict, idx_dict_keys):
    print("curent keyword : " + keyword)
    # 현재 keyword 관련 정보(L: 길이, nran_idx: (와일드카드가 접두사인지여부, 랜덤 아닌 부분 start idx, end idx) )
    L = len(keyword)
    if keyword[0] == '?':
        for i in range(len(keyword)):
            if keyword[i] != '?':
                nran_idx = (True, i, L)
                break
    else:
        for i in range(len(keyword)):
            if keyword[i] == '?':
                nran_idx = (False, 0, i)
                break
    print(nran_idx)

    # 단어 탐색
    cnt = 0
    if not idx_dict_keys.count(L):
        pass
    elif idx_dict_keys.index(L) == len(idx_dict_keys) - 1:
        for i in range(idx_dict[L], len(lyrics)):
            if check_word(lyrics[i], keyword, nran_idx):
                cnt += 1
    else:
        for i in range(idx_dict[L], idx_dict[idx_dict_keys[idx_dict_keys.index(L) + 1]]):
            if check_word(lyrics[i], keyword, nran_idx):
                cnt += 1

    return cnt


def check_word(lyric, kwd, kwd_info):
    for i in range(kwd_info[1], kwd_info[2]):
        if lyric[i] != kwd[i]:
            return False
    print(lyric)
    return True


def solution(words, queries):
    # words 길이별 정렬
    words.sort(key=len)
    print(words)

    # words 길이 idx에 따른 dict 생성
    words_idx_dict = dict()
    for i in range(len(words)):
        word_len = len(words[i])
        if not words_idx_dict.get(word_len):
            words_idx_dict[word_len] = i
    words_idx_dict[len(words[0])] = 0

    print(words_idx_dict)

    # answer = words_idx_dict
    # result 담을 list 생성
    result = []
    for query in queries:
        result.append(cnt_match(words, query, words_idx_dict, list(words_idx_dict)))

    # return answer
    return result



print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))