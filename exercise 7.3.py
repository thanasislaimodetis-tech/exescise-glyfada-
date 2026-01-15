

import timeit

def find_best_path_rec(x, y, grid, memo=None):
   
   
    if memo is None:
        memo = {}
        
    
    if (x, y) in memo:
        return memo[(x, y)]
    
   
    if x < 0 or y < 0:
        return 0

    
    current_value = grid.get((x, y), 0)

    
    if x == 0 and y == 0:
        return current_value

 
    
    score_from_left = -1
    score_from_up = -1
    
   
    if x > 0:
        score_from_left = find_best_path_rec(x - 1, y, grid, memo)
        

    if y > 0:
        score_from_up = find_best_path_rec(x, y - 1, grid, memo)
        
 
    best_previous = max(score_from_left, score_from_up)
    

    total_score = current_value + best_previous
    
 
    memo[(x, y)] = total_score
    return total_score


def find_best_path(grid):
 

    width, height = grid["size"]
    
 
    return find_best_path_rec(width - 1, height - 1, grid)



if __name__ == "__main__":

    grid1 = {
        "size": (5, 5),
        (1, 0): 1, (1, 1): 3, (1, 2): 2, (1, 3): 3,
        (2, 2): 2, (2, 3): 1, (4, 2): 2
    }
    print(f"Test 1 Result: {find_best_path(grid1)}")
    
    grid2 = {
        "size": (5, 6),
        (1, 0): 1, (1, 1): 3, (1, 2): 2, (1, 5): 3,
        (2, 0): 2, (2, 1): 3, (2, 2): 2, (2, 3): 1,
        (3, 1): 3, (3, 5): 2, (4, 1): 3, (4, 3): 2
    }
    print(f"Test 2 Result: {find_best_path(grid2)}")


    print("\nRunning efficiency test...")
    large_grid = {"size": (99, 99)}

    large_grid[(1,0)] = 1
    large_grid[(98,98)] = 3
    
    start_time = timeit.default_timer()
    result = find_best_path(large_grid)
    end_time = timeit.default_timer()
    
    print(f"Large Grid Result: {result}")
    print(f"Time taken: {end_time - start_time:.5f} seconds")
    
    if (end_time - start_time) < 1.0:
        print("SUCCESS: Efficiency test passed!")
    else:
        print("FAIL: Too slow!")