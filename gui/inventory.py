

Bear_Skin = 0
Wolf_Skin = 0
Soul_Dead = 0
Wooden_Stick = 0
Wooden_Chunk = 0
Iron_Chunk = 0
Enchanted_Wolf = 0
Mana_Essence = 0
Obsidian = 0
Void_Energy = 0
Haunted_Spirit = 0
Cursed_Wood = 0
Gold_Ingot = 0
Scorpion_Poison = 0
Fire_Essence = 0
Void_Energy = 0

Basic_Spear = 0
Comet_Spear = 0
Spear_Doom = 0
Basic_Sword = 0
Arcane_Sword = 0
Lost_Blade = 0
Sword_Phoenix = 0
Chain_Armour = 0
Black_Armour = 0
Molten_Armour = 0
Wooden_Shield = 0
Iron_Shield = 0
Null_Shield = 0
Gold_Shield = 0
Basic_Dagger = 0
Enchanted_Dagger = 0

def setup():
    fullScreen()
    background(0,0,0)
    font = createFont("Georgia", 54)
    textFont(font)
    textAlign(CENTER, TOP)
    text("Inventory", 980, 100)
    stroke(240)
    line(0, 210, 2000, 210)
    currentNumber = 0

    
    
def draw():
    global Bear_Skin, Wolf_Skin, Soul_Dead, Wooden_Stick, Wooden_Chunk, Iron_Chunk, Enchanted_Wolf, Mana_Essence, Obsidian, Void_Energy, Haunted_Spirit, Cursed_Wood, Gold_Ingot, Scorpion_Poison, Fire_Essense
    
    Bear_Skin = 0
    Wolf_Skin = 0
    Soul_Dead = 0
    Wooden_Stick = 0
    Wooden_Chunk = 0
    Iron_Chunk = 0
    Enchanted_Wolf = 0
    Mana_Essence = 0
    Obsidian = 0
    Void_Energy = 0
    Haunted_Spirit = 0
    Cursed_Wood = 0
    Gold_Ingot = 0
    Scorpion_Poison = 0
    Fire_Essence = 0
    
    textSize(52)
    textAlign(LEFT)
    text("Bear Skin", 110, 350)
    text(Bear_Skin, 700, 350)
    text("Wolf Skin", 110, 410)
    text(Wolf_Skin, 700, 410)
    text("Soul of the Dead", 110, 470)
    text(Soul_Dead, 700, 470)
    text("Wooden Stick", 110, 530)
    text(Wooden_Stick, 700, 530)
    text("Wooden Chunk",1000, 350)
    text(Wooden_Chunk, 1600, 350)
    text("Iron Chunk", 1000, 410)
    text(Iron_Chunk, 1600, 410)
    text("Enchanted Wolf Skin", 1000, 470)
    text(Enchanted_Wolf, 1600, 470)
    text("Mana Essence", 1000, 530)
    text(Mana_Essence, 1600, 530)
    text("Obsidian", 110, 760)
    text(Obsidian, 700, 760)
    text("Void Energy", 110, 820)
    text(Void_Energy, 700, 820)
    text("Haunted Spirit", 110, 880)
    text(Haunted_Spirit, 700, 880)
    text("Cursed Wood", 110, 940)
    text(Cursed_Wood, 700, 940)
    text("Gold Ingot", 1000, 760)
    text(Gold_Ingot, 1600, 760)
    text("Scorpion Poison", 1000, 820)
    text(Scorpion_Poison, 1600, 820)
    text("Fire Essence", 1000, 880)
    text(Fire_Essence, 1600, 880)
    text("Void Energy", 1000, 940)
    text(Void_Energy, 1600, 940)
    
        
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False

#def mousePressed():
    #if isMouseWithinSpace(150, 850, 150, 60):
        #increaseCurrentNumber()
    
