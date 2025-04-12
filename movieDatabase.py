# Project: Create a Movie Database
# Build a program that lets the user input details of a movie (like title, release year, genre). Store this information in a list of tuples.

import sys
movies = []

# OBJECTIVE 1) Create a function to display all movies.
def movieDisplay():
    for movie in movies:
        print (f"Title: " + movie[0] + " | Release Year: " + movie[1] + " | Genre: " + movie[2])









# OBJECTIVE 2) Create a function that searches for movies by name.
######################################## ERROR ###############################################################
"""def movieSearch(releaseYear, genre):
    for movie in movies:
        if releaseYear == movie[1] and genre == movie[2]:
                return (f"\nTitle: " + movie[0] + " | Release Year: " + movie[1] + " | Genre: " + movie[2])"""












# OBJECTIVE 3) Create a function that adds a movie to the database
def addMovie():
    while True:
        title = input("Please enter the title of your movie: ").title().strip()
        releaseYear = str(input("Please enter the release year of this movie: ")).strip()
        genre = input("Also what is the genre of this movie? : ").title().strip()
        movie1 = (title, releaseYear, genre)
        movies.append(movie1)
        movies.sort(key= lambda movie1: movie1[1])                          # OBJECTIVE 3) Implement sorting of the movies based on release year.
        print (f"Thank you, movie has been added to the database\n")
        return movies


# MAIN PROGRAM LOOP - MAIN MENU
while True:
    print (f"\nYou have three options - \n")
    print ("Option 1: Search for specific movies in the database.")
    print ("Option 2: Take a look at all the movies in the entire database.")
    print ("Option 3: Add another movie to the database.")
    print ("(Enter blank input to exit the program).")
    optionChoice = input(f"\nPlease choose your option: ").lower().strip()


 # MOVIE SEARCH - OPTION 1
    if optionChoice == 'option 1':
        if len(movies) == 0:
            print (f"List is empty, please update the database first.")
            continue
        else:
            genre1 = input("Enter the genre of the movie you're looking for: ").title().strip()
            releaseYear1 = int(input("Enter the release year of the movie you're looking for: ").strip())
            movieSearch(genre1, releaseYear1)


# MOVIE DISPLAY - OPTION 2
    elif optionChoice == 'option 2':
        if len(movies) == 0:
            print ("List is empty, please update the database first")
            continue
        else:
            movieDisplay()


# APPENDING MOVIES - OPTION 3
    elif optionChoice == 'option 3':
        addMovie()

# SYSTEM EXIT OPTION
    elif optionChoice == '':
        sys.exit("Exiting...")

# ERROR HANDLING    
    else:
        print("Please enter 'option 1', 'option 2', 'option 3' or a blank key (exact format).")
        continue



#   PROBLEMS
# - For movie search, the function doesn't filter out specific movies based on its parameters.