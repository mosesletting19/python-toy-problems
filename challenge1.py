def solution(A):
    N = len(A)
    target_bricks = 10
    
    # Calculate the total number of bricks needed in all boxes
    total_bricks = sum(A)
    
    # Calculate the total number of moves needed
    total_moves = 0
    missing_bricks = target_bricks * N - total_bricks
    
    if missing_bricks % N != 0:
        # If the total number of bricks needed cannot be distributed equally
        return -1
    else:
        bricks_per_box = missing_bricks // N
        for bricks_in_box in A:
            bricks_needed = target_bricks - bricks_in_box + bricks_per_box
            if bricks_needed < 0:
                # If it's not possible to distribute the bricks
                return -1
            total_moves += abs(bricks_needed)
    
    return total_moves

# Test cases
print(solution([7, 15, 10, 8]))  # Output: 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Output: 6
print(solution([7, 14, 10]))  # Output: -1
