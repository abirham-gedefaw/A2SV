def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
     
    return "".join(l)

if __name__ == '__main__':
    
""" 
The above code have o(n) time and space complexity
But the following code is the optimized one with o(n) time complexity and o(1) space complexity 
    
"""
    
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
