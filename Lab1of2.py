# Quiz: Calculate
# In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling.
# One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

# 1. How many tiles are needed?
# 2. You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?


# Fill this in with an expression that calculates how many tiles are needed.

floor_1 = 9 * 7   # Area of Floor 1
floor_2 = 5 * 7   # Area of Floor 2
tiles_needed = floor_1 + floor_2    # Total required Tiles for the job
print("\nThe number of tiles needed is: ", tiles_needed)

# Fill this in with an expression that calculates how many tiles will be left over.

total_tiles = 17 * 6      # Finding the total tiles available for the job
left_over = total_tiles - tiles_needed    # Finding the number of tiles leftover after tiling.
print("\nThe Left-over Tiles are: ", left_over)
