def queensAttack(n, k, r_q, c_q, obstacles):
    # Directions the queen can move: (row change, column change)
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),  # vertical and horizontal
        (1, 1), (1, -1), (-1, 1), (-1, -1)  # diagonals
    ]
    
    # Convert obstacles list to a set of tuples for faster lookup
    obstacle_set = set((r, c) for r, c in obstacles)
    
    attackable_squares = 0
    
    # Check each direction
    for dr, dc in directions:
        nr, nc = r_q + dr, c_q + dc
        while 1 <= nr <= n and 1 <= nc <= n and (nr, nc) not in obstacle_set:
            attackable_squares += 1
            nr += dr
            nc += dc
    
    return attackable_squares

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    r_q = int(data[2])
    c_q = int(data[3])
    
    obstacles = []
    for i in range(k):
        obstacles.append((int(data[4 + 2 * i]), int(data[5 + 2 * i])))
    
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
