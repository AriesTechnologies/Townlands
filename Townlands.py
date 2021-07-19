#Author: AtlasCorporations
#Published: AtlasCorporations
#Copyright: 2017-2018
import os
import pygame
import time
from pygame.locals import *
pygame.init()

pygame.display.set_caption("Townlands")
World = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/World.png")
World2 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/WorldNight.png")
Sun = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Sun.png")
Moon = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Moon.png")
RedMoon = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/RedMoon.png")
Portal = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Portal.png")
TownHall = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/TownHall.png")
TownHall2 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/TownHall2.png")
TownHall3 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/TownHall3.png")
Shop = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Shop.png")
Prince = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Prince.png")
LPrince = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/PrinceLeft.png")
Tree = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Tree.png")
Wall = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Wall.png")
Wall2 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Wall2.png")
Statue = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Statue.png")
Statue2 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Statue2.png")
Cannon = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Cannon.png")
Cannon2 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Cannon2.png")
Cannon3 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Cannon3.png")
ArcherTower = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/ArcherTower.png")
ArcherTower2 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/ArcherTower3.png")
ArcherTower3 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/ArcherTower2.png")
PauseMenu = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/PauseMenu.png")
Tree1 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Tree.png")
Waterfall = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Waterfall.png")
Farm = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Farm.png")
Farm2 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Farm2.png")
AtlasFlag = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/AtlasCorpFlag.png")
RedFlag = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/RedFlag.png")
RedBanner = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/RedBanner.png")
RedBannerClan = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/RedBannerClan.png")
YellowFlag = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/YellowFlag.png")
YellowBanner = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/YellowBanner.png")
YellowBannerClan = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/YellowBannerClan.png")
GreenFlag = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/GreenFlag.png")
GreenBanner = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/GreenBanner.png")
GreenBannerClan = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/GreenBannerClan.png")
BlueFlag = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/BlueFlag.png")
BlueBanner = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/BlueBanner.png")
BlueBannerClan = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/BlueBannerClan.png")
PurpleFlag = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/PurpleFlag.png")
PurpleBanner = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/PurpleBanner.png")
PurpleBannerClan = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/PurpleBannerClan.png")
PinkFlag = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/PinkFlag.png")
PinkBanner = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/PinkBanner.png")
PinkBannerClan = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/PinkBannerClan.png")
RedFlagStar = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/RedFlagRedStar.png")
RedStarBanner = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/RedStarBanner.png")
RedStarBannerClan = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/RedStarBannerClan.png")
GreenFlagStar = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/GreenFlagRedStar.png")
GreenStarBanner = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/GreenStarBanner.png")
GreenStarBannerClan = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/GreenBannerClan.png")
BlueFlagStar = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/BlueFlagRedStar.png")
StarryNightFlag = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/StarryNightFlag.png")
NASAFlag = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/NASAFlag.png")
JacksepticeyeBanner = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/JacksepticeyeBanner.png")
JacksepticeyeBannerClan = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/JacksepticeyeBannerClan.png")
Monster = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Monster.png")
Tree2 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Tree.png")
Tree3 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Tree.png")
##Tree4 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Tree.png")
##Tree5 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Tree.png")
##Tree6 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Tree.png")
##Tree7 = pygame.image.load("C:/Users/AtlasDisease/Pictures/Tree.png")
Icon = pygame.image.load("C:/Users/AtlasDisease/Pictures/Games/Townlands/Icon.png")

smallfont = pygame.font.SysFont ("comicsansms", 25)
mediumfont = pygame.font.SysFont ("comicsansms", 50)
largefont = pygame.font.SysFont ("comicsansms", 80)
xlargefont = pygame.font.SysFont ("comicsansms", 85)

black = (0,0,0)
red = (200,0,0)
lightbrown = (185,122,85)
brown = (136,89,63)
white = (255,255,255)

Clock = pygame.time.Clock()
MenuFPS = 10
FPS = 20
global NightFall_Time
NightFall_Time = 600
global Instructions
Instructions = 1
Instructions_Left = 3
First_Time_User = True
Version = "Version 0.4.4 Beta (Release Version)"
Version_Info = "Version Info: Added Game Icon, Improved AtlasCorp Flag, Added new Wall, Added new Archer Tower, Added new Farm, Improved Pause Menu"
Version_Stable = "Version Stability: Stable"
Dev_Version = 0
global paused
paused = False
Display_w = 1280
Display_h = 700
global World_X
World_X = -3680
global World_Y
World_Y = 0
global Sun_X
Sun_X = 0
global Sun_Y
Sun_Y = 0
global TownHall_Level
TownHall_Level = 1
global Last_TownHall_Level
Last_TownHall_Level = 0
global TownHall_X
TownHall_X = 0
global TownHall_Y
TownHall_Y = -20
global TownHall_X_Change
TownHall_X_Change = 0
global Shop_X
Shop_X = 0
global Shop_Y
Shop_Y = 326
global Prince_X
Prince_X = 320
global Prince_Y
Prince_Y = 280
global Prince_Direction
Prince_Direction = "Right"
global Tree_X
Tree_X = 1200
global Tree_Y
Tree_Y = 180
global Tree1_X
Tree1_X = -125
global Statue_X
Statue_X = 2800
global Statue_Y
Statue_Y = 323
global Statue_Level
Statue_Level = 1
global Last_Statue_Level
Last_Statue_Level = 0
global Cannon_X
Cannon_X = -1500
global Cannon_Y
Cannon_Y = 328
global Cannon_Level
Cannon_Level = 1
global Last_Cannon_Level
Last_Cannon_Level = 0
global ArcherTower_X
ArcherTower_X = 1500
global ArcherTower_Y
ArcherTower_Y = 177
global ArcherTower_Level
ArcherTower_Level = 1
global Last_ArcherTower_Level
Last_ArcherTower_Level = 0
global Coins
Coins = 10
global CoinsUsed
CoinsUsed = 0
global Statue_Coins_Used
Statue_Coins_Used = 0
global Cannon_Coins_Used
Cannon_Coins_Used = 0
global ArcherTower_Coins_Used
ArcherTower_Coins_Used = 0
global GameOver
GameOver = False
global Event
Event = 3
global Day
Day = 1
global Last_Day
Last_Day = 0
global Wall_Level
Wall_Level = 1
global Last_Wall_Level
Last_Wall_Level = 0
global Wall_Coins_Used
Wall_Coins_Used = 0
global Wall1_Level
Wall1_Level = 1
global Last_Wall1_Level
Last_Wall1_Level = 0
global Wall1_Coins_Used
Wall1_Coins_Used = 0
global Portal_X
Portal_X = -3860
Portal_Y = 125
global Waterfall_X
Waterfall_X = -1250
Waterfall_Y = -60
global Farm_Level
Farm_Level = 1
global Farm_Coins_Used
Farm_Coins_Used = 0
global Last_Farm_Level
Last_Farm_Level = 0
global Flag_X
Flag_X = 975
global Flag_Y
Flag_Y = -20
global Flag_Type
Flag_Type = 4
global Banner_Type
Banner_Type = 4
global Banner_X
Banner_X = 574
global Banner_Y
Banner_Y = 260
global ArcherTower1_X
ArcherTower1_X = -500
global ArcherTower1_Y
ArcherTower1_Y = 177
global ArcherTower1_Level
ArcherTower1_Level = 1
global Last_ArcherTower1_Level
Last_ArcherTower1_Level = 0
global ArcherTower1_Coins_Used
ArcherTower1_Coins_Used = 0
global Tree2_X
Tree2_X = -1700
global Wall2_Level
Wall2_Level = 1
global Last_Wall2_Level
Last_Wall2_Level = 0
global Wall2_Coins_Used
Wall2_Coins_Used = 0
global Waterfall2_X
Waterfall2_X = 1800
global Farm2_Level
Farm2_Level = 1
global Last_Farm2_Level
Last_Farm2_Level = 0
global Farm2_Coins_Used
Farm2_Coins_Used = 0
global Tree3_X
Tree3_X = 2550
global Wall3_Level
Wall3_Level = 1
global Last_Wall3_Level
Last_Wall3_Level = 0
global Wall3_Coins_Used
Wall3_Coins_Used = 0

