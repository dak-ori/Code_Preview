def solution(brown, yellow):
    answer = []
    
    carpet = brown + yellow # 카펫의 길이
    
    for i in range(3, carpet) :
        if carpet % i == 0:
            div_num = carpet // i # 가로길이
            if (div_num - 2) * (i - 2) == yellow:
                answer.append(div_num)
                answer.append(i)
                return answer
    