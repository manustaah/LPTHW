print "It's late at night and you woke up from a loud noise coming from downstairs. What do you do? #1 : Stay upstairs and wait #2 : Go downstairs and investigate"

act = raw_input("> ")

if act == "1":
        print "You hear another loud sound coming from downstairs. Someone is in your house! What now?"
        print "1. You stay in your Bedroom, the noise could be coming from outside."
        print "2. You go downstairs."

if act == "2":
    print " You leave your room and as you enter your upstairs hallway you hear another loud sound coming from downstairs. Someone is in your house! What now?"
    print "1. You go back into your Bedroom"
    print "2. You go downstairs."

someone = raw_input("> ")

if someone == "1":
                print "The noise is clearly not coming from outside. Someone is in your house! Hide!"
                print "1. Hide in the closet."
                print "2. Hide under the bed."

elif someone == "2":
                print "You walk downstairs and reach the downstairs hallway. Straight across from you is the frontdoor but to get to it you have to pass the door to the kitchen. What do you do? "
                print "1. You try to reach the frontdoor."
                print "2. You go back upstairs"

frontdoor = raw_input("> ")

if frontdoor == "1":
                print "As quietly as you can you walk passed the kitchen but the intruder sees you."
                print "The intruder finds and kills you! Sorry"

if frontdoor == "2":
                print "You go back into your room and are looking for a hiding spot. You pick the closet."
                print "Press 1 to hide in the closet."

hide = raw_input("> ")

if hide == "1":
                 print "You hide in the closet and try to be really quiet. After a few seconds you realize that your phone is in your office across the hall. You leave your closet and go into the hallway but you're too scared. Go back to your room!"
                 print "Press 1 to go back to your room."
else:
                 dead("The intruder finds you and kills you")


downstairs = raw_input("> ")

if downstairs == "1":
        print "Back in your room you're searching for your phone to call the police but you realise that you left it in your office across the hall. Do you want to risk going over there and might be heard by the intruder? "
        print "1. Try to go into the office to get the phone"
        print "2. Stay in your bedroom and hide."

if downstairs == "2":
             print "As quiet as you can you leave your room and walk into the upstairs hallway. You can hear now clearly that someone is downstairs. You hear steps and the opening of drawers in your kitchen. You're almost at your office until you trip over one of your shoes in you left in the hallway. You don't fall but you made some noise. You hear that the noises from the kitched stopped. What do you do? "
             print "1. You run as fast as you can back to your room and hide inside your closet."
             print "2. As quietly as you can you walk towards the office to get your phone."


office = raw_input("> ")

if office == "1":
                        print "You walk into the upstairs hallway to go to your office. You left your shoes in the hallway and you fall over them and make a lot of noise. What should you do?"
                        print "1. You get up and run into the office."
                        print "2. You get up and run back into your bedroom."

elif office == "2":
        print "You run back to your room and hide in the closet.You try to catch your breath and be as quiet as you can. You hear footsteps. Someone is coming up your stairs! What do you do?"
        print "1.You stay were you are being as quiet as you can."
        print "2.You get out and try to fight the guy."


hallway = raw_input("> ")

if hallway == "1":
    print "You reach your office and there is your phone. As you try to dial 911 you realize that your phone is dead. What do you do?"
    print "1.Try to run back into your bedroom"
    print "2.Stay in the office."

elif hallway == "2":
    print "You get out of the closet and see the guy coming into your room. You attack him but you didn't see the gun he was holding. What do you do? "
    print "1. Try to get the gun from the intruder."
    print "2. Run for your life."



noise = raw_input("> ")

if noise == "1":
        print "You go back into your room and hide in the closet. You try to catch your breath and be as quiet as you can. You hear footsteps. Someone is coming up your stairs! What do you do?"
        print "1. You stay in the closet and hope he doesn't find you."
        print "2. You leave the closet and try to find something to protect yourself from the intruder."

elif noise == "2":
    print "You walk downstairs and reach the downstairs hallway. Straight across from you is the frontdoor but to get to it you have to pass the door to the kitchen. What do you do? "
    print "1. You try to reach the frontdoor."
    print "2. You take the door to your left leading into the basement. Maybe you can climb out the basement window."

footsteps = raw_input("> ")

if footsteps == "1":
        print "You're in your closet and you hear footsteps coming towards your room. He is coming closer! What do you do?"
        print "1. You stay in the closet and hope he doesn't find you."
        print "2. You leave the closet and try to find something to protect yourself from the intruder."

elif footsteps == "2":
    print " You get out of the closet and look around your room. All you have to defend yourself are a Bottleopener and your lamp from your nightstand. Which one do you choose?"
    print " 1. Bottleopener"
    print " 2. Lamp"

weapon = raw_input("> ")

if weapon == "1":
        print "The intruder stands in front of you. You take the Bottleopener and ram it into his head. "
        print "Congrats, he's dead and you are not."

elif weapon == "2":
        print "The intruder stands in front of you. You take the lamp and hit him over his head with it."
        print "He is still standing and is not impressed."
        print "He kills you. Sorry."

intruder = raw_input("> ")

if intruder == "1":
        print "You hear him in your room. He is looking for you."
        print "You hold your breath....You hear him coming towards the closet.."
        print "HE GOT YOU! you're dead. Sorry."
elif intruder == "2":
        print "You walk downstairs and reach the downstairs hallway. Straight across from you is the frontdoor but to get to it you have to pass the door to the kitchen. What do you do? "
        print "1. You try to reach the frontdoor."
        print "2. You take the door to your left leading into the basement. Maybe you can climb out the basement window."