newpath = 'C:/Program Files (x86)/AtlasCorporations/Games/SaveFiles/Townlands' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

def SaveFile():
    First_Time_User = False
    str(First_Time_User)
    str(Dev_Version)
    str(World_X)
    str(World_Y)
    str(TownHall_X)
    str(TownHall_Level)
    str(Last_TownHall_Level)
    str(Coins)
    str(CoinsUsed)
    str(Prince_X)
    str(Statue_X)
    str(Statue_Coins_Used)
    str(Statue_Level)
    str(Last_Statue_Level)
    str(Cannon_X)
    str(Cannon_Coins_Used)
    str(Cannon_Level)
    str(Last_Cannon_Level)
    str(ArcherTower_X)
    str(ArcherTower_Level)
    str(Last_ArcherTower_Level)
    str(ArcherTower_Coins_Used)
    str(Instructions)
    str(Day)
    str(NightFall_Time)
    str(Tree1_X)
    str(Portal_X)
    str(Waterfall_X)
    str(Farm_Level)
    str(Last_Farm_Level)
    str(Farm_Coins_Used)
    str(Flag_X)
    str(Flag_Type)
    str(Banner_X)
    str(Banner_Type)
    str(ArcherTower1_X)
    str(ArcherTower1_Level)
    str(Last_ArcherTower1_Level)
    str(Tree2_X)
    str(Wall2_Level)
    str(Last_Wall2_Level)
    str(Wall2_Coins_Used)
    str(Waterfall2_X)
    str(Farm2_Level)
    str(Last_Farm2_Level)
    str(Farm2_Coins_Used)
    str(Tree3_X)
    str(Wall3_Level)
    str(Last_Wall3_Level)
    str(Wall3_Coins_Used)
    File = open("C:/Program Files (x86)/AtlasCorporations/Games/Savefiles/Townlands/savefile.txt", "w")
    File.write(str(First_Time_User))
    File.write("\n")
    File.write(str(Dev_Version))
    File.write("\n")
    File.write(str(World_X))
    File.write("\n")
    File.write(str(TownHall_X))
    File.write("\n")
    File.write(str(TownHall_Level))
    File.write("\n")
    File.write(str(Last_TownHall_Level))
    File.write("\n")
    File.write(str(Shop_X))
    File.write("\n")
    File.write(str(Coins))
    File.write("\n")
    File.write(str(CoinsUsed))
    File.write("\n")
    File.write(str(Prince_X))
    File.write("\n")
    File.write(str(Statue_X))
    File.write("\n")
    File.write(str(Statue_Coins_Used))
    File.write("\n")
    File.write(str(Statue_Level))
    File.write("\n")
    File.write(str(Last_Statue_Level))
    File.write("\n")
    File.write(str(Cannon_X))
    File.write("\n")
    File.write(str(Cannon_Coins_Used))
    File.write("\n")
    File.write(str(Cannon_Level))
    File.write("\n")
    File.write(str(Last_Cannon_Level))
    File.write("\n")
    File.write(str(ArcherTower_X))
    File.write("\n")
    File.write(str(ArcherTower_Level))
    File.write("\n")
    File.write(str(Last_ArcherTower_Level))
    File.write("\n")
    File.write(str(ArcherTower_Coins_Used))
    File.write("\n")
    File.write(str(Instructions))
    File.write("\n")
    File.write(str(Day))
    File.write("\n")
    File.write(str(NightFall_Time))
    File.write("\n")
    File.write(str(Tree1_X))
    File.write("\n")
    File.write(str(Portal_X))
    File.write("\n")
    File.write(str(Waterfall_X))
    File.write("\n")
    File.write(str(Farm_Level))
    File.write("\n")
    File.write(str(Last_Farm_Level))
    File.write("\n")
    File.write(str(Farm_Coins_Used))
    File.write("\n")
    File.write(str(Flag_X))
    File.write("\n")
    File.write(str(Flag_Type))
    File.write("\n")
    File.write(str(Banner_X))
    File.write("\n")
    File.write(str(Banner_Type))
    File.write("\n")
    File.write(str(ArcherTower1_X))
    File.write("\n")
    File.write(str(ArcherTower1_Level))
    File.write("\n")
    File.write(str(Last_ArcherTower1_Level))
    File.write("\n")
    File.write(str(Tree2_X))
    File.write("\n")
    File.write(str(Wall2_Level))
    File.write("\n")
    File.write(str(Last_Wall2_Level))
    File.write("\n")
    File.write(str(Wall2_Coins_Used))
    File.write("\n")
    File.write(str(Waterfall2_X))
    File.write("\n")
    File.write(str(Farm2_Level))
    File.write("\n")
    File.write(str(Last_Farm2_Level))
    File.write("\n")
    File.write(str(Farm2_Coins_Used))
    File.write("\n")
    File.write(str(Tree3_X))
    File.write("\n")
    File.write(str(Wall3_Level))
    File.write("\n")
    File.write(str(Last_Wall3_Level))
    File.write("\n")
    File.write(str(Wall3_Coins_Used))
    File.write("\n")
    File.close()

