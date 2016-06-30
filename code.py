import sys
print 'Instructions\n Rating is from 1 to 10 .\n If you wanna try again you can input yes/no \n or a simple y/n'
def myScript():
        # Rate our Love!! 
    ###   Press F5
    ## then input a rating for our relationship so far
    love_rate = raw_input("Jacky,Type a rating for our relationship:")   
	### word answers
    idk = 'idk'
    no = 'no' 
    yes = 'yes' 
    lol = 'lol'
    smh = 'smh'
    love(love_rate)

def love(n):
        if n < 0 : 
            print "Why would it be negative?!" 
        elif n == 'yes' : 
            print " Well if that's the case, then I think we're gonna be just fine." 
        elif n == 'no' : 
            print 'well then... this is awkward'
        elif n == 'lol' : 
            print '''THATS NOT EVEN A NUMBER  
            
            
              ......sniff'''
        elif n == 'smh' :
            print "I'm kinda mad that's an answer you thought of putting here"      
        ## numbered entries 
        elif n == '0' : 
            print " *gasps profusely* YOU DON'T DESERVE THIS PROGRAM" 
        elif n == '1' :
            print "Wow that is kinda hurtful, not gonna lie" 
        elif n == '2' : 
            print "You make me smile at least once , I DESERVE BETTER"
        elif n == '3' : 
            print"you wouldn't believe how annoying it was to get this program to run properly!" + " Thats all i get?"
        elif n == '4' : 
            print "let's " + "shoot a little higher than that"
        elif n == '5' : 
            print "you're unforgettable, that's what you are" 
        elif n == '6' :
            print "always have, always '____?' *hint* fill in the blank " 
        elif n == '7' :
            print "I could never leave you, I love you too much" 
        elif n == '8' : 
            print "an 8/10 is still only a B, Ata KCSE haukupata B" 
        elif n == '9' : 
            print " well, I'm not perfect yet, could have seen that one coming. But do i see :)" 
        elif n == '10' : 
            print " Yaaaaaaas BITCH !!!!!!"     
        elif n == '11' : 
            print """"I knew your ass was cheeky enough to try 11 hihihi""" 
        elif n == '12' : 
            print "I don't think the scale is supposed to go this high" 
        elif n == '13' :
            print "alright now you're pushing it." 
        elif n == '14' : 
            print "alright, THE SCALE GOES UP TO AROUND 10. CEASE!" 
        elif n == '15' : 
            print " go up one more number. I DARE YOU"
        elif n == '16' : 
            print " go up one more number. see what happens"
        elif n == '17' : 
            print "one more number" 
        elif n == '18' : 
            print "one more" 
        elif n == '19' : 
            print "STOP" 
        elif n == '92412' : 
            print " I think that is one fantastic answer, can't wait for our anniversary" 
        else:
            print "I still really hope that we could get married someday." 

        print """Want to try again?"""
        yes = set(['yes','y', 'ye', ''])
        no = set(['no','n'])

        choice = raw_input().lower()
        if choice in yes:
           myScript()
        elif choice in no:
           sys.exit(0)
        else:
           sys.stdout.write("Please respond with 'yes' or 'no'")
        myScript()



myScript()
