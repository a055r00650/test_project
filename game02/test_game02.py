# 定義撲克牌的花色和點數
poker_suit, poker_rank = ['♦', '♣', '♠', '♥'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# 生成所有一副撲克牌保存在list裡面

poker_cards = [f"{x}{y}" for x in poker_suit for y in poker_rank]
print(poker_cards)