try:
    with open("C:/Program Files (x86)/AtlasCorporations/Games/Savefiles/Townlands/savefile.txt") as File:
        D0 = File.readline()
        First_Time_User = bool(D0)
        D1 = File.readline()
        Dev_Version = int(D1)
        D2 = File.readline()
        World_X = int(D2)
        D3 = File.readline()
        TownHall_X_Change = int(D3)
        D4 = File.readline()
        TownHall_Level = int(D4)
        D5 = File.readline()
        Last_TownHall_Level = int(D5)
        D6 = File.readline()
        Shop_X = int(D6)
        D7 = File.readline()
        Coins = int(D7)
        D8 = File.readline()
        CoinsUsed = int(D8)
        D9 = File.readline()
        Prince_X = int(D9)
        D10 = File.readline()
        Statue_X = int(D10)
        D11 = File.readline()
        Statue_Coins_Used = int(D11)
        D12 = File.readline()
        Statue_Level = int(D12)
        D13 = File.readline()
        Last_Statue_Level = int(D13)
        D14 = File.readline()
        Cannon_X = int(D14)
        D15 = File.readline()
        Cannon_Coins_Used = int(D15)
        D16 = File.readline()
        Cannon_Level = int(D16)
        D17 = File.readline()
        Last_Cannon_Level = int(D17)
        D18 = File.readline()
        ArcherTower_X = int(D18)
        D19 = File.readline()
        ArcherTower_Level = int(D19)
        D20 = File.readline()
        Last_ArcherTower_Level = int(D20)
        D21 = File.readline()
        ArcherTower_Coins_Used = int(D21)
        D22 = File.readline()
        Instructions = int(D22)
        D23 = File.readline()
        Day = int(D23)
        D24 = File.readline()
        NightFall_Time = int(D24)
        D25 = File.readline()
        Tree1_X = int(D25)
        D26 = File.readline()
        Portal_X = int(D26)
        D27 = File.readline()
        Waterfall_X = int(D27)
        D28 = File.readline()
        Farm_Level = int(D28)
        D29 = File.readline()
        Last_Farm_Level = int(D29)
        D30 = File.readline()
        Farm_Coins_Used = int(D30)
        D31 = File.readline()
        Flag_X = int(D31)
        D32 = File.readline()
        Flag_Type = int(D32)
        D33 = File.readline()
        Banner_X = int(D33)
        D34 = File.readline()
        Banner_Type = int(D34)
        D35 = File.readline()
        ArcherTower1_X = int(D35)
        D36 = File.readline()
        ArcherTower1_Level = int(D36)
        D37 = File.readline()
        Last_ArcherTower1_Level = int(D37)
        D38 = File.readline()
        Tree2_X = int(D38)
        D39 = File.readline()
        Wall2_Level = int(D39)
        D40 = File.readline()
        Last_Wall2_Level = int(D40)
        D41 = File.readline()
        Wall2_Coins_Used = int(D41)
        D42 = File.readline()
        Waterfall2_X = int(D42)
        D43 = File.readline()
        Farm2_Level = int(D43)
        D44 = File.readline()
        Last_Farm2_Level = int(D44)
        D45 = File.readline()
        Farm2_Coins_Used = int(D45)
        D46 = File.readline()
        Tree3_X = int(D46)
        D47 = File.readline()
        Wall3_Level = int(D47)
        D48 = File.readline()
        Last_Wall3_Level = int(D48)
        D49 = File.readline()
        Wall3_Coins_Used = int(D49)

except ValueError:
    SaveFile()
        
except IOError:
    if First_Time_User == False:
        print("Type of Error: IOError")
        print("Error Number: 000001")
        print("Error Statement: Cannot open file or can't find file")
        print("For More Infomation: www.atlascorporations.com/games/errors")

except OSError:
    print("Type of Error: OSError")
    print("Error Number: 000002")
    print("Error Statement: Main Cause Unknown.")
    print("For More Infomation: www.atlascorporations.com/games/errors")

try:
    with open("C:/Program Files (x86)/AtlasCorporations/Games/SaveFiles/Townlands/version.txt") as File3:
        VD0 = File3.readline()
        Version = str(VD0)
        VD1 = File3.readline()
        Version_Stable = str(VD1)

except IOError:
    if First_Time_User == False:
        print("Type of Error: IOError")
        print("Error Number: 000001")
        print("Error Statement: Cannot open file or can't find file")
        print("For More Infomation: www.atlascorporations.com/games/errors")

except OSError:
    print("Type of Error: OSError")
    print("Error Number: 000002")
    print("Error Statement: Main Cause Unknown.")
    print("For More Infomation: www.atlascorporations.com/games/errors")
    pygame.quit()

def SaveFile2():
    File2 = open("C:/Program Files (x86)/AtlasCorporations/Games/SaveFiles/Townlands/pastversionsinfo.txt", "w")
    File2.write("Update 0.1.0 Gamma:\n *Added in basic start off code\n *Added in Town Hall\n")
    File2.write("Update 0.2.0 Gamma:\n *Added in save function and world movement\n")
    File2.write("Update 0.2.1 Gamma:\n *Fixed a couple bugs in the world movement coordinates\n")
    File2.write("Update 0.2.2 Gamma:\n *Fixed another small bug in world movement coordinates\n *Added compressed file startup\n")
    File2.write("Update 0.2.3 Gamma:\n *Added new startup save files\n")
    File2.write("Update 0.2.4 Gamma:\n *Added in a Sun\n *Added code to comment who's the owner of the code\n")
    File2.write("Update 0.2.5 Gamma:\n *Fixed lag bug in movement\n *Added changed movement speed\n")
    File2.write("Update 0.3.0 Gamma:\n *Added Function+F11 to switch back to the last Stable Release Version\n *Added Function+F12 to switch to the Unstable Developer Version\n")
    File2.write("Update 0.3.1 Gamma:\n *Added in better prince character\n *Added in Trees\n *Added in the Shop\n")
    File2.write("Update 0.3.2 Gamma:\n *Added in Statue sprite\n *Compressed some building blitting\n")
    File2.write("Update 0.3.3 Gamma:\n *Added in Cannons\n")
    File2.write("Update 0.3.4 Gamma:\n *Added in Instructions (Click Space to go to the next instruction)\n")
    File2.write("Update 0.3.5 Gamma:\n *Added in Coins amount to screen\n *Added in-game info\n")
    File2.write("Update 0.4.0 Gamma:\n *Added in Archer Tower\n *Improved instructions\n *Added in Night Time\n")
    File2.write("Update 0.4.1 Gamma:\n *Improved Pause Menu and fixed small bug in Pause Menu\n *Fixed big bug in Instructions handling\n *Added more event saving\n *Added in Background Trees")
    File2.write("Update 0.4.2 Gamma:\n *Fixed bug in Pause Menu (sort of),\n *Added new way to exit Pause Menu\n *Added in Walls\n *Added in Farms\n *Added in Portal\n")
    File2.write("Update 0.4.3 Gamma:\n *Added in Farm Level 2\n *Added in Flags\n *Added in Banners\n *Fixed bug with displaying of leveled structures\n *Fixed bug with Night Cycle\n *Changed earned coin amount after day\n")
    File2.write("Update 0.4.4 Gamma:\n *Added Game Icon\n *Improved AtlasCorp Flag\n *Added new Wall\n *Added new Archer Tower\n *Added new Farm\n *Improved Pause Menu\n")
    File2.write("Update 0.4.5 Gamma:\n *Added new Banner Clans\n *Added new Banner\n *Added in Credits\n")
    File2.close()

