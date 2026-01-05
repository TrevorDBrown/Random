#
#   Cards.py
#   A basic playing card abstraction, for casino and other card games.
#

import json
import uuid
import random

class Card:
    def __init__(
        self,
        rank: str,
        suit: str,
        name: str,
        face_value: int,
        color: str,
        deck_id: uuid.UUID,
    ) -> None:
        self.__card: str = f"{rank}{suit}"
        self.__rank: str = rank
        self.__suit: str = suit
        self.__name: str = name
        self.__face_value: int = face_value
        self.__color: str = color
        self.__deck_id: uuid.UUID = deck_id

    def __str__(self) -> str:
        return f"{self.__card}"


class Deck:
    def __init__(self, cards: list[Card] = [], exclude_jokers: bool = False) -> None:
        self.__id: uuid.UUID = uuid.uuid4()
        self.__cards: list[Card] = []

        if len(cards) <= 0:
            # No cards provided. Generate a 52-54 card deck, contingent on inclusion of Joker cards.
            with open("Cards.json", "r", encoding="utf8") as fp:
                json_cards: dict = json.load(fp)

            for card in json_cards:
                if exclude_jokers and card["card_name"] == "Joker":
                    continue

                new_card: Card = Card(
                    rank=card["card_rank"],
                    suit=card["card_suit"],
                    name=card["card_name"],
                    face_value=card["face_value"],
                    color=card["color"],
                    deck_id=self.__id,
                )

                self.__cards.append(new_card)

        else:
            # A previously generated deck is provided. Generate a new deck from it.
            self.__cards = cards

        return

    def shuffle(self) -> None:
        random.shuffle(self.__cards)

        return

    def cards(self) -> list[Card]:
        return self.__cards

    def draw(self, cards_to_draw: int = 1) -> list[Card]:
        drawn_cards: list[Card] = []

        if (len(self.__cards) - cards_to_draw) <= 0:
            cards_to_draw = len(self.__cards)

        for draw in range(0, cards_to_draw):
            drawn_cards.append(self.__cards.pop())

        return drawn_cards

    def __str__(self) -> str:
        str_output: str = ""

        for i, card in enumerate(self.__cards):
            if i < len(self.__cards) - 1:
                str_output += f"{card}\n"
            else:
                str_output += f"{card}"

        return str_output


class Shoe:
    def __init__(self, shoe_size: int = 6) -> None:
        self.__decks: list[Deck] = []
        self.__mix_shoe = False

        for index in range(0, shoe_size):
            new_deck: Deck = Deck(exclude_jokers=True)
            self.__decks.append(new_deck)

        return

    def shuffle(self, mix_shoe: bool = True) -> None:
        combined_cards: list[Card] = []
        self.__mix_shoe = mix_shoe

        for deck in self.__decks:
            deck.shuffle()

            if mix_shoe:
                combined_cards.extend(deck.cards())

        if not mix_shoe:
            # Each deck was shuffled independently.
            return

        # All decks are shuffled together.
        shuffled_deck: Deck = Deck(cards=combined_cards)

        shuffled_deck.shuffle()

        self.__decks = [shuffled_deck]

        return

    def draw(self, cards_to_draw: int = 1) -> list[Card]:
        drawn_cards: list[Card] = []
        drawn: bool = False

        if (len(self.cards()) - cards_to_draw) <= 0:
            # Draw the remaining cards.
            print(
                f"Unable to draw {cards_to_draw} cards. Drawing remaining {len(self.cards())} cards from shoe."
            )

        for deck in self.__decks:
            if drawn:
                continue

            if len(self.cards()) > 0:
                drawn_cards.extend(deck.draw(cards_to_draw=cards_to_draw))
                cards_to_draw -= len(drawn_cards)

            if cards_to_draw <= 0:
                drawn = True

        return drawn_cards

    def cards(self) -> list[Card]:
        cards_in_shoe: list[Card] = []

        for deck in self.__decks:
            cards_in_shoe.extend(deck.cards())

        return cards_in_shoe

    def __str__(self) -> str:
        str_output: str = ""

        for deck in self.__decks:
            str_output += f"{deck}"

        return str_output


def main() -> None:
    # Generate a shoe. Defaults to a six-deck shoe.
    card_shoe: Shoe = Shoe(shoe_size=6)

    # Shuffle the shoe of decks.
    card_shoe.shuffle(mix_shoe=True)

    # Draw five cards (first hand).
    first_hand: list[Card] = card_shoe.draw(5)

    for card in first_hand:
        print(card)

    # Draw five cards (second hand).
    # second_hand: list[Card] = card_shoe.draw(308)

    # for card in second_hand:
    # print(card)

    print(f"{len(card_shoe.cards())} cards remaining in shoe.")

    for card in card_shoe.cards():
        print(card)

    # Show the cards.
    # print(card_shoe)

    return


if __name__ == "__main__":
    main()
