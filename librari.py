import time
time.sleep(1)
print("hello")
time.sleep(2)
print("welcome to our library")
print("these are the books we have")
time.sleep(2)
bookmanage={
    "the tortoise and the hare",
    "diary of a wimpy kid",
    "captain under pants"
}
print(bookmanage)

print("do you  want to borrow a book?")
a = input("which book do you want to borrow? " )
time.sleep(2)
b = input("what is your name?"  )
print("the book that has been borrowed is  " + a)
print(b+ " when are you borrwing this book " +a)
c = input("input the day you are borrowing this book "  )
time.sleep(2)

print("when are you retuning the book " +a)
d = input("input the day ")

print("you are borrowed " + a + " on " + c + " and retuning it on " + d )
print("thankyou for visting us goodbye")
