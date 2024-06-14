# %%
import random
import time
from IPython.display import clear_output


def generate_numbers_sum_to_100(n):
    # 0과 100 사이에 n-1개의 랜덤 점을 찍고, 0과 100을 추가한 뒤 정렬
    points = sorted(random.sample(range(1, 100), n - 1))
    points = [0] + points + [100]

    # 인접한 점들 사이의 차이를 계산하여 n개의 숫자를 얻음
    return [points[i + 1] - points[i] for i in range(n)]


rcpDict = {1: "가위✌🏻", 2: "바위✊🏻", 3: "보✋🏻"}
point = 0

# 게임 설명글
print("*" * 40)
print("[ 슈퍼 랜덤 가위바위보 게임 ]")
print(
    "- 총 N번의 게임을 진행합니다.\n- 총 100점을 획득할 수 있으며, 각 게임마다 획득할 수 있는 점수는 랜덤입니다.\n"
)
print(
    "- 게임 중 최대 M번 특정 동작의 확률을 높일 수 있으며 획득 점수를 알기 전 선택합니다.\n"
)
print("- 이기면 점수를 온전히 획득, 비기면 1/3점 획득, 지면 획득하지 못합니다.")
print("*" * 40)

time.sleep(7)

gameTime = int(input("게임 수 입력"))
# n개의 랜덤 숫자가 합해서 100이 되도록 생성
random_numbers = generate_numbers_sum_to_100(gameTime)
# 게임 수 만큼 확률 올릴 기회 정하기
chance = (gameTime // 3) + 1

# 게임 N회 진행
for i, v in enumerate(random_numbers):
    weights = [1, 1, 1]
    # 컴퓨터 가위바위보 선택
    computerChoice = random.sample(range(1, 4), 1)[0]
    clear_output(wait=True)
    do = "n"

    print(f"[ {i+1}번째 경기 ]")
    print(f"너의 현재 점수 : {point}")

    # 기회가 남아있다면 확률 올릴지 말지 선택 가능
    if chance > 0:
        do = str(input(f"확률을 높이실건가요? {chance}번의 기회가 남았어요. (y/n)"))
    time.sleep(0.5)
    print(f"이번판 획득 가능 점수: {v}")
    print(f"컴퓨터는 <{rcpDict[computerChoice]}>를 낼겁니다.")

    # 확률 높일 동작 선택
    if do == "y":
        weightPoint = int(
            input("확률을 올릴 값을 선택해주세요.\n1. 가위✌🏻 / 2. 바위✊🏻 / 3.보✋🏻")
        )
        # 내가 선택한 동작 가중치 증가
        weights[weightPoint - 1] = 3
        # 기회 감소
        chance -= 1
    # 가중치 준 만큼 랜덤으로 가위바위보 선택
    choice = random.choices([1, 2, 3], weights, k=1)[0]
    # 내가 확률 올린 동작이 선택이 안됐을때
    if do == "y" and choice != weightPoint:
        print("확률 올리기 실패...")

    print(f"너는 <{rcpDict[choice]}>를 냈어요")

    # 가위바위보 우승 여부 판단
    if choice == computerChoice:
        print(f"비김! {v//3}점 획득!")
        point += v // 3
    elif computerChoice == 1:
        if choice == 2:
            print(f"우승! {v}점 획득!")
            point += v
        else:
            print("패배!")
    elif computerChoice == 2:
        if choice == 3:
            print(f"우승! {v}점 획득!")
            point += v
        else:
            print("패배!")
    elif computerChoice == 3:
        if choice == 1:
            print(f"우승! {v}점 획득!")
            point += v
        else:
            print("패배!")
    else:
        print("??")
    print("-" * 30)
    time.sleep(1.5)
    clear_output(wait=True)

# 최종 점수 산출
print(f"[ 너의 최종 점수 : {point} ]\n")
print(f"[ 총 게임 수 : {gameTime} ]\n")

if point == 100:
    print("< 어떻게 한거야 >")
elif point > 70:
    print("< 운이 좋아요 >")
elif point > 50:
    print("< 적당하네요 굿굿 >")
elif point > 30:
    print("< 운이 없어요 >")
else:
    print("< 개못하네요 >")
