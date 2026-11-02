import random
def simulate_100_coins_riddle():
    
    heads = 1
    tails = 0
    initial_p = [heads] * 10 + [tails] * 90
    
    random.shuffle(initial_p)
    
    group_a = initial_p[:10]
    group_b = initial_p[10:]
    
    flipped_group_a = []
    for coin in group_a:
        flipped_group_a.append(1 - coin)
        
    heads_in_a = sum(flipped_group_a)
    heads_in_b = sum(group_b)
    
    print("Verification")
    print(f"Group A (10 coins in total) contains: {heads_in_a} Heads")
    print(f"Group B (90 coins in total) contains: {heads_in_b} Heads")
    print(f"Success! Do both groups match? {heads_in_a == heads_in_b}")
    
if __name__ == "__main__":
    simulate_100_coins_riddle()
