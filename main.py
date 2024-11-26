# gets data set from user and converts it to a list of floats
def getDataSet():
  while True:
# separates the numbers in the data set by spaces
    try:
      dataSet = input("Enter a dataset separated by spaces:").split()
# converts the data set to a list of floats
      dataSet = [float(num) for num in dataSet]
      return dataSet
# validates user input
    except ValueError:
      print("Invalid input.")
      
# gets calculation choice from user
def getCalculationChoice():
  while True:
    try:
      calculationChoice = int(input("What would you like to calculate?\n1. Sum\n2. Average\n3. Minimum\n4. Maximum\nEnter a number (1-4):"))
# validates user input
      if 1 <= calculationChoice <= 4:
        return calculationChoice
      else:
        print("Invalid choice.")
    except ValueError:
      print("Invalid input.")

# performs the calculation based on the user's choice
def performCalculation(dataSet, calculationChoice):
# calculates the sum of the data set
  if calculationChoice == 1:
    dataSum = sum(dataSet)
    print("Sum:", dataSum)
# calculates the average of data set
  elif calculationChoice == 2:
    dataAvg = sum(dataSet) / len(dataSet)
    print("Average:", dataAvg)
# finds the minimum value in the data set
  elif calculationChoice == 3:
    dataMin = min(dataSet)
    print("Minimum:", dataMin)
# finds the maximum value in the data set
  elif calculationChoice == 4:
    dataMax = max(dataSet)
    print("Maximum:", dataMax)

# asks user if they want to continue with the same data set
def userContinue():
  while True:
    nextAction = input("Would you like to perform another calculation? (y/n):")
# vaidates user input
    if nextAction.lower() in ["y", "n"]:
      return nextAction.lower() == "y"
    else:
      print("Invalid choice.")

# main program loops until user chooses to exit
def main():
  while True:
    dataSet = getDataSet()

    while True:
      calculationChoice = getCalculationChoice()
      performCalculation(dataSet, calculationChoice)
# exits program
      if not userContinue():
        print("Exiting calculator. Goodbye.")
        exit()
# calls the main function to start the program
if __name__ == "__main__":
  main()