import math 

def solve(N, step):
    step = step + 1
    maxI = float('inf')
    
    print(f'Step: {step}, value: {N}')
    
    if(N == 1):
        return step

    #for i in range(2, int(N/2)+1):
    for i in range(2, int(math.sqrt(N))+1):
        if(N % i == 0):  # checking if number is divisible or not
            maxI = min(maxI, max(N/i, i))
            print(str(N) + ' % ' + str(i) + ' = 0 maxI:' + str(maxI) )

    if maxI == float('inf'):
        return solve( N - 1, step)   
    return solve( maxI, step)

if __name__ == "__main__":
    text = input("Input positive number: ")
    n = int(text)
    if n <= 0:
        raise Exception('NoPositiveNumber')
    print('Min number of steps: ' + str(solve(n, -1)))