def SaveFile3():
    File3 = open("C:/Program Files (x86)/AtlasCorporations/Games/SaveFiles/Townlands/version.txt", "w")
    File3.write(Version)
    File3.write("\n")
    File3.write(Version_Info)
    File3.write("\n")
    File3.write(Version_Stable)
    File3.close()
        
def Save():
    SaveFile()
    SaveFile2()
    SaveFile3()

def Text_Objects(Text, Color, Size):
    if Size == "small":
        TextSurface = smallfont.render (Text, True, Color)
    elif Size == "medium":
        TextSurface = mediumfont.render (Text, True, Color)
    elif Size == "large":
        TextSurface = largefont.render (Text, True, Color)
    return TextSurface, TextSurface.get_rect()

def message_to_screen(msg, Color, x_Pos, x_Displace=0, y_Displace=0, Size="small"):
    TextSurf, TextRect = Text_Objects(msg, Color, Size)
    if x_Pos == 1:
        TextRect.left = (int(Display_w/6)+x_Displace, int(Display_h/2)+y_Displace)
    if x_Pos == 1.5:
        TextRect = (int(Display_w/3)+x_Displace, int(Display_h/2)+y_Displace)
    if x_Pos == 2:
        TextRect.center = (int(Display_w/2)+x_Displace, int(Display_h/2)+y_Displace)
    if x_Pos == 3:
        TextRect.right = (int(Display_w/1.5)+x_Displace, int(Display_h/2)+y_Displace)
    gameDisplay.blit(TextSurf, TextRect)

def text_to_button(msg, Color, Button_X, Button_Y, Button_w, Button_h, Size="small"):
    textSurf, textRect  = Text_Objects(msg, Color, Size)
    textRect.center = ((Button_X+(Button_w/2)), Button_Y+(Button_h/2))
    gameDisplay.blit(textSurf, textRect)

def BannerClan_Blit():
    global Banner_Type
    if Banner_Type == 1:
        gameDisplay.blit(RedBannerClan, ((Display_w/2-250), (Display_h/2-250)))
    elif Banner_Type == 2:
        gameDisplay.blit(YellowBannerClan, ((Display_w/2-250), (Display_h/2-250)))
    elif Banner_Type == 3:
        gameDisplay.blit(GreenBannerClan, ((Display_w/2-250), (Display_h/2-250)))
    elif Banner_Type == 4:
        gameDisplay.blit(BlueBannerClan, ((Display_w/2-250), (Display_h/2-250)))
    elif Banner_Type == 5:
        gameDisplay.blit(PurpleBannerClan, ((Display_w/2-250), (Display_h/2-250)))
    elif Banner_Type == 6:
        gameDisplay.blit(PinkBannerClan, ((Display_w/2-250), (Display_h/2-250)))
    elif Banner_Type == 7:
        gameDisplay.blit(RedStarBannerClan, ((Display_w/2-250), (Display_h/2-250)))
    elif Banner_Type == 8:
        gameDisplay.blit(YellowStarBannerClan, ((Display_w/2-250), (Display_h/2-250)))
    elif Banner_Type == 9:
        gameDisplay.blit(GreenStarBannerClan, ((Display_w/2-250), (Display_h/2-250)))
    elif Banner_Type == 10:
        gameDisplay.blit(JacksepticeyeBannerClan, ((Display_w/2-250), (Display_h/2-250)))
        
def Pause():
    global paused
    gameDisplay.blit(PauseMenu, (0,0))
    pygame.draw.rect(gameDisplay, brown, (65, 50, 300, 100))
    pygame.draw.rect(gameDisplay, lightbrown, (78, 63, 275, 75))
    text_to_button("Continue", black, 120, 50, 200, 100, Size="small")
    pygame.draw.rect(gameDisplay, brown, (65, 175, 300, 100))
    pygame.draw.rect(gameDisplay, lightbrown, (78, 187, 275, 75))
    text_to_button("New Game", black, 120, 175, 200, 100, Size="small")
    pygame.draw.rect(gameDisplay, brown, (65, 300, 300, 100))
    pygame.draw.rect(gameDisplay, lightbrown, (78, 312, 275, 75))
    text_to_button("Options", black, 120, 300, 200, 100, Size="small")
    pygame.draw.rect(gameDisplay, brown, (65, 425, 300, 100))
    pygame.draw.rect(gameDisplay, lightbrown, (78, 438, 275, 75))
    text_to_button("Credits", black, 120, 427, 200, 100, Size="small")
    pygame.draw.rect(gameDisplay, brown, (65, 550, 300, 100))
    pygame.draw.rect(gameDisplay, lightbrown, (78, 563, 275, 75))
    text_to_button("Save + Quit", black, 120, 550, 200, 100, Size="small")
    BannerClan_Blit()
    while paused == True:
        pygame.display.update()
        Cursor = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 78+275 > Cursor[0] > 78 and 63+75 > Cursor[1] > 63:
                    paused = False
                    pygame.display.update()
                    break
                elif 78+275 > Cursor[0] > 78 and 187+75 > Cursor[1] > 187:
                    pygame.quit()
                elif 78+275 > Cursor[0] > 78 and 312+75 > Cursor[1] > 312:
                    print("Options Coming Soon")
                    continue
                elif 78+275 > Cursor[0] > 78 and 438+75 > Cursor[1] > 438:
                    gameDisplay.fill(brown)
                    pygame.draw.rect(gameDisplay, lightbrown, (78, 63, 275, 75))
                    text_to_button("Continue", black, 120, 50, 200, 100, Size="small")
                    message_to_screen("Credits:", black, 2, 0, -300, Size="medium")
                    message_to_screen("Made By: AtlasCorporations", black, 2, 0, -250, Size="small")
                    message_to_screen("Published By: AtlasCorporations", black, 2, 0, -200, Size="small")
                    message_to_screen("Copyright By: AtlasCorporations 2017-2018", black, 2, 0 , -150, Size="small")
                    message_to_screen("Project Designer: Brendan Beard", black, 2 , 0 , -100, Size="small")
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 78+275 > Cursor[0] > 78 and 63+75 > Cursor[1] > 63:
                            break
            elif event.type == pygame.QUIT:
                pygame.register_quit(Save())
                pygame.quit()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    continue

def TownHall_Blit():
    global TownHall_Level
    global TownHall_X
    global TownHall_Y
    if TownHall_Level == 1:
        gameDisplay.blit(TownHall, (TownHall_X, TownHall_Y))
    elif TownHall_Level == 2:
        gameDisplay.blit(TownHall2, (TownHall_X, TownHall_Y))
    elif TownHall_Level == 3:
        gameDisplay.blit(TownHall3, (TownHall_X, TownHall_Y))

def Prince_Blit():
    global Prince_Direction
    if Prince_Direction == "Right":
        gameDisplay.blit(Prince, (320, Prince_Y))
    if Prince_Direction == "Left":
        gameDisplay.blit(LPrince, (320, Prince_Y))

