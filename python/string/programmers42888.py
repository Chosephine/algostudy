# 2019 KAKAO BLIND RECRUITMENT - 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

records = [i.split() for i in record]
user_info = {}
results = []
for r in records:
    if r[0] == 'Enter':
        user_info[r[1]] = r[2]
        results.append([r[1], '님이 들어왔습니다.'])
    elif r[0] == 'Leave':
        results.append([r[1], '님이 나갔습니다.'])
    else:
        user_info[r[1]] = r[2]
for i in range(len(results)):
    results[i] = user_info[results[i][0]] + results[i][1]
print(results)