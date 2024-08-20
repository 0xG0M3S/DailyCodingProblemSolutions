
if __name__=='__main__':
    
    value = input('Input string: ')
    
    if(len(value) <= 0):
        exit
    
    result = ''
    last = ''
    i = 0
    while i < len(value):
        if last != value[i]:
           result += value[i]
           last = value[i] 
        
        i += 1
    
    if( result[0] == ')'):
        result = '(' + result
    
    if( result[len(result) -1] == '('):
        result += ')'
    
    print(f'Result: {result}')