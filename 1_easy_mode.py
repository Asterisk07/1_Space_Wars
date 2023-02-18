# Import the pygame module
from pygame import mixer as mx
import sqlite3
conn = sqlite3.connect('game1.db')  
cur=conn.cursor()
import pygame
import random
from tkinter import messagebox as mb
from tkinter import *
clock = pygame.time.Clock()
pygame.display.set_caption("Space war") 
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_KP8,
    K_KP4,
    K_KP6,
    K_KP2,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_SPACE,
    QUIT,
)
mx.pre_init()
mx.init()
sound1 = pygame.mixer.Sound("music.mp3")
sound4 = pygame.mixer.Sound("gunfire.wav")

sound1.set_volume(0.05)
sound4.set_volume(0.05)
sound3 = pygame.mixer.Sound("lostmusic.wav")
sound3.set_volume(0.2)
sound2 = pygame.mixer.Sound("boom.wav")

channel1 = pygame.mixer.Channel(0) # argument must be int
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel1.play(sound1, loops = -1)

# mx.music.set_volume(0.2)

# Initialize pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
font_color=(0,0,0)
font_obj=pygame.font.SysFont("Comic Sans MS",25)
# Render the objects

def submit():
    q1="""UPDATE scores
    SET Name="{}",score={}
    WHERE id = 1;""".format(E1.get(),score)
    cur.execute(q1)
    # print("done")
    top.destroy()
    


 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # self.surf = pygame.image.load("lives.png").convert()
        myimage = pygame.image.load("tri3.png")
        # self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.Surface((45,45))
        self.rect = self.surf.get_rect()
        self.surf.blit(myimage,self.rect)
        # self.surf.fill((255,255,255))
    def pos(self):
        return (self.rect.right,(self.rect.top+self.rect.bottom)//2)
    def update(self, pressed_keys):
        r=2
        # if pressed_keys[K_F1]:
        if pressed_keys[K_UP] or pressed_keys[K_KP8]:
            self.rect.move_ip(0, -r)
        if pressed_keys[K_DOWN] or pressed_keys[K_KP2]:
            self.rect.move_ip(0,r)
        if pressed_keys[K_LEFT] or pressed_keys[K_KP4]:
            self.rect.move_ip(-r, 0)
        if pressed_keys[K_RIGHT] or pressed_keys[K_KP6]:
            self.rect.move_ip(r, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
# def collide(a,b):
    
#     c=a.rect
#     d=b.rect
#     if ((c.left<=d.left<=c.right) or (c.left<=d.right<=c.right)) and ((c.top>=d.top>=c.bottom) or (c.top>=d.bottom>=c.bottom)):
#         print("ture")
#         return True
#     print(c.left,d.left,c.right,d.right,"\t",c.top,d.top,c.bottom,d.bottom)
#     return False

class cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(cloud,self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        # self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        # self.speed = random.randint(1,3)
        k=random.randint(1,max(20,score//5))
       
        
        self.speed = k
        
        self.speed = 1
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Gun(pygame.sprite.Sprite):
    def __init__(self,tupple):
        super(Gun,self).__init__()
        myimage = pygame.image.load("gun.png")
        # self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.Surface((20,5))
        self.rect = self.surf.get_rect(
            center=tupple
        )
        self.surf.blit(myimage,self.rect)
        self.speed=2
        # self.surf = pygame.image.load("bull.png").convert()
        # self.rect=
    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.left > SCREEN_WIDTH:
            self.kill()
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        # self.surf = pygame.Surface((20,10))
        # self.surf = pygame.image.load("bull.png").convert()
        myimage = pygame.image.load("bull.png")
        # self.surf.fill((255,0,0))
        self.surf = pygame.Surface((40,40))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        # self.speed = random.randint(1,3)
        
        k=random.randint(max(1,score//35),max(score//30,2))
       
        
        self.speed = k
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = 0
player=Player()
guns=pygame.sprite.Group()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Main loop
i=0
score=0
# mx.music.play()
mb.showinfo('Welcome!',' This is Space War v2. An example game by Ayushmaan Pandey. ')
mb.showinfo('Instructions','Use arrow keys to dodge the enemies .\n press Space Bar to fire bullets at the enemy!\nPress Escape to exit.')
# global levelspeed
# levelspeed=500
options_list = ["Easy","Medium","Hard"]
levmenu=Tk()
level=StringVar(levmenu)
level.set("Click here to select difficulty level: ")
question_menu = OptionMenu(levmenu, level, *options_list)
question_menu.pack()
def set_level():
    global levelspeed
    levelspeed=300
    if (level.get()=="Easy"):
        levelspeed=120
        # print(levelspeed)
        # print("hegsgdghdsgdjr")
    elif (level.get()=="Hard"):
        levelspeed=500
    # levmenu.deiconify()
    # levmenu.quit()
    levmenu.destroy()
    

submit_button = Button(levmenu, text='Choose', command=set_level)
submit_button.pack()
  
levmenu.mainloop()
# print("my speed is ",levelspeed)
res=mb.askquestion( 'Ready?',' Click Yes or press Enter to begin')
if res == 'yes' :
    running=1
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 1000)
    ADDCLOUD = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDCLOUD, 1000)
    # RELOAD=
    RELOAD = pygame.USEREVENT + 3
    pygame.time.set_timer(RELOAD, 1000)
else :
    running=0

# tasks:
# make keydown space to fire
# class Gun
# sprite gun

# Main loop
# screen.fill((135, 206, 250))
# print("my speed is ",levelspeed)
ammo=1
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
            elif event.key==K_SPACE and ammo:
                ammo=0
                channel3.play(sound4)
                gun=Gun(player.pos())
                all_sprites.add(gun)
                guns.add(gun)
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
        elif event.type==ADDENEMY:
            score=score+1
            enem=Enemy()
            all_sprites.add(enem)
            enemies.add(enem)
        elif event.type==ADDCLOUD:
            clo=cloud()
            all_sprites.add(clo)
            clouds.add(clo)
        elif event.type==RELOAD and (ammo==0):
           ammo=1

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Fill the screen with black
    screen.fill((85,184,241,255))
    # print(i)
    guns.update()
    enemies.update()
    clouds.update()
    # if (i<255):
    #     i=i+0.05
    # surf=pygame.Surface((50,50))
    # surf=player.surf
    # # surf.fill((0, 0, 0))
    # rect=player.rect
    # screen.blit(surf, ((SCREEN_WIDTH-surf.get_width())/2, (SCREEN_HEIGHT-surf.get_height())/2))
    for entity in clouds:
        screen.blit(entity.surf, entity.rect)
    text_obj=font_obj.render("Score:"+str(score),True,font_color)
    screen.blit(text_obj, (400,0))
    # for gun in guns:
    #     for enemy in enemies:
    #         if collide(enemy,gun):
    #             print("collide")
    #             enemy.kill()
    #             gun.kill()
    for enemy in enemies:
        if pygame.sprite.spritecollideany(enemy, guns):
            enemy.kill()
            channel2.play(sound2)
    for entity in enemies:
        screen.blit(entity.surf, entity.rect)
    screen.blit(player.surf, player.rect)
    for entity in guns:
        screen.blit(entity.surf, entity.rect)
    if pygame.sprite.spritecollideany(player, enemies):
    # If so, then remove the player and stop the loop
        player.kill()
        running = False
        # messagebox.showinfo('Game Over!','Well played!\n Your score is '+str(score//4))
        mx.music.stop()
    
        
        
            
    # GAME_FONT.render_to(screen, (40, 350), "Hello World!", (0, 0, 0))
    pygame.display.flip()
    clock.tick(levelspeed)
    # clock.tick(speed)
channel1.play(sound3)


mb.showinfo('Game Over!','Well played!\n Your score is '+str(score))
# conn.execute(q)
q = """SELECT * from scores;"""
cur.execute(q)
d=cur.fetchall()
for i in d:
    if (score>i[2]):
        top=Tk()
        # top.eval('PlaceWindow . center')

        frame = Frame(top)
        frame.pack()
        bottomframe = Frame(top)
        bottomframe.pack( side = BOTTOM )
        top.title("High Score!")
        L1 = Label(frame, text="Enter your username")
        L1.pack( side = LEFT)
        E1 = Entry(frame, bd =5)
        E1.pack(side = RIGHT)
        subm = Button(bottomframe, text="Submit", fg="green",command=submit)
        subm.pack( side = LEFT)
        subm = Button(bottomframe, text="Quit", fg="red",command=quit)
        subm.pack( side = RIGHT)
      
        top.mainloop()

conn.commit()
conn.close()
mb.showinfo('Saved!',' Thank you for playing')