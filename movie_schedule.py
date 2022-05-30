current_movies = {
    "ABC":"11:00",
    "XYZ":"1:00",
    "ABCD":"4:00",
    "A123":"8:00"
}
print("These movies are running now:",current_movies)

for key in current_movies:
    print(key)
movie = input("whaich movie you want to watch")
time=current_movies.get(movie)
if time ==None:
    print("Movie is not found")
else:
    print(movie +" is playing at "+time)
    print(movie ," is playing at ",time)


    