again = "yes"

while again == "yes":
    praiseType = raw_input("Select a type of praise \n a: personality \n b: appearance \n c: intelligence \n Your selection: ")
    if praiseType == "a":
        print "You are funny, because your life is a joke. Gaster is better."

    elif praiseType == "c":
        print "You are nowhere near as intelligent as Doctor W.D. Gaster, \n The Royal Scientist. Why even try to beat him?"

    elif praiseType == "b":
        print "Your complexion will never match the snow white bone of W.D. And that is with \n his scars, fool."

    else:
        print "That was not even an existing option. Are you that dumb? Gaster is smarter."

again = raw_input("Would you like some more praise?")
