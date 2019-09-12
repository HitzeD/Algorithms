#!/usr/bin/python

import argparse

arr = [1050, 270, 1540, 3800, 2]

def find_max_profit(prices):
	max_profit = -9999999999999
	

	for i in reversed(range(0, len(prices))):

		for j in reversed(range(0, len(prices))):

			# skips the current or previous indexes
			if j >= i:
				pass
			else:
				if (prices[i] - prices[j]) > max_profit:
					max_profit = prices[i] - prices[j]
	return max_profit


			

	


find_max_profit(arr)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))