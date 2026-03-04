import sys

def solve():
    input_data = sys.stdin.read().split()
    
    for x_str in input_data:
        x = int(x_str)
        
        if x == 0:
            break
            
        output = ' '.join(map(str, range(1, x + 1)))
        
        print(output)

if __name__ == "__main__":
    solve()