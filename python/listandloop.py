InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "MovieName":
    "Spider-Man: No Way Home",
    "MovieYear":
    "2021",
    "Rating":
    "5",
    "Actors": [
        "Tom Holland", "Tobey Maguire", "Zendaya", "Andrew Garfield",
        "Marisa Tomei"
    ]
})

InfoDb.append({
    "MovieName":
    "Star Wars: The Force Awakens",
    "MovieYear":
    "2015",
    "Rating":
    "4",
    "Actors": ["Daisy Ridley", "John Boyega", "Harrison Ford", "Adam Driver"]
})

InfoDb.append({
    "MovieName":
    "Toy Story",
    "MovieYear":
    "1995",
    "Rating":
    "5",
    "Actors": ["Tom Hanks", "Laurie Metcalf", "Ernie Sabella", "Nathan Lane"]
})


def print_data(n):
    print("Movie Name:", InfoDb[n]["MovieName"], "Year:", InfoDb[n]["MovieYear"], "Rating: ",InfoDb[n]["Rating"]  )  # using comma puts space between values
    print("\t", "Actors in the movie: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Actors"]))  # join allows printing a string list with separator
    print()


def tester():
    print("for_loop_limit:")
    for_loop_limit(1,2)
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion


# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def for_loop_limit(start, end):
    for n in range(start, end+1):
        print_data(n)
      
# while loop contains an initial n and an index incrementing statement (n += 1)
# dont need to write n = 0 because it being called in the tester
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

if __name__ == "__main__":
  tester()
