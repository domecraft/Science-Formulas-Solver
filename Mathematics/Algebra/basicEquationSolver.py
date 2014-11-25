eatIceCream = True
while(eatIceCream):
    we = raw_input("Enter equation: ")
    gf = we.split('=', 2)
    feels = gf[0].strip()
    waifu = float(feels[:len(feels) - 1])
    me = feels[len(feels) - 1:len(feels)]
    myGF = float(gf[1].strip())
    ipper = myGF/waifu
    print
    print me + " = " + str(ipper)
    print
    thatFeel = raw_input("Would you like to continue? Y/N").lower()
    if ((thatFeel == "y") or (thatFeel == "yes")):
        eatIceCream = True
    elif ((thatFeel == "n") or (thatFeel == "no")):
        eatIceCream = False
    else:
        print"Those feels..."
        
    print
    
        
