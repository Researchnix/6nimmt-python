import Player

def get_n_heads(num):
	if num == 55:
		return 7
	elif not(num % 11):
		return 5
	elif not(num % 10):
		return 3
	elif not(num % 5):
		return 2
	else:
		return 1

sum_row = lambda row: reduce(lambda x, y: get_n_heads(x)+y, row)

def sort_hand(name):
	# Higher bulls first
	if name == "Mean":
		return lambda hand: sorted(hand, key=get_n_heads, reverse=True)
	# Lower bulls first
	elif name == "Soft":
		return lambda hand: sorted(hand, key=get_n_heads)
	# Identity
	else:
		return lambda hand: hand

class Jonas(Player.Player):

	
	def pickRow(self, fields):
		# Picks minimal bull row, believe it
		return fields.cards.index((min(fields.cards, key=sum_row)))

	def playCard(self, fields):
		# hand sort behaviour based on name
		self.hand = sort_hand(self.name)(self.hand)

		# figures the highest bull rate card that don't take cards
		for card in self.hand:
			tmp = {}
			for n, row in enumerate(fields.cards):
				if card < row[-1]:
					continue
				elif card > row[-1]:
					tmp[n] = row[-1]

			if len(tmp) == 0:
				continue

			index = max(tmp.keys(), key=lambda x: tmp[x])
			if len(fields.cards[index]) < 5:
				return card
		return self.hand[0]
