# r/dailyprogrammer 
# easy #379
# Progressive taxation
# https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/
# write program that calculate tax


def tax(income):

    '''
    If your income is less than ¤10,000, you owe 0 income tax.

    If your income is between ¤10,000 and ¤30,000, you owe 10% income tax on the income that exceeds ¤10,000.\ 
    For instance, if your income is ¤18,000, then your income in the 10% bracket is ¤8,000.\ 
    So your income tax is 10% of ¤8,000, or ¤800.

    If your income is between ¤30,000 and ¤100,000,\
    then you owe 10% of your income between ¤10,000 and ¤30,000, plus 25% of your income over ¤30,000.

    And finally, if your income is over ¤100,000, then you owe 10% of your income from ¤10,000 to ¤30,000,\
    plus 25% of your income from ¤30,000 to ¤100,000, plus 40% of your income above ¤100,000.
    '''

    p1 = ((income - 10000) * 0.10)
    p2 = ((20000 * 0.10) + ((income - 30000) * 0.25))
    p3 = ((20000 * 0.10) + ((100000 - 30000) * 0.25)+ ((income - 100000) * 0.40))
    
    if income in range(10000, 30000):
        print(int(p1))
    elif income in range(30000, 100000):
        print(int(p2))
    elif income > 100000:
        print(int(p3))
    else:
        print(0)




tax(0)
tax(10000)
tax(10009)
tax(10010)
tax(12000)
tax(56789)
tax(1234567)