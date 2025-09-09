stones = input()
hit = input()

def hit_count(stones, hit):
    if hit == stones[0]:
        return '6'
        
    flag = False
    count = 0
    for i, digit in enumerate(stones):
        if digit == hit or flag:
            flag = True
            count += 1
    return str(count)

stones_digit = stones.split(' ')
print(hit_count(stones_digit, hit))