def Statue_Blit():
    global Statue_Level
    global Statue_X
    global Statue_Y
    if Statue_Level == 1:
        gameDisplay.blit(Statue, (Statue_X, Statue_Y))
    elif Statue_Level == 2:
        gameDisplay.blit(Statue2, (Statue_X, Statue_Y))

def Cannon_Blit():
    global Cannon_Level
    global Cannon_X
    global Cannon_Y
    if Cannon_Level == 1:
        gameDisplay.blit(Cannon, (Cannon_X, Cannon_Y))
    elif Cannon_Level == 2:
        gameDisplay.blit(Cannon2, (Cannon_X, Cannon_Y))
    elif Cannon_Level == 3:
        gameDisplay.blit(Cannon3, (Cannon_X, Cannon_Y))

def ArcherTower_Blit():
    global ArcherTower_Level
    global ArcherTower_X
    global ArcherTower_Y
    if ArcherTower_Level == 1:
        gameDisplay.blit(ArcherTower, (ArcherTower_X, ArcherTower_Y))
    if ArcherTower_Level == 2:
        gameDisplay.blit(ArcherTower2, (ArcherTower_X, ArcherTower_Y))
    if ArcherTower_Level == 3:
        gameDisplay.blit(ArcherTower3, (ArcherTower_X, ArcherTower_Y))

def Instructions_Check():
    global Instructions
    global Instructions_Left
    if Instructions == 1:
        if Instructions_Left == 3:
            message_to_screen("Click the Left/Right Arrow Keys to move", black, 2, 0, -300, Size="small")
        elif Instructions_Left == 2:
            message_to_screen("Click the Down Arrow to upgrade buildings", black, 2, 0, -300, Size="small")
        elif Instructions_Left == 1:
            message_to_screen("Click the F6 key to get extra help and to pause", black, 2, 0, -300, Size="small")

def Wall_Blit():
    global Wall_Level
    global Tree_X
    global Tree_Y
    if Wall_Level == 1:
        gameDisplay.blit(Tree, (Tree_X, Tree_Y))
    if Wall_Level == 2:
        gameDisplay.blit(Wall, (Tree_X, Tree_Y))
    if Wall_Level == 3:
        gameDisplay.blit(Wall2, (Tree_X, Tree_Y))

def Wall1_Blit():
    global Wall1_Level
    global Tree1_X
    global Tree_Y
    if Wall1_Level == 1:
        gameDisplay.blit(Tree1, (Tree1_X, Tree_Y))
    if Wall1_Level == 2:
        gameDisplay.blit(Wall, (Tree1_X, Tree_Y))
    if Wall1_Level == 3:
        gameDisplay.blit(Wall2, (Tree1_X, Tree_Y))

def Wall2_Blit():
    global Wall2_Level
    global Tree2_X
    global Tree_Y
    if Wall2_Level == 1:
        gameDisplay.blit(Tree2, (Tree2_X, Tree_Y))
    if Wall2_Level == 2:
        gameDisplay.blit(Wall, (Tree2_X, Tree_Y))
    if Wall2_Level == 3:
        gameDisplay.blit(Wall2, (Tree2_X, Tree_Y))

def Wall3_Blit():
    global Wall3_Level
    global Tree3_X
    global Tree_Y
    if Wall3_Level == 1:
        gameDisplay.blit(Tree3, (Tree3_X, Tree_Y))
    if Wall3_Level == 2:
        gameDisplay.blit(Wall, (Tree3_X, Tree_Y))
    if Wall3_Level == 3:
        gameDisplay.blit(Wall2, (Tree3_X, Tree_Y))

def Farm_Blit():
    global Farm_Level
    global Waterfall_X
    global Waterfall_Y
    if Farm_Level == 1:
        gameDisplay.blit(Waterfall, (Waterfall_X, Waterfall_Y))
    if Farm_Level == 2:
        gameDisplay.blit(Farm, (Waterfall_X, Waterfall_Y))
    if Farm_Level == 3:
        gameDisplay.blit(Farm2, (Waterfall_X, Waterfall_Y))

def Farm2_Blit():
    global Farm2_Level
    global Waterfall2_X
    global Waterfall2_Y
    if Farm2_Level == 1:
        gameDisplay.blit(Waterfall, (Waterfall2_X, Waterfall_Y))
    if Farm2_Level == 2:
        gameDisplay.blit(Farm, (Waterfall2_X, Waterfall_Y))
    if Farm2_Level == 3:
        gameDisplay.blit(Farm2, (Waterfall2_X, Waterfall_Y))

def Flag_Blit():
    global Flag_Type
    global Flag_X
    global Flag_Y
    if Flag_Type == 1:
        gameDisplay.blit(RedFlag, (Flag_X, Flag_Y))
    elif Flag_Type == 2:
        gameDisplay.blit(YellowFlag, (Flag_X, Flag_Y))
    elif Flag_Type == 3:
        gameDisplay.blit(GreenFlag, (Flag_X, Flag_Y))
    elif Flag_Type == 4:
        gameDisplay.blit(BlueFlag, (Flag_X, Flag_Y))
    elif Flag_Type == 5:
        gameDisplay.blit(PurpleFlag, (Flag_X, Flag_Y))
    elif Flag_Type == 6:
        gameDisplay.blit(PinkFlag, (Flag_X, Flag_Y))
    elif Flag_Type == 7:
        gameDisplay.blit(RedFlagStar, (Flag_X, Flag_Y))
    elif Flag_Type == 8:
        gameDisplay.blit(GreenFlagStar, (Flag_X, Flag_Y))
    elif Flag_Type == 9:
        gameDisplay.blit(BlueFlagStar, (Flag_X, Flag_Y))
    elif Flag_Type == 10:
        gameDisplay.blit(AtlasFlag, (Flag_X, Flag_Y))
    elif Flag_Type == 11:
        gameDisplay.blit(StarryNightFlag, (Flag_X, Flag_Y))
    elif Flag_Type == 12:
        gameDisplay.blit(NASAFlag, (Flag_X, Flag_Y))

def Banner_Blit():
    global Banner_Type
    global Banner_X
    global Banner_Y
    if Banner_Type == 1:
        gameDisplay.blit(RedBanner, (Banner_X, Banner_Y))
    elif Banner_Type == 2:
        gameDisplay.blit(YellowBanner, (Banner_X, Banner_Y))
    elif Banner_Type == 3:
        gameDisplay.blit(GreenBanner, (Banner_X, Banner_Y))
    elif Banner_Type == 4:
        gameDisplay.blit(BlueBanner, (Banner_X, Banner_Y))
    elif Banner_Type == 5:
        gameDisplay.blit(PurpleBanner, (Banner_X, Banner_Y))
    elif Banner_Type == 6:
        gameDisplay.blit(PinkBanner, (Banner_X, Banner_Y))
    elif Banner_Type == 7:
        gameDisplay.blit(RedStarBanner, (Banner_X, Banner_Y))
    elif Banner_Type == 8:
        gameDisplay.blit(YellowStarBanner, (Banner_X, Banner_Y))
    elif Banner_Type == 9:
        gameDisplay.blit(GreenStarBanner, (Banner_X, Banner_Y))
    elif Banner_Type == 10:
        gameDisplay.blit(JacksepticeyeBanner, (Banner_X, Banner_Y))

