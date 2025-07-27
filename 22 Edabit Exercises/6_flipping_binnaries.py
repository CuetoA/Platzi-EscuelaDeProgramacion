


def mysolution(n):
    """
    Did not work, size is not constrained to 32 and that results into multiple issues. It's to elaborate
    See proposed solution by others
    """
    bin_rep = bin(n)
    print(f"recieved: {bin_rep}")

    num = bin_rep[2:]
    new_num = []
    for i in range( len(num )):
        new_num.append( f"{abs( int(num[i]) -1 )}" )
    num = bin_rep[:2] + "".join(new_num)

    print(f"final:    {num}")
    print(f"final:    {int( num, 2 )}")

    return int( num, 2 )

    
def proposed_solution(n):
    max = 4294967295 
    return max - n




flipping_bits(1)
flipping_bits(4)