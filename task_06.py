class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(players):
    if len(players) != 2:
        raise WrongNumberOfPlayersError()
    if players[0][1] not in 'RPS' or players[1][1] not in 'RPS':
        raise NoSuchStrategyError()
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

print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))
