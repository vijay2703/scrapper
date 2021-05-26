#
# def printSubSequences(STR, lst,subSTR=""):
#
#     if len(STR) == 0:
#         a=(subSTR)
#         lst.append(a)
#         return
#
#     printSubSequences(STR[:-1],lst, subSTR + STR[-1])
#
#     printSubSequences(STR[:-1],lst, subSTR)
#     return lst
#
# def decimalToBinary(n):
#     return bin(n).replace("0b", "")
#
# def main():
#     """
# 	main function to drive code
# 	"""
#     STR = "1001011"
#     lst=[]
#     printSubSequences(STR,lst)
#
#     for i in range(1,1000000):
#         if(decimalToBinary(i) not in lst):
#             print(decimalToBinary(i))
#             break
#     print (lst)
#
#
# if __name__ == "__main__":
#     main()

# by itsvinayak

def decimalToBinary(n):
    return bin(n).replace("0b", "")

# # Driver code
# if __name__ == '__main__':
#     print(decimalToBinary(8))
#     print(decimalToBinary(1800000))
#     print(decimalToBinary(7))
import itertools


def Sub_Sequences(STR,lst):
    combs = []
    for l in range(1, len(STR) + 1):
        combs.append(list(itertools.combinations(STR, l)))
    for c in combs:
        for t in c:
            a=(''.join(t))
            lst.append(a)


# Testing with driver code
if __name__ == '__main__':
    lst=[]
    Sub_Sequences('1001011',lst)
    for i in range(1, 1000000):
        if(decimalToBinary(i) not in lst):
            print(decimalToBinary(i))
            break