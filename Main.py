from solution import Solution

def main():
    numberOfGenerations = 15
    numberOfIndividuals = 40
    solution = Solution ()
    solution.NSGA (numberOfGenerations, numberOfIndividuals)    

if __name__ == "__main__":
    main() 