def ArcherTower1_Blit():
    global ArcherTower1_Level
    global ArcherTower1_X
    global ArcherTower_Y
    if ArcherTower1_Level == 1:
        gameDisplay.blit(ArcherTower, (ArcherTower1_X, ArcherTower_Y))
    elif ArcherTower1_Level == 2:
        gameDisplay.blit(ArcherTower2, (ArcherTower1_X, ArcherTower_Y))
    elif ArcherTower1_Level == 3:
        gameDisplay.blit(ArcherTower3, (ArcherTower1_X, ArcherTower_Y))

def Graphics_Update():
    global Instructions
    global NightFall_Time
    global Day
    global Coins
    global Last_Day
    NightFall_Time -= 1
    if NightFall_Time > 0:
        gameDisplay.blit(World, (World_X, World_Y))
        gameDisplay.blit(Sun, (Sun_X, Sun_Y))
    else:
        gameDisplay.blit(World2, (World_X, World_Y))
        gameDisplay.blit(Moon, (Sun_X, Sun_Y))
        if Day == 5 or Day == 10 or Day == 15:
            if NightFall_Time < 0:
                gameDisplay.blit(RedMoon, (Sun_X, Sun_Y))
    if NightFall_Time < -600:
        Last_Day += 1
        if Day >= 1 and Last_Day == Day:
            Coins += 10
            if Farm_Level == 2 or Farm2_Level == 2:
                Coins += 5
            elif Farm_Level == 3 or Farm2_Level == 3:
                Coins += 10
            Day += 1
            NightFall_Time = 600

    TownHall_Blit()
    Banner_Blit()
    Flag_Blit()
    gameDisplay.blit(Shop, (Shop_X, Shop_Y))
    gameDisplay.blit(Portal, (Portal_X, Portal_Y))
    Cannon_Blit()
    Statue_Blit()
    ArcherTower_Blit()
    ArcherTower1_Blit()
    Farm_Blit()
    Farm2_Blit()
    Prince_Blit()
    Wall_Blit()
    Wall1_Blit()
    Wall2_Blit()
    Wall3_Blit()
    if Instructions == 1:
        Instructions_Check()
    str(Coins)
    str(Day)
    if NightFall_Time > 0:
        message_to_screen("Day:", black, 2 , -25, -330, Size="small")
        message_to_screen(str(Day), black, 2, 25, -330, Size="small")
        message_to_screen("Coins:", black, 2, 500, -330, Size="small")
        message_to_screen(str(Coins), black, 2, 575, -330, Size="small")
    else:
        message_to_screen("Day:", white, 2, -25, -330, Size="small")
        message_to_screen(str(Day), white, 2, 25, -330, Size="small")
        message_to_screen("Coins:", white, 2, 500, -330, Size="small")
        message_to_screen(str(Coins), white, 2, 575, -330, Size="small")
    pygame.display.update()

def Movement():
    global World_X
    global TownHall_X
    global Shop_X
    global Prince_X
    global Prince_Direction
    global Tree_X
    global Statue_X
    global Cannon_X
    global ArcherTower_X
    global Tree1_X
    global Portal_X
    global Waterfall_X
    global Flag_X
    global Banner_X
    global ArcherTower1_X
    global Tree2_X
    global Waterfall2_X
    global Tree3_X

    if event.key == pygame.K_LEFT:
        if event.key != pygame.K_LSHIFT:
            if World_X != 0:
                World_X += 5
                Prince_X -= 5
                TownHall_X += 5
                Shop_X += 5
                Prince_Direction = "Left"
                Tree_X += 5
                Tree1_X += 5
                Statue_X += 5
                Cannon_X += 5
                ArcherTower_X += 5
                Portal_X += 5
                Waterfall_X += 5
                Flag_X += 5
                Banner_X += 5
                ArcherTower1_X += 5
                Tree2_X += 5
                Waterfall2_X += 5
                Tree3_X += 5

    elif event.key == pygame.K_LSHIFT and pygame.K_LEFT:
        if World_X < 0:
            World_X += 10
            Prince_X -= 10
            TownHall_X += 10
            Shop_X += 10
            Prince_Direction = "Left"
            Tree_X += 10
            Tree1_X += 10
            Statue_X += 10
            Cannon_X += 10
            ArcherTower_X += 10
            Portal_X += 10
            Waterfall_X += 10
            Flag_X += 10
            Banner_X += 10
            ArcherTower1_X += 10
            Tree2_X += 10
            Waterfall2_X += 10
            Tree3_X += 10
        
    elif event.key == pygame.K_RIGHT:
        if event.key != pygame.K_LSHIFT:
            if World_X != -6395:
                World_X -= 5
                TownHall_X -= 5
                Shop_X -= 5
                Prince_X += 5
                Prince_Direction = "Right"
                Tree_X -= 5
                Tree1_X -= 5 
                Statue_X -= 5
                Cannon_X -= 5
                ArcherTower_X -= 5
                Portal_X -= 5
                Waterfall_X -= 5
                Flag_X -= 5
                Banner_X -= 5
                ArcherTower1_X -= 5
                Tree2_X -= 5
                Waterfall2_X -= 5
                Tree3_X -= 5

    elif event.key == pygame.K_RSHIFT and pygame.K_RIGHT:
        if World_X != -6395:
            World_X -= 10
            TownHall_X -= 10
            Shop_X -= 10
            Prince_X += 10
            Prince_Direction = "Right"
            Tree_X -= 10
            Tree1_X -= 10
            Statue_X -= 10
            Cannon_X -= 10
            ArcherTower_X -= 10
            Portal_X -= 10
            Waterfall_X -= 10
            Flag_X -= 10
            Banner_X -= 10
            ArcherTower1_X -= 10
            Tree2_X -= 10
            Waterfall2_X -= 10
            Tree3_X -= 10

