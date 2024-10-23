card1 = int(input("1-11 "))
card2 = int(input("1-11 "))

card_sum = card1 + card2
if card_sum > 21:
    print("Bust")
elif card_sum < 21:
    print("Not Blackjack")
else:
    card_sum = 21
print("Blackjack")

#again bool note were confusing