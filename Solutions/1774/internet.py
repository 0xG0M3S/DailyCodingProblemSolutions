# https://www.geeksforgeeks.org/minimum-step-reach-one/
# Python3 program to get minimum step
# to reach 1 under given constraints

# Structure represent one node in queue
class data:

	def __init__(self, val, steps):
		self.val = val
		self.steps = steps


# Method returns minimum step to reach one
def minStepToReachOne(N):
	q = []
	q.append(data(N, 0))

	# Set is used to visit numbers
	# so that they won't be pushed
	# in queue again
	st = set()

	# Loop until we reach to 1
	while (len(q)):

		t = q.pop(0)

		# If current data value is 1,
		# return its steps from N
		if (t.val == 1):
			return t.steps

		# Check curr - 1, only if
		# it not visited yet
		if not (t.val - 1) in st:
			q.append(data(t.val - 1, t.steps + 1))
			st.add(t.val - 1)

		# Loop from 2 to Math.sqrt(value)
		# for its divisors
		for i in range(2, int((t.val) ** 0.5) + 1):

			# Check divisor, only if it is not
			# visited yet if i is divisor of val,
			# then val / i will be its bigger divisor
			if (t.val % i == 0 and (t.val / i) not in st):
				q.append(data(t.val / i, t.steps + 1))
				st.add(t.val / i)
	return -1

# Driver code
#N = 17
#print(minStepToReachOne(N))

# This code is contributed by phasing17

if __name__ == "__main__":
    text = input("Input positive number: ")
    n = int(text)
    if n <= 0:
        raise Exception('NoPositiveNumber')
    print('Min number of steps: ' + str(minStepToReachOne(n)) )