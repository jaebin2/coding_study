#https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    username = {}
    ka_log = []
    answer = []
    
    for i in range(len(record)):
        if len(record[i].split()) == 3:
            cm, num, nick = record[i].split()
        else:
            cm, num = record[i].split()

        if (cm == "Enter"):
            cm = "들어왔습니다."
        if (cm == "Leave"):
            cm = "나갔습니다."

        ka_log.append((cm,num))

        if cm[i] != "Leave":
            username.update({num:nick})

    for i in range(len(record)):
        if ka_log[i][0] != "Change":
            answer.append(f"{username[ka_log[i][1]]}님이 {ka_log[i][0]}")
    
    return answer
