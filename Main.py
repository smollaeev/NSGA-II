from solution import Solution

def main():
    numberOfGenerations = 100
    numberOfIndividuals = 60
    solution = Solution ()
    solution.NSGA (numberOfGenerations, numberOfIndividuals)

if __name__ == "__main__":
    main()