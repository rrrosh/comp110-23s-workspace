"""Knock Knock Joke with Conditionals"""

inter_cow: str = input("Do you want an interrupting cow? ")
print("Knock Knock ")
if inter_cow:
    print("... who's there?")
    print("Interrupting cow.")
    print("... interrupting cow wh---")
    print("MOO!!!")
else: 
    print("oh... ok... :(")
    if (inter_cow == "you're not funny"):
        print("wow my feelings are hurt")