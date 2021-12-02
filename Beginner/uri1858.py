n = int(input())
t = map(int, input().split())


def theon_answer(people):
    people_list = list(people)
    minor = min(people_list)
    result = people_list.index(minor) + 1
    print(result)


theon_answer(t)
