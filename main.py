# -*- coding: utf-8 -*-
import card
import hand

player_name = 'あなた'
dealer_name = 'ディーラー'

# リトライ
def retry():
    input_text = input('もう一度遊びますか？遊ぶ場合はYを、終わる場合はNを入力してください: ')
    
    if input_text == 'Y':
        game_start()

    elif input_text == 'N':
        print('また遊んでね')
        exit()

    else:
        retry()


# ゲームスタート
def game_start():
    print('ゲームスタート\n')

    # 初期化
    player_hand = []
    dealer_hand = []
    card.reset()

    # 初手引き
    ## プレイヤーは山札からカードを2枚引く
    player_hand = card.draw(player_name, player_hand, 2)

    ## プレイヤーの手札を標準出力する
    hand.print_list(player_name, player_hand, False)

    ## プレイヤーの手札の合計を標準出力する
    hand.print_total(player_hand)

    ## ディーラーは山札からカードを2枚引く
    dealer_hand = card.draw(dealer_name, dealer_hand, 2)

    ## ディーラーの手札を標準出力する
    hand.print_list(dealer_name, dealer_hand, True)

    ## 追加でカードを引くか確認する
    while card.is_draw(player_name, player_hand):
        ## プレイヤーは山札からカードを1枚引く
        player_hand = card.draw(player_name, player_hand, 1)

        ## プレイヤーの手札を標準出力する
        hand.print_list(player_name, player_hand, False)

        ## プレイヤーの手札の合計を標準出力する
        hand.print_total(player_hand)

        ## ディーラーの手札を標準出力する
        hand.print_list(dealer_name, dealer_hand, True)

        ## プレイヤーの手札がバーストしているかを判定する
        if hand.is_burst(player_hand):
            print(player_name + 'の手札の合計が21を超えました')
            print(player_name + 'の負けです')
            retry()

    # プレイヤーのターン終了
    ## プレイヤーの手札を標準出力する
    hand.print_list(player_name, player_hand, False)

    ## プレイヤーの手札の合計を標準出力する
    hand.print_total(player_hand)

    ## ディーラーの手札を標準出力する
    hand.print_list(dealer_name, dealer_hand, False)

    ## ディーラーの手札の合計を標準出力する
    hand.print_total(dealer_hand)

    ## ディーラーの手札がバーストしているかを判定する
    if hand.is_burst(dealer_hand):
        print(dealer_name + 'の手札の合計が21を超えました')
        print(player_name + 'の勝ちです')

    ## ディーラーは手札の合計が17以上になるまでカードを引く
    while hand.calculate_total(dealer_hand) < 17: 
        ## ディーラーは山札からカードを1枚引く
        dealer_hand = card.draw(dealer_name, dealer_hand, 1)

        ## プレイヤーの手札の合計を標準出力する
        hand.print_list(player_name, player_hand, False)

        ## ディーラーの手札を標準出力する
        hand.print_total(player_hand)

        ## ディーラーの手札を標準出力する
        hand.print_list(dealer_name, dealer_hand, False)

        ## ディーラーの手札の合計を標準出力する
        hand.print_total(dealer_hand)

    else:
        ## ディーラーの手札がバーストしているかを判定する
        if hand.is_burst(dealer_hand):
            print(dealer_name + 'の手札の合計が21を超えました')
            print(player_name + 'の勝ちです')

        else:
            ## 勝敗を判定する
            player_hand_total = hand.calculate_total(player_hand)
            dealer_hand_total = hand.calculate_total(dealer_hand)
            if player_hand_total > dealer_hand_total:
                print(player_name + 'の勝ちです')

            elif player_hand_total < dealer_hand_total:
                print(player_name + 'の負けです')

            else:
                print('引き分けです')

    retry()

game_start()