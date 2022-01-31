import random

card_suits: list[str] = '♠ ♥ ♣ ♦'.split()
cards: list[str] = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def create_deck_cards(aleatory: bool = False) -> cards:
    """Create deck with 52 cards
    :param aleatory: boolean
    :return: deck_cards
    """
    deck_cards = [(cs, c) for c in cards for cs in card_suits]
    if aleatory:
        random.shuffle(deck_cards)
    return deck_cards


def dealing_the_cards(deck_cards: cards) -> tuple[cards, cards, cards, cards]:
    """Dealing the cards to the players
    :param deck_cards: cards
    :return: list with 4 tuples
    """
    return deck_cards[0::4], deck_cards[1::4], deck_cards[2::4], deck_cards[3::4]


def player_game() -> None:
    """Start card game
    :return: cards for players
    """
    cards_game: cards = create_deck_cards(aleatory=True)
    players: list[str] = 'P1 P2 P3 P4'.split()
    dealing_cards: dict[str, cards] = {p: c for p, c in zip(players, dealing_the_cards(cards_game))}

    for player, player_cards in dealing_cards.items():
        card: str = ' '.join(f'{p}{c}' for (p, c) in player_cards)
        print(f'{player}: {card}')


if __name__ == '__main__':
    player_game()
