import os; import time; import re

byteList = []

def operate():
    with open(filePath, "rb") as inputFile:
        for line in inputFile:
            byteList.append(line)

    if (operation == "1"):
            byteList.insert(-1, b'\r\n')

    length = len(byteList)
    half = length // 2

    with open(output, "wb") as outputFile:
        for element in byteList[half::-1]:
            outputFile.write(element)
        for element in byteList[:half:-1]:
            outputFile.write(element)


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def outputFileName():
        try:
            outputMatch = re.search(r"(.+)[$\.].+", filePath)
            output = str(outputMatch[1])
            extensionMatch = re.search(r".+[$\.](.+)", filePath)
            extension = str(extensionMatch[1])
        except:
            output = filePath
            extension = ""

        if (operation == "1"):
            output += " [Scrambled]." + extension
        elif (operation == "2"):
            output += " [Unscrambled]." + extension
        return(output)


############### Main ###############

if __name__ == "__main__":

    try:

        while (True):
            print("Operations:-")
            print("1. Scramble a file\n2. Unscramble a file")
            operation = input("\nSelect operation number: ")
            if (operation in ["1", "2"]):
                while (True):
                    filePath = input("\nEnter file path: ")
                    if (os.path.isfile(filePath) is True):
                        break
                    else:
                        clrscr()
                        print("\nEither file does not exist or invalid path entered. Try again.")
                        continue
                clrscr()
                output = outputFileName()
                print("\nWorking...", end='')

                start = time.time()
                operate()
                break
            else:
                clrscr()
                print("\nInvalid entry. Choose either option 1 or 2. Try again.\n")
                continue

        completionTime = time.time() - start

        clrscr()
        print(f"\nThe task completed successfully in {completionTime} seconds.")
        print("Press Enter to exit. GG;WP.")
        input()
    except KeyboardInterrupt:
        clrscr()
        print("\nCTRL ^C\n\nThrew a wrench in the works.")
        print("Press Enter to exit.")
        input()
