# Puzzle: Sum of Squares
# Link: https://www.janestreet.com/puzzles/sum-of-squares-index/
# Images: https://www.janestreet.com/puzzles/niedermaier1.png

# Place a digit in each of the 25 spots in the below 5×5 grid, so that each 5-digit number (leading zeroes are ok) reading across and reading down is divisible by the number outside the grid, trying to maximize the sum of the 25 numbers you enter. An example of a completed grid with sum 100 is presented on the right.
# Please submit your answer (along with any other comments you want to provide) as an ordered pair of your sum, and your 25 numbers, reading left to right, top to bottom.
# Example submission: (100,1623552460048932486847030)

##############################################
##############################################

# A || B || C || D || E  | 1
# F || G || H || I || J  | 2
# K || L || M || N || O  | 3
# P || Q || R || S || T  | 4
# U || V || W || X || Y  | 5
# ==========================
# 6 || 7 || 8 || 9 || 10 | #

# Conditions:
# - Y has to be 0; any number divisible by both 5 and 10 has to end in 0.
# - J, T, U, W have to be even; those lines divisible by even numbers.

# Steps:
# 1. Create an array with all possible 5-digit values [00000, ..., 99999]
# 2. Use this list to filter out rows and columns divisible by [6,7,8,9,10] and by the previous listed conditions.
# 3. Select a value from each array to create new numbers via the index of the selected and check if they're divisible by 1,2,3,4,5.
# 4. If not, change a value and try again. Iterate through until we get a match.

##############################################
##############################################

import itertools

# This is a function to calculate the sum of all the digits in an array.
def sum_of_digits(list):
    digits = [int(digit) for digit in str(list)]
    return sum(digits)

# An array that contains all values from 0 to 99999, with zeroes filled in for numbers that are not 5 digits ie. 1 becomes 00001.
all_vals = [str(i).zfill(5) for i in reversed(range(100000))]

# Multiple functions are executing for each of the five lines below:
# 1. The square brackets are a list comprehension where it is filtering out values divisible by 6-10 from the all_vals list.
# 2. The sorted function uses the sum_of_digits function. This will sort the array according to the sum of the respective digits.
# 3. The reverse=True will revert the sorting from ascending to descending, giving us the larger sum of digits at the top.
div6_vals = sorted([i for i in all_vals if int(i) % 6 == 0], key=sum_of_digits, reverse=True)
div7_vals = sorted([i for i in all_vals if int(i) % 7  == 0], key=sum_of_digits, reverse=True)
div8_vals = sorted([i for i in all_vals if int(i) % 8  == 0], key=sum_of_digits, reverse=True)
div9_vals = sorted([i for i in all_vals if int(i) % 9  == 0], key=sum_of_digits, reverse=True)
div10_vals = sorted([i for i in all_vals if int(i[4]) == 0], key=sum_of_digits, reverse=True)

# The n determines the first n values we will be iterating through from each list.
# As this number gets larger, the number of combinations increases exponentially.
# This means with a value of 5, the all_combos will contain 5^5 = 3,125 combinations of the five largest values from each list.
n = 30
print("making " + str(pow(n,5)) + " combos..")
all_combos = [[a,b,c,d,e] for a in itertools.islice(div6_vals, n) for b in itertools.islice(div7_vals, n) for c in itertools.islice(div8_vals, n) for d in itertools.islice(div9_vals, n) for e in itertools.islice(div10_vals, n)]

print("finished creating a list of all combos, length: " + str(len(all_combos)))
# The max_val and max_list will hold the largest sum of the digits and their corresponding array that satisfies our conditions.
max_val = 0
max_list = []

# We will loop through the all_combos list to check for each one if they are divisible by their respective row.

for x in all_combos:
    if sum([sum_of_digits(i) for i in x]) > max_val:
        div1_int = int(x[0][0] + x[1][0] + x[2][0] + x[3][0] + x[4][0])
        div2_int = int(x[0][1] + x[1][1] + x[2][1] + x[3][1] + x[4][1])
        div3_int = int(x[0][2] + x[1][2] + x[2][2] + x[3][2] + x[4][2])
        div4_int = int(x[0][3] + x[1][3] + x[2][3] + x[3][3] + x[4][3])
        div5_int = int(x[0][4] + x[1][4] + x[2][4] + x[3][4] + x[4][4])

        total_val = sum_of_digits(div1_int) + sum_of_digits(div2_int) + sum_of_digits(div3_int) + sum_of_digits(div4_int) + sum_of_digits(div5_int)

        # If it is true, the values are saved and printed.
        # If we hit the same value of the sum of digits, it will skip until we find a higher sum.
        if div1_int % 1 == 0 and div2_int % 2 == 0 and div3_int % 3 == 0 and div4_int % 4 == 0 and div5_int % 5 == 0 and total_val > max_val:
            max_val = total_val
            max_list = str(x)
            print(max_list, max_val)

print("end of script.")
print(max_list, max_val)

# Once we get a large n, we can iterate through millions of combinations to get the biggest value. 

# Problems with this function:
# - Currently this function runs very slowly, mainly due to the all_combos array generation.
# - If we want to get the true maximum sum of digits, we would need to iterate through them all.
# - By increasing the value of n to the maximum, This will take a VERY long time.
# - If we created a combo list of the largest 1000 values from each list, and it took one second per 1000 combinations, it would take 31,709.8 years.

# Optimising:
# - Instead of directly creating the all_combos list, we could just create a function to iterate through the combos and check if they are divisible by 1,2,3,4,5.
# - Additionally, we could calculate the sum of the digits in real time and not consider any that are less than or equal to our current max value.
