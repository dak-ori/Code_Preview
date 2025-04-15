def solution(people, limit):
    people.sort()  # 무게순 정렬
    left = 0
    right = len(people) - 1
    count = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1 # 탈 수 있는 경우
        right -= 1 # 무거워서 못 타는 경우
        count += 1

    return count
