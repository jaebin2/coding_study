#https://programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = []
    tmp = list(map(lambda x, y:x|y, arr1, arr2))
    tmp = list(map(lambda x:f'{x:0{n}b}', tmp))

    for i in range(n):
        tmp2 = ''
        for j in range(n):
            if tmp[i][j] == '1':
                tmp2 = tmp2 + '#'
            else:
                tmp2 = tmp2 + ' '
        answer.append(tmp2)

    return answer
