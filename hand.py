import card

# 手札を開示する
def print_list(name, hand, is_hidden):
    print(name + 'の手札')

    hand_num = 1

    for i in hand:
        mark = card.marks[i // 13]
        number = 13 if i % 13 == 0 else i % 13

        ## 初手のディーラーの2枚目を隠す
        if is_hidden and hand_num == 2:
            print(str(hand_num) + '枚目: ***\n')

        else:
            print(str(hand_num) + '枚目: ' + mark + str(number))
        
        hand_num += 1


# 手札の合計を計算する
def calculate_total(hand):
    result = 0

    for i in hand:
        result += 10 if i % 13 == 11 or i % 13 == 12 or i % 13 == 0 else i % 13

    return result


# 手札の合計を標準出力する
def print_total(hand):
    total = calculate_total(hand)
    print('合計: ' + str(total) + '\n')


# バースト判定をする
def is_burst(hand):
    total = calculate_total(hand)
    if total > 21:
        return True
    else:
        return False