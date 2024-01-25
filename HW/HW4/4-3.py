def play_card_game():
    try:
        player1, player2 = input().split()
        health1, health2 = map(int, input().split())
        damages = list(map(int, input().split())) 
        score1, score2 = 0, 0
        card_mapping = {"A": 0, "B": 1, "C": 2}
        for _ in range(3):
            card1, card2 = input().split()
            damage1, damage2 = damages[card_mapping[card1]], damages[card_mapping[card2]]

            health1 -= damage2
            health2 -= damage1

            if damage1 > damage2:
                score1 += 1
            elif damage2 > damage1:
                score2 += 1

        print(f"{player1} -> Score: {score1}, Health: {health1}")
        print(f"{player2} -> Score: {score2}, Health: {health2}")

    except ValueError: 
        print("Invalid Command.")

play_card_game()