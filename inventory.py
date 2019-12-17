def setup():
    background(0,0,0)
    font = createFont("Georgia", 54)
    textFont(font)
    textAlign(CENTER, TOP)
    text("Inventory", 980, 100)
    stroke(240)
    line(0, 210, 2000, 210)
    
    
    
def draw():
    
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
    

    
    
    
    
    
    
    #if (210 < mouseX < 535 and 440<  mouseY < 525):
        #links = stroke(240)
    #elif (1060 < mouseX < 1500 and 440 < mouseY < 525):
        #rechts = stroke(240)
    #else:
        #stroke(0)
