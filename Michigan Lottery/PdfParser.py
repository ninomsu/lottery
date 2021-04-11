
#dowlonad from here: https://data.ny.gov/Government-Finance/Lottery-Mega-Millions-Winning-Numbers-Beginning-20/5xaw-6ayf/data
#dowlonad from here: https://data.ny.gov/Government-Finance/Lottery-Powerball-Winning-Numbers-Beginning-2010/d6yy-54nr
import os
import csv
import matplotlib.pyplot as plt
import numpy
import datetime
import numpy as np

class LotteryNumber:
    def __init__(self): 
        self.lotteryName = "n/a"
        self.dateDrawn = "n/a"
        self.numbers = []
    
    def Print(self): 
        print(f"Lottery: {self.lotteryName}, Date Drawn: {self.dateDrawn}, Winning Numbers: {self.numbers}")

class Container:
    def __init__(self, number, count):
        self.number = number
        self.count = count
    
    def __lt__(self, other):
         return self.count < other.count
    
    def Print(self):
        print(f"{self.number} occured { self.count} times")


def readData():
    val = []
    arr = os.listdir()
    for f in arr:
        if ".csv" in f:
            with open(f) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                nameOfLottery = "n/a"
                if "mega" in f.lower():
                    nameOfLottery = "Mega Millions"
                elif "power" in f.lower():
                    nameOfLottery = "PowerBall"
                for row in csv_reader:
                    if line_count == 0:
                        print(f'Column names are {", ".join(row)}')
                        line_count += 1
                    else:

                        lotteryNumb = LotteryNumber()
                        date = row[0].split("/")
                        lotteryNumb.dateDrawn = datetime.datetime(int(date[2]), int(date[0]), int(date[1])) #year, month, day
                        lotteryNumb.lotteryName = nameOfLottery
                        for numb in row[1].split(" "):
                            lotteryNumb.numbers.append(int(numb))
                        line_count += 1
                        val.append(lotteryNumb)
                print(f'Processed {line_count} lines.')
    return val

def GraphData(allNumbs,allDates):
    plt.scatter(allDates, allNumbs)
    plt.xlabel('Year')
    plt.ylabel('Number')
    plt.show()

def getCountOfNumbers(allNumbs):
    a = numpy.array(allNumbs)
    unique, counts = numpy.unique(a, return_counts=True)
    pairs = dict(zip(unique, counts))
    containers = []
    for key, value in pairs.items():
        tmp = Container(key, value)
        containers.append(tmp)
    
    containers.sort()

    for container in containers:
        container.Print()

def plotSinWave(alldates):
    # Get x values of the sine wave
    time = np.arange(0, 10, 0.1)
    # Amplitude of the sine wave is sine of a variable like time
    amplitude = np.sin(alldates)
    # Plot a sine wave using time and amplitude obtained for the sine wave
    plt.plot(time, amplitude)
    # Give a title for the sine wave plot
    plt.title('Sine wave')
    # Give x axis label for the sine wave plot
    plt.xlabel('Time')
    # Give y axis label for the sine wave plot
    plt.ylabel('Amplitude = sin(time)')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()
    # Display the sine wave
    plt.show()

def main():
    LotteryNumbers = []
    LotteryNumbers = readData()
    #for numb in LotteryNumbers:
    #    numb.Print()

    allNumbs = []
    allDates = []
    for numb in LotteryNumbers:
        for winner in numb.numbers:
            allNumbs.append(winner)
            allDates.append(numb.dateDrawn)

    getCountOfNumbers(allNumbs)
    
    testDates = [] 
    for test in allDates:
        testDates.append(np.datetime64(test))
    GraphData(allNumbs,allDates)
    #plotSinWave(testDates)
if __name__ == "__main__":
    # calling the main function
    main()