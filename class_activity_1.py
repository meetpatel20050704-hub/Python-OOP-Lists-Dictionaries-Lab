class MovieWatchlist:
    def __init__(self):
        self.__movies = []

    def addMovie(self, title, genre, rating):
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }

        self.__movies.append(movie)
        print(f'"{title}" has been added to your watchlist!')

    def displayMovies(self):
        if len(self.__movies) == 0:
            print("\nNo movies found in the watchlist.")
        else:
            print("\n===== MOVIE WATCHLIST =====")

            for movie in self.__movies:
                print(f"Title : {movie['title']}")
                print(f"Genre : {movie['genre']}")
                print(f"Rating: {movie['rating']}/10")
                print("--------------------------")

    def searchMovie(self, title):
        found = False

        for movie in self.__movies:
            if movie["title"].lower() == title.lower():
                print("\nMovie Found!")
                print("--------------------------")
                print(f"Title : {movie['title']}")
                print(f"Genre : {movie['genre']}")
                print(f"Rating: {movie['rating']}/10")
                print("--------------------------")
                found = True
                break

        if not found:
            print("\nMovie not found.")

    def countMovies(self):
        return len(self.__movies)


# Create object
watchlist = MovieWatchlist()

# Ask user how many movies to add
number_of_movies = int(input("How many movies do you want to add? "))

# Add movies
for i in range(number_of_movies):
    print(f"\nEnter details for Movie {i + 1}")

    title = input("Enter movie title: ")
    genre = input("Enter movie genre: ")
    rating = float(input("Enter movie rating (out of 10): "))

    watchlist.addMovie(title, genre, rating)

# Display all movies
watchlist.displayMovies()

# Search movie
search_title = input("\nEnter movie title to search: ")
watchlist.searchMovie(search_title)

# Count movies
print("\nTotal movies in watchlist:", watchlist.countMovies())