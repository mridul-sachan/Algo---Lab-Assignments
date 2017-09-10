def get_min_coins(rate_list, amount):

	res = [0 for i in range(0,amount+1)]
	n = len(rate_list)

	for j in range(1, amount+1):
		smallest = float("inf")
		for k in range(0,n):
			if rate_list[k] <= j:
				smallest = min(smallest, res[j - rate_list[k]])
				#print("Value of j: {0}, k: {1}, smallest: {2}".format(j,k,smallest))

		res[j] = 1+smallest
		
	return res[amount]			




if __name__ == "__main__":
	problems = [
    [[1, 3, 4],  20],
    [[1, 2, 3],  9],
    [[1, 2, 3],  10],
    [[1, 5], 13923],
    [[7, 22, 71, 231], 753],
    [[3, 5, 12], 25],
    [[800], 800],
    [[2], 50000]
	]

	
	for rate_list,amount in problems:
		print("Min no of coins: ",get_min_coins(rate_list, amount))
