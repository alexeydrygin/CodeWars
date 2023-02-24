Lеt's create function to play cards. You receive 3 arguments: card1 and card2 are cards from a single deck; trump is the main suit, which beats all others.

You have a preloaded deck (in case you need it):

```
deck = ["joker","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♣",
                "2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦","A♦",
                "2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♥",
                "2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♠"]
```

Game rules
If both cards have the same suit, the higher one wins
If both cards have trump, the higher one wins
If the cards have different suits and no one has trump, return "Let us play again."
If one card has trump, but not the other, the one with the trump wins
If there is a winner, return "The first/second card won."
If the two cards are the same, return "Someone cheats."
The joker always wins
Examples

```
"3♣", "Q♣", "♦"  -->  "The second card won."
"5♥", "A♣", "♦"  -->  "Let us play again."
"8♠", "8♠", "♣"  -->  "Someone cheats."
"2♦", "A♠", "♦"  -->  "The first card won."
"joker", "joker", "♦"  -->  "Someone cheats."
```

## игра в карты

Опишем функцию для игры в карты согласно правилам, принимающую 3 аргумента: card1 и card2 - карты из одной колоды, trump - козырная масть, которая побеждает все остальные.

В качестве входных данных также предоставляется предварительно загруженная колода карт (deck), которая может понадобиться для решения задачи.

Правила игры следующие:

- Если обе карты имеют одну и ту же масть, побеждает карты с большим номиналом.
- Если обе карты являются козырными, побеждает карты с большим номиналом.
- Если карты имеют разные масти и никто из них не является козырным, вернуть "Let us play again."
- Если одна карта является козырной, а другая нет, то побеждает карта с козырной мастью.
- Если есть победитель, вернуть "The first/second card won."
- Если обе карты одинаковы, вернуть "Someone cheats."
- Джокер всегда побеждает.
