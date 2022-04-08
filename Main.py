import player_vs_computer as p_v_c
import player_vs_player as p_v_p


def main(min_take=1, max_take=3, number_of_candies=10):
    game = int(input('Введите 1, если хотите играть против компьютера, и 2 - если вдвоем: '))
    if game == 1:
        p_v_c(min_take, max_take, number_of_candies)
    else:
        p_v_p(min_take, max_take, number_of_candies)


main()
