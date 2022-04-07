# -*- coding: utf-8 -*-
import random
import hand

deck = []
marks = ['ハート', 'クローバー', 'ダイヤ', 'スペード']

# 山札をリセットする
def reset():
    global deck
    deck = list(range(1,49))


# 山札から任意の枚数のカードを引く
def draw(name, hand, number_of_draw):
    print(name + 'はカードを' + str(number_of_draw) + '枚引きました')
    
    for i in range(number_of_draw):
        draw_card = random.choice(deck)
        hand.append(draw_card)
        deck.remove(draw_card)
        
    return hand


# カードを引くか判定する
def is_draw(name, hand):
    input_text = input('カードを1枚引きますか？引く場合はYを、引かない場合はNを入力してください: ')

    if input_text == 'Y':
        return True 

    elif input_text == 'N':
        return False

    else:
        return is_draw(name, hand)