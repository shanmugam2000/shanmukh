book = []
count = int(input("Enter number of books"))
for i in range(0, count):
    bookname = input("Enter the book name")
    aname = input("Enter the author name")
    size = input("Enter the size")
    publisher = input("enter publisher")
    details = {"Bookname" : bookname, "Author name" : aname, "Size of book" : size, "Publisher" : publisher}
    book.append(details)

print(book)