def Upgrade():
    global Prince_X
    global Coins
    global CoinsUsed
    global TownHall_Level
    global Statue_Level
    global Last_TownHall_Level
    global Last_Statue_Level
    global Statue_Coins_Used
    global Cannon_Level
    global Last_Cannon_Level
    global Cannon_Coins_Used
    global ArcherTower_Level
    global Last_ArcherTower_Level
    global ArcherTower_Coins_Used
    global Wall_Level
    global Last_Wall_Level
    global Wall_Coins_Used
    global Wall1_Level
    global Last_Wall1_Level
    global Wall1_Coins_Used
    global Farm_Level
    global Last_Farm_Level
    global Farm_Coins_Used
    global ArcherTower1_X
    global ArcherTower1_Level
    global Last_ArcherTower1_Level
    global ArcherTower1_Coins_Used
    global Tree2_X
    global Wall2_Level
    global Last_Wall2_Level
    global Wall2_Coins_Used
    global Waterfall2_X
    global Farm2_Level
    global Last_Farm2_Level
    global Farm2_Coins_Used
    global Wall3_Level
    global Last_Wall3_Level
    global Wall3_Coins_Used
    if event.key == pygame.K_DOWN:
        if Prince_X >= 120 and Prince_X <= 760:
            if Coins >= (5 + CoinsUsed):
                if TownHall_Level == 2:
                    if Statue_Level >= 2:
                        Last_TownHall_Level += 1
                        TownHall_Level = (1 + Last_TownHall_Level)
                        Coins -= (5 + CoinsUsed)
                        CoinsUsed += (5 + CoinsUsed)
                        pygame.time.delay(75)
                    else:
                        message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(750)
                elif TownHall_Level == 1:
                    Last_TownHall_Level += 1
                    TownHall_Level = (1 + Last_TownHall_Level)
                    Coins -= (5 + CoinsUsed)
                    CoinsUsed += (5 + CoinsUsed)
                    pygame.time.delay(75)
                elif TownHall_Level == 3:
                        message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(750)
            else:
                message_to_screen("Not enough coins", red, 2, 0, -300, Size="small")
                pygame.display.update()
                pygame.time.delay(750)
                    
        elif Prince_X <= 2885 and Prince_X >= 2650:
            if Coins >= 8:
                if Statue_Level == 1:
                    Last_Statue_Level += 1
                    Statue_Level = (1 + Last_Statue_Level)
                    Coins -= (8 + Statue_Coins_Used)
                    Statue_Coins_Used += (8 + Statue_Coins_Used)
                    pygame.time.delay(75)
                else:
                    message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                    pygame.display.update()
                    pygame.time.delay(750)
            else:
                message_to_screen("Not enough coins", red, 2, 0, -300, Size="small")
                pygame.display.update()
                pygame.time.delay(750)

        elif Prince_X >= -1665 and Prince_X <= -1440:
            if Coins >= (3 + Cannon_Coins_Used):
                if Cannon_Level == 2:
                    if Statue_Level >= 2:
                        Last_Cannon_Level += 1
                        Cannon_Level = (1 + Last_Cannon_Level)
                        Coins -= (2 + Cannon_Coins_Used)
                        Cannon_Coins_Used += (2 + Cannon_Coins_Used)
                        pygame.time.delay(75)
                    else:
                        message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(750)
                elif Cannon_Level == 1:
                    Last_Cannon_Level += 1
                    Cannon_Level = (1 + Last_Cannon_Level)
                    Coins -= (3 + Cannon_Coins_Used)
                    Cannon_Coins_Used += (3 + Cannon_Coins_Used)
                    pygame.time.delay(75)
                elif Cannon_Level == 3:
                        message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(750)
            else:
                message_to_screen("Not enough coins", red, 2, 0, -300, Size="small")
                pygame.display.update()
                pygame.time.delay(750)

        elif Prince_X >= 1300 and Prince_X <= 1630:
            if Coins >= (5 + ArcherTower_Coins_Used):
                if ArcherTower_Level == 1:
                    if Statue_Level >= 2:
                        Last_ArcherTower_Level += 1
                        ArcherTower_Level = (1 + Last_ArcherTower_Level)
                        Coins -= (3 + ArcherTower_Coins_Used)
                        ArcherTower_Coins_Used += (3 + ArcherTower_Coins_Used)
                        pygame.time.delay(75)
                    else:
                        message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(750)
                elif ArcherTower_Level == 2:
                    if Statue_Level >= 2:
                        Last_ArcherTower_Level += 1
                        ArcherTower_Level = (1 + Last_ArcherTower_Level)
                        Coins -= (3 + ArcherTower_Coins_Used)
                        ArcherTower_Coins_Used += (3 + ArcherTower_Coins_Used)
                        pygame.time.delay(75)
                elif ArcherTower_Level == 3:
                    if Statue_Level >= 2:
                        message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(750)                        
            else:
                message_to_screen("Not enough coins", red, 2, 0, -300, Size="small")
                pygame.display.update()
                pygame.time.delay(750)

        elif Prince_X >= 1000 and Prince_X <= 1160:
            if Coins >= (1 + Wall_Coins_Used):
                if Wall_Level == 2:
                    if Statue_Level >= 2:
                        Last_Wall_Level += 1
                        Wall_Level = (1+Last_Wall_Level)
                        Coins -= (1 + Wall_Coins_Used)
                        Wall_Coins_Used += (1 + Wall_Coins_Used)
                        pygame.time.delay(75)
                    else:
                        message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(750)
                elif Wall_Level == 1:
                    Last_Wall_Level += 1
                    Wall_Level = (1+Last_Wall_Level)
                    Coins -= (1 + Wall_Coins_Used)
                    Wall_Coins_Used += (1 + Wall_Coins_Used)
                    pygame.time.delay(75)
                elif Wall_Level == 3:
                    message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                    pygame.display.update()
                    pygame.time.delay(750)
            else:
                message_to_screen("Not enough coins", red, 2, 0, -300, Size="small")
                pygame.display.update()
                pygame.time.delay(750)

        elif Prince_X >= -320 and Prince_X <= -180:
            if Coins >= (1 + Wall1_Coins_Used):
                if Wall1_Level == 2:
                    if Statue_Level >= 2:
                        Last_Wall1_Level += 1
                        Wall1_Level = (1 + Last_Wall1_Level)
                        Coins -= (1 + Wall1_Coins_Used)
                        Wall1_Coins_Used += (1 + Wall1_Coins_Used)
                        pygame.time.delay(75)
                    else:
                        message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(750)  
                elif Wall1_Level == 1:
                    Last_Wall1_Level += 1
                    Wall1_Level = (1+Last_Wall1_Level)
                    Coins -= (1 + Wall1_Coins_Used)
                    Wall1_Coins_Used += (1 + Wall1_Coins_Used)
                    pygame.time.delay(75)
                elif Wall1_Level == 3:
                    message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                    pygame.display.update()
                    pygame.time.delay(750)
            else:
                message_to_screen("Not enough coins", red, 2, 0, -300, Size="small")
                pygame.display.update()
                pygame.time.delay(750)

        elif Prince_X >= -1120 and Prince_X <= -900:
            if Coins >= (3 + Farm_Coins_Used):
                if Farm_Level == 2:
                    if Statue_Level >= 2:
                        Last_Farm_Level += 1
                        Farm_Level = (1 + Last_Farm_Level)
                        Coins -= (3 + Farm_Coins_Used)
                        pygame.time.delay(75)
                    else:
                        message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(750)            
                elif Farm_Level == 1:
                    Last_Farm_Level += 1
                    Farm_Level = (1 + Last_Farm_Level)
                    Coins -= (3 + Farm_Coins_Used)
                    Farm_Coins_Used += (3 + Farm_Coins_Used)
                    pygame.time.delay(75)
                elif Farm_Level == 3:
                    message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                    pygame.display.update()
                    pygame.time.delay(750) 
            else:
                message_to_screen("Not enough coins", red, 2, 0, -300, Size="small")
                pygame.display.update()
                pygame.time.delay(750)

        elif Prince_X <= -380 and Prince_X >= -700:
            if Coins >= (5 + ArcherTower1_Coins_Used):
                if ArcherTower1_Level == 1:
                    if Statue_Level >= 2:
                        Last_ArcherTower1_Level += 1
                        ArcherTower1_Level = (1 + Last_ArcherTower1_Level)
                        Coins -= (3 + ArcherTower1_Coins_Used)
                        ArcherTower1_Coins_Used += (3 + ArcherTower1_Coins_Used)
                        pygame.time.delay(75)
                    else:
                        message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(750)
                elif ArcherTower1_Level == 2:
                    if Statue_Level >= 2:
                        Last_ArcherTower1_Level += 1
                        ArcherTower1_Level = (1 + Last_ArcherTower1_Level)
                        Coins -= (3 + ArcherTower1_Coins_Used)
                        ArcherTower1_Coins_Used += (3 + ArcherTower1_Coins_Used)
                        pygame.time.delay(75)
                elif ArcherTower1_Level == 3:
                    if Statue_Level >= 2:
                        message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(750)                        
            else:
                message_to_screen("Not enough coins", red, 2, 0, -300, Size="small")
                pygame.display.update()
                pygame.time.delay(750)

        elif Prince_X <= -1775 and Prince_X >= -1900:
            if Coins >= (1 + Wall2_Coins_Used):
                if Wall2_Level == 2:
                    if Statue_Level >= 2:
                        Last_Wall2_Level += 1
                        Wall2_Level = (1 + Last_Wall2_Level)
                        Coins -= (1 + Wall2_Coins_Used)
                        Wall2_Coins_Used += (1 + Wall2_Coins_Used)
                        pygame.time.delay(75)
                    else:
                        message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(750)  
                elif Wall2_Level == 1:
                    Last_Wall2_Level += 1
                    Wall2_Level = (1+Last_Wall2_Level)
                    Coins -= (1 + Wall2_Coins_Used)
                    Wall2_Coins_Used += (1 + Wall2_Coins_Used)
                    pygame.time.delay(75)
                elif Wall2_Level == 3:
                    message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                    pygame.display.update()
                    pygame.time.delay(750)
            else:
                message_to_screen("Not enough coins", red, 2, 0, -300, Size="small")
                pygame.display.update()
                pygame.time.delay(750)

        elif Prince_X >= 1800 and Prince_X <= 2100:
            if Coins >= (3 + Farm2_Coins_Used):
                if Farm2_Level == 2:
                    if Statue_Level >= 2:
                        Last_Farm2_Level += 1
                        Farm2_Level = (1 + Last_Farm2_Level)
                        Coins -= (3 + Farm2_Coins_Used)
                        pygame.time.delay(75)
                    else:
                        message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(750)            
                elif Farm2_Level == 1:
                    Last_Farm2_Level += 1
                    Farm2_Level = (1 + Last_Farm2_Level)
                    Coins -= (3 + Farm2_Coins_Used)
                    Farm2_Coins_Used += (3 + Farm2_Coins_Used)
                    pygame.time.delay(75)
                elif Farm2_Level == 3:
                    message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                    pygame.display.update()
                    pygame.time.delay(750) 
            else:
                message_to_screen("Not enough coins", red, 2, 0, -300, Size="small")
                pygame.display.update()
                pygame.time.delay(750)

        elif Prince_X >= 2370 and Prince_X <= 2450:
            if Coins >= (1 + Wall3_Coins_Used):
                if Wall3_Level == 2:
                    if Statue_Level >= 2:
                        Last_Wall3_Level += 1
                        Wall3_Level = (1 + Last_Wall3_Level)
                        Coins -= (1 + Wall3_Coins_Used)
                        Wall3_Coins_Used += (1 + Wall3_Coins_Used)
                        pygame.time.delay(75)
                        Wall3_Health = 200
                    else:
                        message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(750)  
                elif Wall3_Level == 1:
                    Last_Wall3_Level += 1
                    Wall3_Level = (1+Last_Wall3_Level)
                    Coins -= (1 + Wall3_Coins_Used)
                    Wall3_Coins_Used += (1 + Wall3_Coins_Used)
                    pygame.time.delay(75)
                    Wall3_Health = 150
                elif Wall3_Level == 3:
                    message_to_screen("Max Level?", red, 2, 0, -300, Size="small")
                    pygame.display.update()
                    pygame.time.delay(750)
            else:
                message_to_screen("Not enough coins", red, 2, 0, -300, Size="small")
                pygame.display.update()
                pygame.time.delay(750)

