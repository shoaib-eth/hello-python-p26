file = open("youtube.txt", "w")

try:
    file.write("This is a YouTube manager project.")
finally:
    file.close()
    
# Another way to do the same thing but with a context manager, which automatically handles closing the file even if an error occurs 
with open("youtube.txt", "w") as file:
    file.write("This is a YouTube manager project.")
