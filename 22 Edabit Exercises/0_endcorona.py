'''
Create a function that takes the number of daily average recovered cases recovers, daily average new_cases, current active_cases, 
and returns the number of days it will take to reach zero cases.

Examples
end_corona(4000, 2000, 77000) ➞ 39

end_corona(3000, 2000, 50699) ➞ 51

end_corona(30000, 25000, 390205) ➞ 79
Notes
The number of people who recover per day recovers will always be greater than daily new_cases.
Be conservative and round up the number of days needed.
'''


# OPTION 1. BRUTE FORCE
def end_corona(rec_cases, new_cases, curr_cases):

    day_counter = 0

    while curr_cases > 0:
        day_counter += 1
        curr_cases = curr_cases + new_cases - rec_cases

    return day_counter


# OPTION 2. SECOND WAY
def end_corona2(rec_cases, new_cases, curr_cases):
    net_recovery = rec_cases - new_cases

    if net_recovery <= 0:
        print(f"Corona may never end, net recovery cases is negative {net_recovery}")
        day_counter = -1
    else:
        day_counter = curr_cases / net_recovery
    
    return day_counter


## MAIN
print( end_corona(4000, 2000, 77000) )
print( end_corona(3000, 2000, 50699) )
print( end_corona(30000, 25000, 390205) )
        
print( end_corona2(4000, 2000, 77000) )
print( end_corona2(3000, 2000, 50699) )
print( end_corona2(30000, 25000, 390205) )