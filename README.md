# Mini_Project_Blackjack
24.07.11

## 실행 화면

### 블랙잭 게임이란?
- 카드 게임의 한 종류로, 목표는 카드의 합계가 21을 넘지 않으면서 가능한 한 21에 가깝게 만드는 것
- 카드를 계산하는 방식은 2부터 10에 이르는 모든 카드가 액면가로 계산됨. 잭, 퀸, 킹은 10으로 계산하고 에이스(A)는 1 또는 11로 계산할 수 있음

### 게임 진행 방식
1. 초기 배분
  - 딜러와 플레이어는 각각 두 장의 카드를 받음
  - 플레이어의 두 카드는 모두 공개됨
  - 딜러는 한 장의 카드는 공개하고, 다른 한 장의 카드는 비공개로 유지함
2. 플레이어의 선택
  - 플레이어는 합계가 21을 넘지 않도록 추가 카드를 요청(히트)하거나, 멈출(스탠드) 수 있음
  - 플레이어가 카드를 추가로 받아 합계가 21을 초과하면 즉시 패배함
3. 딜러의 규칙
  - 딜러는 합계가 17 이상이면 더 이상 카드를 받을 수 없음
  - 딜러의 합계가 16 이하이면 반드시 카드를 추가로 받아야 함
4. 결과
  - 플레이어가 더 이상 카드를 받지 않겠다고 선언하면, 딜러는 자신의 두 번째 카드를 공개하고 규칙에 따라 행동함
  - 딜러와 플레이어의 카드 합계를 비교하여 더 높은 합계가 승리함
  - 합계가 같으면 무승부로 끝남

### 예시
1. 초기 배분: 딜러가 10을 가지고 있고, 플레이어는 퀸을 가지고 있음. 딜러는 공개된 10 외에 비공개 카드 하나를 추가로 가지고 있음
2. 추가 배분: 플레이어는 3을 받아 합계가 13이 됨. 플레이어는 계속 카드를 요청할 수 있음
3. 게임 종료: 플레이어가 21을 넘지 않고 카드를 그만 받겠다고 하면, 딜러는 자신의 비공개 카드를 공개하고 규칙에 따라 추가 카드를 받을지 결정함
4. 승패 결정: 딜러와 플레이어의 합계를 비교하여 승부를 결정함

## Flow Chart
<img width="726" alt="image" src="https://github.com/jysung1122/Mini_Project_Blackjack/assets/56614779/41bb938e-68d1-4eca-a53d-f78847997f17">
