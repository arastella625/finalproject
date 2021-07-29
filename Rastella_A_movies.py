# Name:        Amber Rastella
# Class:       CSC 110 - Summer 2021
# Assignment:  Programming Project Implementation
# Due Date:    July 30, 2021

# Program Title:  Movies Data
  
# Project Description:
# --------------------
# This program is going to take information from a data file about movies that
# were released between 2000 and 2009 and display that information based on a
# choice that the user will be allowed to input.

# General Solution:
# -----------------
# Will very much have to use modular design as there will be 7 different questions
# that the user will have available to them as choices. Each question will require
# its own function minimally that will then get called together in a main
# function. 

# Pseudocode:
# -----------
# User will enter name of data file
#   If it is incorrect
#       Use exception handling to get a new name for the file
# Display all options for the user
# User inputs option choice
# While the choice is not 8
#   If choice is the same as (numbers 1-7)
#       Call appropriate function
#   Else
#       print "Error in your choice"


# Function Design:
# ----------------


def openFile():
    # This function will be the exception handling for inputting the data
    # file name

    goodFile = False
    while goodFile == False:
        fname = input("Enter name of the file: ")
        try:
            movieData = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid filename, please try again...")
    return movieData

 

def getData():
    # This function will get all the data from the file and put them into lists

    dataFile = openFile()

    titleList = []
    genreList = []
    runTimeList = []
    ratingList = []
    studioList = []
    yearList = []

    count = 0
    for line in dataFile:
        
        temp = line.split(",")
        count += 1
        if (len(temp) == 6):
            titleList.append(temp[0])
            genreList.append(temp[1])
            runTimeList.append(temp[2])
            ratingList.append(temp[3])
            studioList.append(temp[4])
            yearList.append(temp[5])

    dataFile.close()

    return titleList, genreList, runTimeList, ratingList, studioList, yearList    

def allFilmsbyStudio(titleList, genreList, runTimeList, ratingList, studioList, yearList):
    # This function takes seven parameters (all the information of movies) and
    # will display all the movies for the user all the information about films made by a chosen
    # studio

    goodName = False
    while goodName == False:
        try:
            studioName = input("Enter studio name: ")
            goodName = True
        except:
            print("That studio name cannot be found. Please try again.")


    for x in range(len(studioList)):
        
        if studioName == studioList[x]:
            print("")
            print(titleList[x].ljust(40), genreList[x].ljust(14),runTimeList[x].ljust(5),ratingList[x].ljust(8),studioList[x].ljust(25),yearList[x].ljust(4))
    
   

def longestFilm_by_Genre(genreName, titleList, genreList, runTimeList, ratingList, studioList, yearList):
    # This function will take seven parameters and will return
    # the information of the longest film in a specific genre that will
    # be inputted by the user
    
    genre = []
    title = []
    runtime = []
    rating = []
    studio = []
    year = []
    for x in range(len(genreList)):

        if genreName == genreList[x]:
            genre.append(genreList[x])
            title.append(titleList[x])
            runtime.append(runTimeList[x])
            rating.append(ratingList[x])
            studio.append(studioList[x])
            year.append(yearList[x])
            
    n = len(runtime)
    for i in range(n):
        for j in range(n-i-1):
            if (runtime[j]>runtime[j+1]):
                genre[j],genre[j+1] = genre[j+1],genre[j]
                title[j],title[j+1] = title[j+1],title[j]
                runtime[j],runtime[j+1] = runtime[j+1],runtime[j]
                rating[j],rating[j+1] = rating[j+1],rating[j]
                studio[j],studio[j+1] = studio[j+1],studio[j]
                year[j],year[j+1] = year[j+1],year[j]
    print(f"{genre[0]},{title[0]},{runtime[0]},{rating[0]},{studio[0]},{year[0]}")
    return

def filmsInRange_and_Rating(rating, yearOne, yearTwo, titleList, genreList, runTimeList, ratingList, studioList, yearList):    
    # This option displays all information about films with a chosen
    # rating that were produced within a range of years chosen by the user.

    return


def film_by_Title(titleName, titleList, genreList, runTimeList, ratingList, studioList, yearList):
    # This function displays all information about the film with a specific title.
    for i in range(len(titleList)):
        if (titleName == titleList[i]):
            break
    print(f"{titleList[i]},{genreList[i]},{runTimeList[i]},{ratingList[i]},{studioList[i]},{yearList[i]}")
    return

def averageRuntime_by_Rating(ratingChoice, ratingList, runTimeList):
    # This option displays a single number representing the average runtime of
    # films with a rating specified by the user.

    return

def sort_by_year(titleList, genreList, runTimeList, ratingList, studioList, yearList):
    # This option sorts the lists by the year the films were produced and writes
    # the resulting sorted lists to a file.

    return

def mostFilmsProduced_by_Studio(titleList, studioList):
    # This function will find the studio that has produced the most films.
  
    
    

    return

def getChoice():
    # This function displays the menu of choices for the user
    # It reads in the user's choice and returns it as an integer
    
    print("")
    print("Make a selection from the following choices:")
    print("1 - Find all films produced by a certain studio")
    print("2 - Find the longest film of a specific genre")
    print("3 - Find all films made in a given year range with a specific rating")
    print("4 - Search for a film by title")
    print("5 - Find average runtime of films with a certain rating")
    print("6 - Sort all lists by year and write the results to a new file")
    print("7 - Find the studio that has produced the most films")
    print("8 - Quit")
    
    print("")
    
    checkChoice = False
    while checkChoice == False:
        try:
            choice = int(input("Enter your choice --> "))
            checkChoice = True
        except:
            print("Invalid integer. Please try again: ")
        

    return choice

def main():
    # The main function implements the pseudocode by using the functions defined above.

    titleList, genreList, runTimeList, ratingList, studioList, yearList = getData()

    choice = getChoice()
    while choice != 8:
        if choice == 1:
            allFilmsbyStudio(titleList, genreList, runTimeList, ratingList, studioList, yearList)
            choice = getChoice()
            
        elif choice == 2:
            while(True):
                try:
                    genreName = input("Enter genre: ")
                    break
                except:
                    print("That genre cannot be found. Please try again.")

            longestFilm_by_Genre(genreName, titleList, genreList, runTimeList, ratingList, studioList, yearList)
            choice = getChoice()
        elif choice == 3:
           
            choice = getChoice()
        elif choice == 4:
            while True:
                try:
                    titleName = input("Enter Title")
                    break
                except:
                    print("That Title cannot be found. Please try again.")
            film_by_Title(titleName, titleList, genreList, runTimeList, ratingList, studioList, yearList)
            choice = getChoice()
        elif choice == 5:
           
            choice = getChoice()
        elif choice == 6:
           
            choice = getChoice()
        elif choice == 7:
           
            choice = getChoice()
        else:
            print("Error in your choice")
            choice = getChoice()
    print("Good-bye")


main()
