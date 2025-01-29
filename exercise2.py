from collections import deque

def is_palindrome(string : str) -> bool:
    result = True
    dq = deque()
    for char in string:
        if char != ' ':
            dq.append(char.lower())
    
    for _ in range(len(dq)):
        if len(dq) == 1:
            break
        elif len(dq) > 1:
            left = dq.popleft()
            right = dq.pop()
            print(f'left - {left}, right - {right}')
            if left != right:
                result = False
                break

    return result

def main():
    print(is_palindrome('ra d a r'))

if __name__ == '__main__':
    main()