import smtplib, os

class Mail():

    def __init__(self):
        """Initalization"""
        os.system('clear')
        print("Works with gmai\n")
        print('You\'ve runned the best mail script!')
        print('Open this link \'https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4My3Re3q7mOkgWaFYrNBG6F85VW8jio7RJ299yk3aZJWw2DMhr9Si7GNbMoT2yrfe-fOobQjtCcpMPdTKoO4IhqirLtYQ\'\nand make it enable ')
        
        self.smtp = smtplib.SMTP('smtp.gmail.com', 587)# start smtp server
        self.smtp.starttls()# secure
        self.logIn() # run method lodIn

    def logIn(self):
        """"Log in your mail account"""
        myMail = input('Insert your mail adrees: ')
        myPass = input('Insert your mail adrees\'s password: ')
            
        
        try:
            self.smtp.login('vasenkvak1@gmail.com', 'vasenkvak1') 
            self.send() 
        except:
            print('You\'ve entered the wrong email adrees or password\nPlease try again...')
        
    def send(self):

        print('\n')
        self.toMail = input('Send letter to: ')
        self.message = input('Text:' )
        self.sendTimes = int(input('How many times: '))

        self.letter = ['milagamadrilla@gmail.com', self.toMail ,self.message]

        for i in range(self.sendTimes):
            self.smtp.sendmail(self.letter[0], self.letter[1], self.letter[2])
            print(i + 1 , ' letter has sent...')

        self.quit()

    def quit(self):
        self.smtp.quit()
        


if __name__ == '__main__':
    Mail()

