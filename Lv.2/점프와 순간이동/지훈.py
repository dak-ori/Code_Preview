def solution(n):
    total = format(n, 'b')
    count = 0
    for i in range(len(total)):
        if total[i] == '1':
            count += 1
    return count