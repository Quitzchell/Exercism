package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	switch card {
	case "ace":
		return 11
	case "two":
		return 2
	case "three":
		return 3
	case "four":
		return 4
	case "five":
		return 5
	case "six":
		return 6
	case "seven":
		return 7
	case "eight":
		return 8
	case "nine":
		return 9
	case "ten":
		return 10
	case "jack":
		return 10
	case "queen":
		return 10
	case "king":
		return 10
	default:
		return 0
	}
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
	valueCard1 := ParseCard(card1)
	valueCard2 := ParseCard(card2)
	valueDealerCard := ParseCard(dealerCard)
	valueCombined := valueCard1 + valueCard2

	switch {
	case valueCard1 == 11 && valueCard2 == 11:
		return "P"
	case valueCombined == 21 && valueDealerCard < 10:
		return "W"
	case valueCombined == 21:
		return "S"
	case valueCombined >= 17 && valueCombined <= 20:
		return "S"
	case valueCombined >= 12 && valueCombined <= 16 && valueDealerCard < 7:
		return "S"
	case valueCombined >= 12 && valueCombined <= 16 && valueDealerCard >= 7:
		return "H"
	case valueCombined <= 11:
		return "H"
	default:
		return "H"
	}
}
