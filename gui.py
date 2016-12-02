import pygame
import Tkinter
import tkMessageBox


#Defines colors to be used easily so you can call them by name
white = (255, 255, 255)


black = (0, 0, 0)


red = (200, 0, 0)


green = (0, 200, 0)


blue = (0, 0, 255)


bright_green = (0, 255, 0)


bright_red = (255, 0, 0)


display_width = 800


display_height = 600




clock = pygame.time.Clock()


#Creates the canvas of the game, sets the size. This is the surface


gameDisplay = pygame.display.set_mode((display_width,display_height))


#Or display.flip(), which updates the entire surface at once. Whereas upda


#A small simple function that facilitates printing text
def text_objects(text, font):


    textSurface = font.render(text, True, black)


    return textSurface, textSurface.get_rect()


#This function defines the buttons for the main menu and eventually the game itself. x, y, w, and h are the position and size of the button, and the on/offcolor decide the color when the mouse is touching the button.
def button(message,x,y,w,h,offColor,onColor,action=None):


    mouse = pygame.mouse.get_pos()


    click = pygame.mouse.get_pressed()


    #print(click)
    #Draws a specific rectangle if the mouse is there


    if x+w > mouse[0] > x and y+h > mouse[1] > y:


        pygame.draw.rect(gameDisplay, onColor,(x,y,w,h))






        if click[0] == 1 and action != None:


            action()
    #Draws a different rectangle if it isn't         


    else:


        pygame.draw.rect(gameDisplay, offColor,(x,y,w,h))






    smallText = pygame.font.SysFont("freesansbold.ttf",20)


    textSurf, textRect = text_objects(message, smallText)


    textRect.center = ( (x+(w/2)), (y+(h/2)) )


    gameDisplay.blit(textSurf, textRect)




#Pop-up is for the main menu. It is a function that is used to open a text box, mostly for the instructions option on the main menu.


def popup():






    window = Tkinter.Tk()
    #This line is important! Without it, a grey box opens up and is just there, blocking some of the screen and causing some problems.


    window.wm_withdraw()






    tkMessageBox.showinfo(title="Instructions", message="Poker is a family of gambling card games, but is often considered a skill based game. All poker variants involve betting as an intrinsic part of play, and determine the winner of each hand according to the combinations of players' cards, at least some of which remain hidden until the end of the hand. Poker games vary in the number of cards dealt, the number of shared or community cards, the number of cards that remain hidden, and the betting procedures.\n In most modern poker games, the first round of betting begins with one or more of the players making some form of a forced bet (the blind and/or ante). In standard poker, each player bets according to the rank he believes his hand is worth as compared to the other players. The action then proceeds clockwise as each player in turn must either match, or call, the maximum previous bet or fold, losing the amount bet so far and all further interest in the hand. A player who matches a bet may also raise, or increase the bet. The betting round ends when all players have either called the last bet or folded. If all but one player folds on any round, the remaining player collects the pot without being required to reveal their hand. If more than one player remains in contention after the final betting round, a showdown takes place where the hands are revealed, and the player with the winning hand takes the pot.\nWith the exception of initial forced bets, money is only placed into the pot voluntarily by a player who either believes the bet has positive expected value or who is trying to bluff other players for various strategic reasons. Thus, while the outcome of any particular hand significantly involves chance, the long-run expectations of the players are determined by their actions chosen on the basis of probability, psychology, and game theory.")








class Menu:
        
        


    def __init__(self, image, gameDisplay, display_width, display_height, gameLoop):


     


     intro = True


     #BackGround = Background(image, [0,0])


     pygame.display.update()






     while intro: 






      


      for event in pygame.event.get():


        #print(event)


        if event.type == pygame.QUIT:


          pygame.quit()


          quit()


      gameDisplay.fill(white)


      #This makes it easier to call title text


      largeText = pygame.font.Font('freesansbold.ttf', 100)
          #These three lines define and display the title


      TextSurf, TextRect = text_objects("Texas Hold 'Em", largeText)


      TextRect.center = ((display_width/2), (display_height/2))


      gameDisplay.blit(TextSurf, TextRect)






      #Defines what the mouse's position is in an easy variable


      mouse = pygame.mouse.get_pos()


      #If the mouse's position is inside the green button, it becomes bright green. Otherwise it stays green. Same concept with red.


          #These are the four buttons displayed on the main menu


      button("Play",200,450,100,50,green,bright_green,gameLoop)


      button("How to",325,450,100,50,red,bright_red,popup)


      button("High Scores",450,450,100,50,green,bright_green,gameLoop)


      button("Options",575,450,100,50,red,bright_red,gameLoop)






      pygame.display.update()






      #These two lines down here constantly refresh the visuals


      pygame.display.update()














      clock.tick(15)
#Just sets up a background using an image file
class Background(pygame.sprite.Sprite):


    def __init__(self, image_file, location):


        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer


        self.image = pygame.image.load(image_file)


        self.rect = self.image.get_rect()


        self.rect.left, self.rect.top = location
#Incomplete, would convert images into sprites for card files so they can be displayed
class Cards(pygame.sprite.Sprite):
    def __init__(self, image_file, name):
       pygame.sprite.Sprite.__init__(self)  


       self.image = pygame.image.load(image_file)
       screen_text = font.render(name, True, color)
       #Fix display location to be fixed underneath the card


       gameDisplay.blit(screen_text, [display_width/2, display_height/2])