def Instruct():
    global Instructions
    global Instructions_Left
    if Instructions == 1:
        while Instructions_Left > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    Instructions_Left -= 1
                    Graphics_Update()
                       
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    None

gameDisplay = pygame.display.set_mode((Display_w, Display_h))
pygame.display.set_icon(Icon)
Graphics_Update()
pygame.display.update()
Clock.tick(FPS)

if Instructions == 1:
    Instruct()
    while Instructions_Left > 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                Instructions_Left -= 1

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        continue
                
while GameOver == False:
    Clock.tick(FPS)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.register_quit(Save())
            pygame.quit()
            
        elif event.type == pygame.KEYDOWN:
            while event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F6:
                    Clock.tick(MenuFPS)
                    paused = True
                    Pause()

                elif event.key == pygame.K_F11:
                    message_to_screen("Switching to Release Mode", black, 2, 0, -300, Size="small")
                    pygame.display.update()
                    pygame.time.delay(150)
                    Version = "Using Version: Update 0.4.5 Gamma (Release Version)"
                    Version_Info = "Version Info: Added new Banner Clans and Added new Banner, Added in Credits"
                    Version_Stable = "Version Stability: Stable"
                    Dev_Version = 0
                    pygame.register_quit(Save())
                    pygame.quit()

                elif event.key == pygame.K_F12:
                    if Dev_Version == 0:
                        message_to_screen("Switching to Developer Mode", black, 2, 0, -300, Size="small")
                        pygame.display.update()
                        pygame.time.delay(150)
                        Version = "Using Version: Update 0.5.0 Gamma (Developer Version)"
                        Version_Info = "Version Info: Added Running"
                        Version_Stable = "Version Stability: Unstable"
                        Dev_Version = 1
                        pygame.register_quit(Save())
                        pygame.quit()
                        
                Movement()
                Upgrade()
                Graphics_Update()
                
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        continue
