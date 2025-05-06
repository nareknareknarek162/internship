class WrongNumbersOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def check(contestants):
    if len(contestants) != 2:
        raise WrongNumbersOfPlayersError('WrongNumbersOfPlayersError')
    if contestants[0][1] not in 'RPS' or contestants[1][1] not in 'RPS':
        raise NoSuchStrategyError('NoSuchStrategyError')
    return True


def rps_game_winner(players):
    try:
        if check(players):
            player0, move0 = players[0]
            player1, move1 = players[1]
            if move0 == 'S':
                if move1 == 'P':
                    return f'{player0} {move0}'
                elif move1 == 'R':
                    return f'{player1} {move1}'
            if move0 == 'P':
                if move1 == 'S':
                    return f'{player1} {move1}'
                elif move1 == 'R':
                    return f'{player0} {move0}'
            if move0 == 'R':
                if move1 == 'P':
                    return f'{player1} {move1}'
                elif move1 == 'S':
                    return f'{player0} {move0}'
            return f'player1 {move0}'
    except WrongNumbersOfPlayersError as e:
        return e
    except NoSuchStrategyError as e:
        return e


print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))
