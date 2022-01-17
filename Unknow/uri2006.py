def identifying_tea(tea, answer):
    return answer.count(tea)


def main():
    tea_type = int(input())
    contestant_answer = list(map(int, input().split()))
    print(identifying_tea(tea_type, contestant_answer))


main()

# or

# tea_type = int(input())
# contestant_answer = list(map(int, input().split()))
# print(contestant_answer.count(tea_type))
