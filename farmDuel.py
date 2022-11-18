import pyautogui
import autoit
import math

class Box:
    def __init__(self, top, left, width, height) -> None:
        self.top=top
        self.left=left 
        self.width=width 
        self.height=height 
        

def click(box):
    autoit.mouse_click("left", math.floor(box.left + box.width/2), math.floor(box.top + box.height/2), 3, 1) 

def duel():
    if(sleep := pyautogui.locateOnScreen('sleep.png', confidence=0.7, grayscale=True)) != None:
        click(sleep)
        while (confirm := pyautogui.locateOnScreen('confirm.png', confidence=0.7, grayscale=True)) == None:
            pyautogui.sleep(.75)
        pyautogui.sleep(.5)
        click(confirm)  
    while (coliseu := pyautogui.locateOnScreen('coliseu.png', confidence=0.7, grayscale=True)) == None:
        pyautogui.sleep(.75)
    pyautogui.sleep(.5)
    click(coliseu)
    while (duelImage := pyautogui.locateOnScreen('duel.png', confidence=0.7, grayscale=True)) == None:
        pyautogui.sleep(.75)
    pyautogui.sleep(.5)
    click(duelImage)
    click(duelImage)
    click(duelImage)
    pyautogui.sleep(.5)

    while (confirm := pyautogui.locateOnScreen('confirm.png', confidence=0.7, grayscale=True)) == None:
        pyautogui.sleep(.75)
    pyautogui.sleep(.5)
    click(confirm)  
    click(confirm)  
    while (attack := pyautogui.locateOnScreen('attack.png', confidence=0.3, grayscale=True)) == None:
        pyautogui.sleep(.75)
    pyautogui.sleep(.5)
    while (confirm := pyautogui.locateOnScreen('confirm.png', confidence=0.7, grayscale=True)) == None:
        pyautogui.sleep(.5)
        if (attack := pyautogui.locateAllOnScreen('attack.png', confidence=0.6, grayscale=True)) != None or (attack := pyautogui.locateAllOnScreen('reverse_attack.png', confidence=0.6, grayscale=True)) != None or (attack := pyautogui.locateAllOnScreen('small_attack.png', confidence=0.6, grayscale=True)) != None:
            chosen_attack = None
            for i, attack_option in enumerate(attack):
                pass
                if attack_option:
                    chosen_attack = attack_option
            if chosen_attack:
                print("attack " + str(chosen_attack))
                chosen_attack_box = Box(chosen_attack.top + 10,chosen_attack.left,chosen_attack.width,chosen_attack.height)
                click(chosen_attack_box)
                autoit.mouse_move(200,200,1)
                

        else:
            if (attack := pyautogui.locateAllOnScreen('low_res_attack.png', confidence=0.6, grayscale=True)) != None or (attack := pyautogui.locateAllOnScreen('reverse_low_res_attack.png', confidence=0.6, grayscale=True)) != None:
                chosen_attack = None
                for i, attack_option in enumerate(attack):
                    pass
                    if attack_option:
                        chosen_attack = attack_option
                        chosen_attack.top = chosen_attack.top + 10
                if chosen_attack:
                    print("low_res " + str(attack))
                    click(chosen_attack)  
                    autoit.mouse_move(200,200,1)
#
        pyautogui.sleep(.75)
    pyautogui.sleep(.5)
    click(confirm)  
    pyautogui.sleep(1)
    #if(agility := pyautogui.locateOnScreen('agility.png', confidence=0.7, grayscale=True)) != None:
    #    for i in range(4):
    #        click(agility)  
    #        pyautogui.sleep(1)
    #    while (confirm := pyautogui.locateOnScreen('confirm.png', confidence=0.7, grayscale=True)) == None:
    #        pyautogui.sleep(.75)
    #    pyautogui.sleep(.5)
    #    click(confirm)  
    #    pyautogui.sleep(.1)
    #    autoit.mouse_move(math.floor(agility.left + agility.width), math.floor(agility.top + agility.height))
    #    autoit.mouse_click("left", agility.left + agility.width/2, agility.top + agility.height/2, 3, .5) 
while True:
    duel()