def card_game(card_1, card_2, trump):
    deck = ['joker', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',
            '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',
            '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',
            '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠']

    if card_1 == card_2:
        return "Someone cheats."

    if card_1 == "joker":
        return "The first card won."

    if card_2 == "joker":
        return "The second card won."

    if card_1[-1] == card_2[-1]:
        return "The first card won." if deck.index(card_1) > deck.index(card_2) else "The second card won."

    if card_1[-1] == trump:
        return "The first card won."

    if card_2[-1] == trump:
        return "The second card won."

    return "Let us play again."
