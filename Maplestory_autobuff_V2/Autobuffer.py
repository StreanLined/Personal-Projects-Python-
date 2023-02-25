import pyautogui
from pyautogui import *
import datetime
import time
import keyboard
import random
import win32api, win32con
from tkinter import *
from PIL import ImageTk, Image




# Enablers
start = True
current_selected_class = ()


# Class list
classes = [
    "Phantom",
    "Adele",
    "Bishop",
    "Pathfinder",
    "Luminous",
    "Evan",
    "Kanna",
    "Kain",
    "Mercedes"
]

# Phantom skills
phantom_heroic_memories = ("C:/Python/Maplestory_autobuff_V2/classes/phantom/phantom_heroic_memories.png")
phantom_goddesses_blessing = ("C:/Python/Maplestory_autobuff_V2/classes/phantom/phantom_goddesses_blessing.png")

# Adele skills
adele_divine_wrath = ("C:/Python/Maplestory_autobuff_V2/classes/adele/adele_divine_wrath.png")
adele_goddesses_blessing = ("C:/Python/Maplestory_autobuff_V2/classes/adele/adele_goddesses_blessing.png")
adele_legacy_restoration = ("C:/Python/Maplestory_autobuff_V2/classes/adele/adele_legacy_restoration.png")
adele_weapon_aura = ("C:/Python/Maplestory_autobuff_V2/classes/adele/adele_weapon_aura.png")
adele_hunting_decree = ("C:/Python/Maplestory_autobuff_V2/classes/adele/adele_hunting_decree.png")
adele_aether_forge = ("C:/Python/Maplestory_autobuff_V2/classes/adele/adele_aether_forge.png")
adele_aetherial_arms = ("C:/Python/Maplestory_autobuff_V2/classes/adele/adele_aetherial_arms.png")

# Bishop skills
bishop_divine_protection = ("C:/Python/Maplestory_autobuff_V2/classes/bishop/bishop_divine_protection.png")
bishop_epic_adventure = ("C:/Python/Maplestory_autobuff_V2/classes/bishop/bishop_epic_adventure.png")
bishop_goddesses_blessing = ("C:/Python/Maplestory_autobuff_V2/classes/bishop/bishop_goddesses_blessing.png")
bishop_infinity = ("C:/Python/Maplestory_autobuff_V2/classes/bishop/bishop_infinity.png")
bishop_magic_guard = ("C:/Python/Maplestory_autobuff_V2/classes/bishop/bishop_magic_guard.png")
bishop_teleport_boost = ("C:/Python/Maplestory_autobuff_V2/classes/bishop/bishop_teleport_boost.png")
bishop_teleport_mastery = ("C:/Python/Maplestory_autobuff_V2/classes/bishop/bishop_teleport_mastery.png")

# Pathfinder skills
pathfinder_epic_adventure = ("C:/Python/Maplestory_autobuff_V2/classes/pathfinder/pathfinder_epic_adventure.png")

# Cannon Master skills
cannon_master_anchors_aweigh = ("C:/Python/Maplestory_autobuff_V2/classes/cannon_master/cannon_master_anchors_aweigh.png")
cannon_master_barrel_roulette = ("C:/Python/Maplestory_autobuff_V2/classes/cannon_master/cannon_master_barrel_roulette.png")
cannon_master_buckshot = ("C:/Python/Maplestory_autobuff_V2/classes/cannon_master/cannon_master_buckshot.png")
cannon_master_epic_adventure = ("C:/Python/Maplestory_autobuff_V2/classes/cannon_master/cannon_master_epic_adventure.png")
cannon_master_monkey_militia = ("C:/Python/Maplestory_autobuff_V2/classes/cannon_master/cannon_master_monkey_militia.png")
cannon_master_rollofthedice = ("C:/Python/Maplestory_autobuff_V2/classes/cannon_master/cannon_master_rollofthedice.png")

# Luminous skills
luminous_heroic_memories = ("C:/Python/Maplestory_autobuff_V2/classes/luminous/luminous_heroic_memories.png")
luminous_light_speed_boost = ("C:/Python/Maplestory_autobuff_V2/classes/luminous/luminous_light_speed_boost.png")

# Evan skills
evan_decent_hyper_body = ("C:/Python/Maplestory_autobuff_V2/classes/evan/evan_decent_hyper_body.png")
evan_heroic_memories = ("C:/Python/Maplestory_autobuff_V2/classes/evan/evan_heroic_memories.png")
evan_magic_guard = ("C:/Python/Maplestory_autobuff_V2/classes/evan/evan_magic_guard.png")

# Kanna skills
kanna_circle_of_suppression = ("C:/Python/Maplestory_autobuff_V2/classes/kanna/kanna_circle_of_suppression.png")
kanna_haku_reborn2 = ("C:/Python/Maplestory_autobuff_V2/classes/kanna/kanna_haku_reborn2.png")
kanna_shikigami_doppelganger = ("C:/Python/Maplestory_autobuff_V2/classes/kanna_shikigami_doppelganger.png")

# Kain skills
kain_dragon_fang = ("C:/Python/Maplestory_autobuff_V2/classes/kain/kain_dragon_fang.png")
kain_lasting_grudge = ("C:/Python/Maplestory_autobuff_V2/classes/kain/kain_lasting_grudge.png")

# Mercedes skills
mercedes_elemental_knights = ("C:/Python/Maplestory_autobuff_V2/classes/mercedes/mercedes_elemental_knights.png")

def confirm_selection():
    global start
    global current_selected_class
    current_selected_class = current.get()
    start = False
    main.destroy()

if start == True:
    main = Tk()
    main.title("Maplestory Autobuffer | Main Menu")
    main.iconbitmap("C:\Python\Maplestory_autobuff_V2\Maplestory.ico")
    main.geometry("330x60")

    # Variables
    current = StringVar()
    current.set("-")

    # Objects
    class_selector_label = Label(main, text="Select your class: ").grid(row=0, column=0, pady=20, padx=20)
    class_selector_menu = OptionMenu(main, current, *classes)
    confirm_selection = Button(main, text="Confirm", command=confirm_selection).grid(row=0, column= 2, padx=20)

    # Placement
    class_selector_menu.grid(row=0, column=1)

    main.mainloop()



# Phantom Menu
if current_selected_class == classes[0]:
    phantom = Tk()
    phantom.title("Maplestory Autobuffer | Phantom")
    phantom.iconbitmap("C:\Python\Maplestory_autobuff_V2\Maplestory.ico")
    phantom.geometry("470x170")

    phantom_activation = False
    newbind_phantom_heroic_memories = ("F4")
    newbind_phantom_goddesses_blessing = ("F5")


    def phantom_confirm_selection():
        global start
        global current_selected_class
        current_selected_class = current.get()
        phantom.destroy()

    def phantom_activate_autobuffer():
        global phantom_activation
        phantom_activation = True
        phantom.destroy()


    def bind_phantom_heroic_memories():
        newbind_phantom_heroic_memories = entry_phantom_heroic_memories.get()
        label_newbind_phantom_heroic_memories = Label(phantom, text="    ").grid(row=1, column=3)
        label_newbind_phantom_heroic_memories = Label(phantom, text=newbind_phantom_heroic_memories).grid(row=1, column=3)
        entry_phantom_heroic_memories.delete(0, END)

    def bind_phantom_goddesses_blessing():
        newbind_phantom_goddesses_blessing = entry_phantom_goddesses_blessing.get()
        label_newbind_phantom_goddesses_blessing = Label(phantom, text="    ").grid(row=2, column=3)
        label_newbind_phantom_goddesses_blessing = Label(phantom, text=newbind_phantom_goddesses_blessing).grid(row=2, column=3)
        entry_phantom_goddesses_blessing.delete(0, END)

    # Variables
    current = StringVar()
    current.set(current_selected_class)

    # Objects
    class_selector_label = Label(phantom, text="Select your class: ").grid(row=0, column=0, pady=20, padx=20)
    class_selector_menu = OptionMenu(phantom, current, *classes)
    confirm_selection = Button(phantom, text="Confirm", command=phantom_confirm_selection).grid(row=0, column= 2, padx=20)
    activation_button = Button(phantom, text="Activate Autobuffer", width=60, command=phantom_activate_autobuffer).grid(row=3, column=0, columnspan=5, padx=20, pady=5)
    entry_phantom_heroic_memories = Entry(phantom)
    entry_phantom_goddesses_blessing = Entry(phantom)
    confirm_phantom_heroic_memories = Button(phantom, text="Bind", command=bind_phantom_heroic_memories).grid(row=1, column=2)
    confirm_phantom_goddesses_blessing = Button(phantom, text="Bind", command=bind_phantom_goddesses_blessing).grid(row=2, column=2)
    label_newbind_phantom_heroic_memories = Label(phantom, text=newbind_phantom_heroic_memories).grid(row=1, column=3)
    label_newbind_phantom_goddesses_blessing = Label(phantom, text=newbind_phantom_goddesses_blessing).grid(row=2, column=3)


    # Image Objects
    display_phantom_heroic_memories = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/phantom/phantom_heroic_memories.png"))
    display2_phantom_heroic_memories = Label(image=display_phantom_heroic_memories).grid(row=1, column=0)
    display_phantom_goddesses_blessing = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/phantom/phantom_goddesses_blessing.png"))
    displa2_phantom_goddesses_blessing = Label(image=display_phantom_goddesses_blessing).grid(row=2, column=0)

    # Placement
    class_selector_menu.grid(row=0, column=1)
    entry_phantom_heroic_memories.grid(row=1, column=1)
    entry_phantom_goddesses_blessing.grid(row=2, column=1)

    phantom.mainloop()

# Adele Menu
if current_selected_class == classes[1]:
    adele = Tk()
    adele.title("Maplestory Autobuffer | Adele")
    adele.iconbitmap("C:\Python\Maplestory_autobuff_V2\Maplestory.ico")
    adele.geometry("470x340")

    adele_activation = False
    newbind_adele_divine_wrath = ("F3")
    newbind_adele_goddesses_blessing = ("F5")
    newbind_adele_hunting_decree = ("2")
    newbind_adele_legacy_restoration = ("F5")
    newbind_adele_weapon_aura = ("F4")
    newbind_adele_aether_forge = ("F9")
    newbind_adele_aetherial_arms = ("F10")

    def adele_confirm_selection():
        global start
        global current_selected_class
        current_selected_class = current.get()
        adele.destroy()

    def adele_activate_autobuffer():
        global adele_activation
        adele_activation = True
        adele.destroy()


    def bind_adele_divine_wrath():
        newbind_adele_divine_wrath = entry_adele_divine_wrath.get()
        label_newbind_adele_divine_wrath = Label(adele, text="    ").grid(row=1, column=3)
        label_newbind_adele_divine_wrath = Label(adele, text=newbind_adele_divine_wrath).grid(row=1, column=3)
        entry_adele_divine_wrath.delete(0, END)

    def bind_adele_goddesses_blessing():
        newbind_adele_goddesses_blessing = entry_adele_goddesses_blessing.get()
        label_newbind_adele_goddesses_blessing = Label(adele, text="    ").grid(row=2, column=3)
        label_newbind_adele_goddesses_blessing = Label(adele, text=newbind_adele_goddesses_blessing).grid(row=2, column=3)
        entry_adele_goddesses_blessing.delete(0, END)

    def bind_adele_hunting_decree():
        newbind_adele_hunting_decree = entry_adele_hunting_decree.get()
        label_newbind_adele_hunting_decree = Label(adele, text="    ").grid(row=3, column=3)
        label_newbind_adele_hunting_decree = Label(adele, text=newbind_adele_hunting_decree).grid(row=3, column=3)
        entry_adele_hunting_decree.delete(0, END)

    def bind_adele_legacy_restoration():
        newbind_adele_legacy_restoration = entry_adele_legacy_restoration.get()
        label_newbind_adele_legacy_restoration = Label(adele, text="    ").grid(row=4, column=3)
        label_newbind_adele_legacy_restoration = Label(adele, text=newbind_adele_legacy_restoration).grid(row=4, column=3)
        entry_adele_legacy_restoration.delete(0, END)

    def bind_adele_weapon_aura():
        newbind_adele_weapon_aura = entry_adele_weapon_aura.get()
        label_newbind_adele_weapon_aura = Label(adele, text="    ").grid(row=5, column=3)
        label_newbind_adele_weapon_aura = Label(adele, text=newbind_adele_weapon_aura).grid(row=5, column=3)
        entry_adele_weapon_aura.delete(0, END)

    def bind_adele_aether_forge():
        newbind_adele_aether_forge = entry_adele_aether_forge.get()
        label_newbind_adele_aether_forge = Label(adele, text="    ").grid(row=5, column=3)
        label_newbind_adele_aether_forge = Label(adele, text=newbind_adele_aether_forge).grid(row=6, column=3)
        entry_adele_aether_forge.delete(0, END)

    def bind_adele_aetherial_arms():
        newbind_adele_aetherial_arms = entry_adele_aetherial_arms.get()
        label_newbind_adele_aetherial_arms = Label(adele, text="    ").grid(row=5, column=3)
        label_newbind_adele_aetherial_arms = Label(adele, text=newbind_adele_aetherial_arms).grid(row=6, column=3)
        entry_adele_aetherial_arms.delete(0, END)


    # Variables
    current = StringVar()
    current.set(current_selected_class)

    # Objects
    class_selector_label = Label(adele, text="Select your class: ").grid(row=0, column=0, pady=20, padx=20)
    class_selector_menu = OptionMenu(adele, current, *classes)
    confirm_selection = Button(adele, text="Confirm", command=adele_confirm_selection).grid(row=0, column= 2, padx=20)
    activation_button = Button(adele, text="Activate Autobuffer", width=60, command=adele_activate_autobuffer).grid(row=8, column=0, columnspan=5, padx=20, pady=5)
    entry_adele_divine_wrath = Entry(adele)
    entry_adele_goddesses_blessing = Entry(adele)
    entry_adele_hunting_decree = Entry(adele)
    entry_adele_legacy_restoration = Entry(adele)
    entry_adele_weapon_aura = Entry(adele)
    entry_adele_aether_forge = Entry(adele)
    entry_adele_aetherial_arms = Entry(adele)
    confirm_adele_divine_wrath = Button(adele, text="Bind", command=bind_adele_divine_wrath).grid(row=1, column=2)
    confirm_adele_goddesses_blessing = Button(adele, text="Bind", command=bind_adele_goddesses_blessing).grid(row=2, column=2)
    confirm_adele_hunting_decree = Button(adele, text="Bind", command=bind_adele_hunting_decree).grid(row=3, column=2)
    confirm_adele_legacy_restoration = Button(adele, text="Bind", command=bind_adele_legacy_restoration).grid(row=4, column=2)
    confirm_adele_weapon_aura = Button(adele, text="Bind", command=bind_adele_weapon_aura).grid(row=5, column=2)
    confirm_adele_aether_forge = Button(adele, text="Bind", command=bind_adele_aether_forge).grid(row=6, column=2)
    confirm_adele_aetherial_arms = Button(adele, text="Bind", command=bind_adele_aetherial_arms).grid(row=7, column=2)
    label_newbind_adele_divine_wrath = Label(adele, text=newbind_adele_divine_wrath).grid(row=1, column=3)
    label_newbind_adele_goddesses_blessing = Label(adele, text=newbind_adele_goddesses_blessing).grid(row=2, column=3)
    label_newbind_adele_hunting_decree = Label(adele, text=newbind_adele_hunting_decree).grid(row=3, column=3)
    label_newbind_adele_legacy_restoration = Label(adele, text=newbind_adele_legacy_restoration).grid(row=4, column=3)
    label_newbind_adele_weapon_aura = Label(adele, text=newbind_adele_weapon_aura).grid(row=5, column=3)
    label_newbind_adele_aether_forge = Label(adele, text=newbind_adele_aether_forge).grid(row=6, column=3)
    label_newbind_adele_aetherial_arms = Label(adele, text=newbind_adele_aetherial_arms).grid(row=7, column=3)


    # Image Objects
    display_adele_divine_wrath = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/adele/adele_divine_wrath.png"))
    display2_adele_divine_wrath = Label(image=display_adele_divine_wrath).grid(row=1, column=0)
    display_adele_goddesses_blessing = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/adele/adele_goddesses_blessing.png"))
    displa2_adele_goddesses_blessing = Label(image=display_adele_goddesses_blessing).grid(row=2, column=0)
    display_adele_hunting_decree = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/adele/adele_hunting_decree.png"))
    display2_adele_hunting_decree = Label(image=display_adele_hunting_decree).grid(row=3, column=0)
    display_adele_legacy_restoration = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/adele/adele_legacy_restoration.png"))
    display2_adele_legacy_restoration = Label(image=display_adele_legacy_restoration).grid(row=4, column=0)
    display_adele_weapon_aura = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/adele/adele_weapon_aura.png"))
    display2_adele_weapon_aura = Label(image=display_adele_weapon_aura).grid(row=5, column=0)
    display_adele_aether_forge = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/adele/adele_aether_forge.png"))
    display2_adele_aether_forge = Label(image=display_adele_aether_forge).grid(row=6, column=0)
    display_adele_aetherial_arms = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/adele/adele_aetherial_arms.png"))
    display2_adele_aetherial_arms = Label(image=display_adele_aetherial_arms).grid(row=7, column=0)


    # Placement
    class_selector_menu.grid(row=0, column=1)
    entry_adele_divine_wrath.grid(row=1, column=1)
    entry_adele_goddesses_blessing.grid(row=2, column=1)
    entry_adele_hunting_decree.grid(row=3, column=1)
    entry_adele_legacy_restoration.grid(row=4, column=1)
    entry_adele_weapon_aura.grid(row=5, column=1)
    entry_adele_aether_forge.grid(row=6, column=1)
    entry_adele_aetherial_arms.grid(row=7, column=1)

    adele.mainloop()

# Bishop Menu
if current_selected_class == classes[2]:
    bishop = Tk()
    bishop.title("Maplestory Autobuffer | Bishop")
    bishop.iconbitmap("C:\Python\Maplestory_autobuff_V2\Maplestory.ico")
    bishop.geometry("470x340")

    bishop_activation = False
    newbind_bishop_divine_protection = ("F8")
    newbind_bishop_epic_adventure = ("F4")
    newbind_bishop_goddesses_blessing = ("F5")
    newbind_bishop_infinity = ("F3")
    newbind_bishop_magic_guard = ("F9")
    newbind_bishop_teleport_boost = ("F10")
    newbind_bishop_teleport_mastery = ("F11")

    def bishop_confirm_selection():
        global start
        global current_selected_class
        current_selected_class = current.get()
        bishop.destroy()

    def bishop_activate_autobuffer():
        global bishop_activation
        bishop_activation = True
        bishop.destroy()


    def bind_bishop_divine_protection():
        newbind_bishop_divine_protection = entry_bishop_divine_protection.get()
        label_newbind_bishop_divine_protection = Label(bishop, text="    ").grid(row=1, column=3)
        label_newbind_bishop_divine_protection = Label(bishop, text=newbind_bishop_divine_protection).grid(row=1, column=3)
        entry_bishop_divine_protection.delete(0, END)

    def bind_bishop_goddesses_blessing():
        newbind_bishop_goddesses_blessing = entry_bishop_goddesses_blessing.get()
        label_newbind_bishop_goddesses_blessing = Label(bishop, text="    ").grid(row=2, column=3)
        label_newbind_bishop_goddesses_blessing = Label(bishop, text=newbind_bishop_goddesses_blessing).grid(row=2, column=3)
        entry_bishop_goddesses_blessing.delete(0, END)

    def bind_bishop_epic_adventure():
        newbind_bishop_epic_adventure = entry_bishop_epic_adventure.get()
        label_newbind_bishop_epic_adventure = Label(bishop, text="    ").grid(row=3, column=3)
        label_newbind_bishop_epic_adventure = Label(bishop, text=newbind_bishop_epic_adventure).grid(row=3, column=3)
        entry_bishop_epic_adventure.delete(0, END)

    def bind_bishop_infinity():
        newbind_bishop_infinity = entry_bishop_infinity.get()
        label_newbind_bishop_infinity = Label(bishop, text="    ").grid(row=4, column=3)
        label_newbind_bishop_infinity = Label(bishop, text=newbind_bishop_infinity).grid(row=4, column=3)
        entry_bishop_infinity.delete(0, END)

    def bind_bishop_magic_guard():
        newbind_bishop_magic_guard = entry_bishop_magic_guard.get()
        label_newbind_bishop_magic_guard = Label(bishop, text="    ").grid(row=5, column=3)
        label_newbind_bishop_magic_guard = Label(bishop, text=newbind_bishop_magic_guard).grid(row=5, column=3)
        entry_bishop_magic_guard.delete(0, END)

    def bind_bishop_teleport_boost():
        newbind_bishop_teleport_boost = entry_bishop_teleport_boost.get()
        label_newbind_bishop_teleport_boost = Label(bishop, text="    ").grid(row=5, column=3)
        label_newbind_bishop_teleport_boost = Label(bishop, text=newbind_bishop_teleport_boost).grid(row=6, column=3)
        entry_bishop_teleport_boost.delete(0, END)

    def bind_bishop_teleport_mastery():
        newbind_bishop_teleport_mastery = entry_bishop_teleport_mastery.get()
        label_newbind_bishop_teleport_mastery = Label(bishop, text="    ").grid(row=5, column=3)
        label_newbind_bishop_teleport_mastery = Label(bishop, text=newbind_bishop_teleport_mastery).grid(row=6, column=3)
        entry_bishop_teleport_mastery.delete(0, END)


    # Variables
    current = StringVar()
    current.set(current_selected_class)

    # Objects
    class_selector_label = Label(bishop, text="Select your class: ").grid(row=0, column=0, pady=20, padx=20)
    class_selector_menu = OptionMenu(bishop, current, *classes)
    confirm_selection = Button(bishop, text="Confirm", command=bishop_confirm_selection).grid(row=0, column= 2, padx=20)
    activation_button = Button(bishop, text="Activate Autobuffer", width=60, command=bishop_activate_autobuffer).grid(row=8, column=0, columnspan=5, padx=20, pady=5)
    entry_bishop_divine_protection = Entry(bishop)
    entry_bishop_goddesses_blessing = Entry(bishop)
    entry_bishop_epic_adventure = Entry(bishop)
    entry_bishop_infinity = Entry(bishop)
    entry_bishop_magic_guard = Entry(bishop)
    entry_bishop_teleport_boost = Entry(bishop)
    entry_bishop_teleport_mastery = Entry(bishop)
    confirm_bishop_divine_protection = Button(bishop, text="Bind", command=bind_bishop_divine_protection).grid(row=1, column=2)
    confirm_bishop_goddesses_blessing = Button(bishop, text="Bind", command=bind_bishop_goddesses_blessing).grid(row=2, column=2)
    confirm_bishop_epic_adventure = Button(bishop, text="Bind", command=bind_bishop_epic_adventure).grid(row=3, column=2)
    confirm_bishop_infinity = Button(bishop, text="Bind", command=bind_bishop_infinity).grid(row=4, column=2)
    confirm_bishop_magic_guard = Button(bishop, text="Bind", command=bind_bishop_magic_guard).grid(row=5, column=2)
    confirm_bishop_teleport_boost = Button(bishop, text="Bind", command=bind_bishop_teleport_boost).grid(row=6, column=2)
    confirm_bishop_teleport_mastery = Button(bishop, text="Bind", command=bind_bishop_teleport_mastery).grid(row=7, column=2)
    label_newbind_bishop_divine_protection = Label(bishop, text=newbind_bishop_divine_protection).grid(row=1, column=3)
    label_newbind_bishop_goddesses_blessing = Label(bishop, text=newbind_bishop_goddesses_blessing).grid(row=2, column=3)
    label_newbind_bishop_epic_adventure = Label(bishop, text=newbind_bishop_epic_adventure).grid(row=3, column=3)
    label_newbind_bishop_infinity = Label(bishop, text=newbind_bishop_infinity).grid(row=4, column=3)
    label_newbind_bishop_magic_guard = Label(bishop, text=newbind_bishop_magic_guard).grid(row=5, column=3)
    label_newbind_bishop_teleport_boost = Label(bishop, text=newbind_bishop_teleport_boost).grid(row=6, column=3)
    label_newbind_bishop_teleport_mastery = Label(bishop, text=newbind_bishop_teleport_mastery).grid(row=7, column=3)


    # Image Objects
    display_bishop_divine_protection = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/bishop/bishop_divine_protection.png"))
    display2_bishop_divine_protection = Label(image=display_bishop_divine_protection).grid(row=1, column=0)
    display_bishop_goddesses_blessing = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/bishop/bishop_goddesses_blessing.png"))
    displa2_bishop_goddesses_blessing = Label(image=display_bishop_goddesses_blessing).grid(row=2, column=0)
    display_bishop_epic_adventure = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/bishop/bishop_epic_adventure.png"))
    display2_bishop_epic_adventure = Label(image=display_bishop_epic_adventure).grid(row=3, column=0)
    display_bishop_infinity = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/bishop/bishop_infinity.png"))
    display2_bishop_infinity = Label(image=display_bishop_infinity).grid(row=4, column=0)
    display_bishop_magic_guard = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/bishop/bishop_magic_guard.png"))
    display2_bishop_magic_guard = Label(image=display_bishop_magic_guard).grid(row=5, column=0)
    display_bishop_teleport_boost = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/bishop/bishop_teleport_boost.png"))
    display2_bishop_teleport_boost = Label(image=display_bishop_teleport_boost).grid(row=6, column=0)
    display_bishop_teleport_mastery = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/bishop/bishop_teleport_mastery.png"))
    display2_bishop_teleport_mastery = Label(image=display_bishop_teleport_mastery).grid(row=7, column=0)


    # Placement
    class_selector_menu.grid(row=0, column=1)
    entry_bishop_divine_protection.grid(row=1, column=1)
    entry_bishop_goddesses_blessing.grid(row=2, column=1)
    entry_bishop_epic_adventure.grid(row=3, column=1)
    entry_bishop_infinity.grid(row=4, column=1)
    entry_bishop_magic_guard.grid(row=5, column=1)
    entry_bishop_teleport_boost.grid(row=6, column=1)
    entry_bishop_teleport_mastery.grid(row=7, column=1)

    bishop.mainloop()

# Pathfinder Menu
if current_selected_class == classes[3]:
    pathfinder = Tk()
    pathfinder.title("Maplestory Autobuffer | Pathfinder")
    pathfinder.iconbitmap("C:\Python\Maplestory_autobuff_V2\Maplestory.ico")
    pathfinder.geometry("470x135")

    pathfinder_activation = False
    newbind_pathfinder_epic_adventure = ("F3")

    def pathfinder_confirm_selection():
        global start
        global current_selected_class
        current_selected_class = current.get()
        pathfinder.destroy()

    def pathfinder_activate_autobuffer():
        global pathfinder_activation
        pathfinder_activation = True
        pathfinder.destroy()


    def bind_pathfinder_epic_adventure():
        newbind_pathfinder_epic_adventure = entry_pathfinder_epic_adventure.get()
        label_newbind_pathfinder_epic_adventure = Label(pathfinder, text="    ").grid(row=1, column=3)
        label_newbind_pathfinder_epic_adventure = Label(pathfinder, text=newbind_pathfinder_epic_adventure).grid(row=1, column=3)
        entry_pathfinder_epic_adventure.delete(0, END)

    # Variables
    current = StringVar()
    current.set(current_selected_class)

    # Objects
    class_selector_label = Label(pathfinder, text="Select your class: ").grid(row=0, column=0, pady=20, padx=20)
    class_selector_menu = OptionMenu(pathfinder, current, *classes)
    confirm_selection = Button(pathfinder, text="Confirm", command=pathfinder_confirm_selection).grid(row=0, column= 2, padx=20)
    activation_button = Button(pathfinder, text="Activate Autobuffer", width=60, command=pathfinder_activate_autobuffer).grid(row=3, column=0, columnspan=5, padx=20, pady=5)
    entry_pathfinder_epic_adventure = Entry(pathfinder)
    confirm_pathfinder_epic_adventure = Button(pathfinder, text="Bind", command=bind_pathfinder_epic_adventure).grid(row=1, column=2)
    label_newbind_pathfinder_epic_adventure = Label(pathfinder, text=newbind_pathfinder_epic_adventure).grid(row=1, column=3)


    # Image Objects
    display_pathfinder_epic_adventure = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/pathfinder/pathfinder_epic_adventure.png"))
    display2_pathfinder_epic_adventure = Label(image=display_pathfinder_epic_adventure).grid(row=1, column=0)

    # Placement
    class_selector_menu.grid(row=0, column=1)
    entry_pathfinder_epic_adventure.grid(row=1, column=1)

    pathfinder.mainloop()

# Luminous Menu
if current_selected_class == classes[4]:
    luminous = Tk()
    luminous.title("Maplestory Autobuffer | Luminous")
    luminous.iconbitmap("C:\Python\Maplestory_autobuff_V2\Maplestory.ico")
    luminous.geometry("470x170")

    luminous_activation = False
    newbind_luminous_heroic_memories = ("F5")
    newbind_luminous_light_speed_boost = ("F9")


    def luminous_confirm_selection():
        global start
        global current_selected_class
        current_selected_class = current.get()
        luminous.destroy()

    def luminous_activate_autobuffer():
        global luminous_activation
        luminous_activation = True
        luminous.destroy()


    def bind_luminous_heroic_memories():
        newbind_luminous_heroic_memories = entry_luminous_heroic_memories.get()
        label_newbind_luminous_heroic_memories = Label(luminous, text="    ").grid(row=1, column=3)
        label_newbind_luminous_heroic_memories = Label(luminous, text=newbind_luminous_heroic_memories).grid(row=1, column=3)
        entry_luminous_heroic_memories.delete(0, END)

    def bind_luminous_light_speed_boost():
        newbind_luminous_light_speed_boost = entry_luminous_light_speed_boost.get()
        label_newbind_luminous_light_speed_boost = Label(luminous, text="    ").grid(row=2, column=3)
        label_newbind_luminous_light_speed_boost = Label(luminous, text=newbind_luminous_light_speed_boost).grid(row=2, column=3)
        entry_luminous_light_speed_boost.delete(0, END)


    # Variables
    current = StringVar()
    current.set(current_selected_class)

    # Objects
    class_selector_label = Label(luminous, text="Select your class: ").grid(row=0, column=0, pady=20, padx=20)
    class_selector_menu = OptionMenu(luminous, current, *classes)
    confirm_selection = Button(luminous, text="Confirm", command=luminous_confirm_selection).grid(row=0, column= 2, padx=20)
    activation_button = Button(luminous, text="Activate Autobuffer", width=60, command=luminous_activate_autobuffer).grid(row=3, column=0, columnspan=5, padx=20, pady=5)
    entry_luminous_heroic_memories = Entry(luminous)
    entry_luminous_light_speed_boost = Entry(luminous)
    confirm_luminous_heroic_memories = Button(luminous, text="Bind", command=bind_luminous_heroic_memories).grid(row=1, column=2)
    confirm_luminous_light_speed_boost = Button(luminous, text="Bind", command=bind_luminous_light_speed_boost).grid(row=2, column=2)
    label_newbind_luminous_heroic_memories = Label(luminous, text=newbind_luminous_heroic_memories).grid(row=1, column=3)
    label_newbind_luminous_light_speed_boost = Label(luminous, text=newbind_luminous_light_speed_boost).grid(row=2, column=3)


    # Image Objects
    display_luminous_heroic_memories = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/luminous/luminous_heroic_memories.png"))
    display2_luminous_heroic_memories = Label(image=display_luminous_heroic_memories).grid(row=1, column=0)
    display_luminous_light_speed_boost = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/luminous/luminous_light_speed_boost.png"))
    displa2_luminous_light_speed_boost = Label(image=display_luminous_light_speed_boost).grid(row=2, column=0)

    # Placement
    class_selector_menu.grid(row=0, column=1)
    entry_luminous_heroic_memories.grid(row=1, column=1)
    entry_luminous_light_speed_boost.grid(row=2, column=1)

    luminous.mainloop()

# Evan Menu
if current_selected_class == classes[5]:
    evan = Tk()
    evan.title("Maplestory Autobuffer | Evan")
    evan.iconbitmap("C:\Python\Maplestory_autobuff_V2\Maplestory.ico")
    evan.geometry("470x200")

    evan_activation = False
    newbind_evan_decent_hyper_body = ("F4")
    newbind_evan_heroic_memories = ("F5")
    newbind_evan_magic_guard = ("F9")

    def evan_confirm_selection():
        global start
        global current_selected_class
        current_selected_class = current.get()
        evan.destroy()

    def evan_activate_autobuffer():
        global evan_activation
        evan_activation = True
        evan.destroy()


    def bind_evan_decent_hyper_body():
        newbind_evan_decent_hyper_body = entry_evan_decent_hyper_body.get()
        label_newbind_evan_decent_hyper_body = Label(evan, text="    ").grid(row=1, column=3)
        label_newbind_evan_decent_hyper_body = Label(evan, text=newbind_evan_decent_hyper_body).grid(row=1, column=3)
        entry_evan_decent_hyper_body.delete(0, END)

    def bind_evan_heroic_memories():
        newbind_evan_heroic_memories = entry_evan_heroic_memories.get()
        label_newbind_evan_heroic_memories = Label(evan, text="    ").grid(row=2, column=3)
        label_newbind_evan_heroic_memories = Label(evan, text=newbind_evan_heroic_memories).grid(row=2, column=3)
        entry_evan_heroic_memories.delete(0, END)

    def bind_evan_magic_guard():
        newbind_evan_magic_guard = entry_evan_magic_guard.get()
        label_newbind_evan_magic_guard = Label(evan, text="    ").grid(row=3, column=3)
        label_newbind_evan_magic_guard = Label(evan, text=newbind_evan_magic_guard).grid(row=3, column=3)
        entry_evan_magic_guard.delete(0, END)


    # Variables
    current = StringVar()
    current.set(current_selected_class)

    # Objects
    class_selector_label = Label(evan, text="Select your class: ").grid(row=0, column=0, pady=20, padx=20)
    class_selector_menu = OptionMenu(evan, current, *classes)
    confirm_selection = Button(evan, text="Confirm", command=evan_confirm_selection).grid(row=0, column= 2, padx=20)
    activation_button = Button(evan, text="Activate Autobuffer", width=60, command=evan_activate_autobuffer).grid(row=8, column=0, columnspan=5, padx=20, pady=5)
    entry_evan_decent_hyper_body = Entry(evan)
    entry_evan_heroic_memories = Entry(evan)
    entry_evan_magic_guard = Entry(evan)
    confirm_evan_decent_hyper_body = Button(evan, text="Bind", command=bind_evan_decent_hyper_body).grid(row=1, column=2)
    confirm_evan_heroic_memories = Button(evan, text="Bind", command=bind_evan_heroic_memories).grid(row=2, column=2)
    confirm_evan_magic_guard = Button(evan, text="Bind", command=bind_evan_magic_guard).grid(row=3, column=2)
    label_newbind_evan_decent_hyper_body = Label(evan, text=newbind_evan_decent_hyper_body).grid(row=1, column=3)
    label_newbind_evan_heroic_memories = Label(evan, text=newbind_evan_heroic_memories).grid(row=2, column=3)
    label_newbind_evan_magic_guard = Label(evan, text=newbind_evan_magic_guard).grid(row=3, column=3)


    # Image Objects
    display_evan_decent_hyper_body = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/evan/evan_decent_hyper_body.png"))
    display2_evan_decent_hyper_body = Label(image=display_evan_decent_hyper_body).grid(row=1, column=0)
    display_evan_heroic_memories = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/evan/evan_heroic_memories.png"))
    displa2_evan_heroic_memories = Label(image=display_evan_heroic_memories).grid(row=2, column=0)
    display_evan_magic_guard = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/evan/evan_magic_guard.png"))
    display2_evan_magic_guard = Label(image=display_evan_magic_guard).grid(row=3, column=0)


    # Placement
    class_selector_menu.grid(row=0, column=1)
    entry_evan_decent_hyper_body.grid(row=1, column=1)
    entry_evan_heroic_memories.grid(row=2, column=1)
    entry_evan_magic_guard.grid(row=3, column=1)

    evan.mainloop()

# Kanna Menu
if current_selected_class == classes[6]:
    kanna = Tk()
    kanna.title("Maplestory Autobuffer | Kanna")
    kanna.iconbitmap("C:\Python\Maplestory_autobuff_V2\Maplestory.ico")
    kanna.geometry("470x200")

    kanna_activation = False
    newbind_kanna_circle_of_suppression = ("F4")
    newbind_kanna_haku_reborn2 = ("F5")
    newbind_kanna_shikigami_doppelganger = ("F9")

    def kanna_confirm_selection():
        global start
        global current_selected_class
        current_selected_class = current.get()
        kanna.destroy()

    def kanna_activate_autobuffer():
        global kanna_activation
        kanna_activation = True
        kanna.destroy()


    def bind_kanna_circle_of_suppression():
        newbind_kanna_circle_of_suppression = entry_kanna_circle_of_suppression.get()
        label_newbind_kanna_circle_of_suppression = Label(kanna, text="    ").grid(row=1, column=3)
        label_newbind_kanna_circle_of_suppression = Label(kanna, text=newbind_kanna_circle_of_suppression).grid(row=1, column=3)
        entry_kanna_circle_of_suppression.delete(0, END)

    def bind_kanna_haku_reborn2():
        newbind_kanna_haku_reborn2 = entry_kanna_haku_reborn2.get()
        label_newbind_kanna_haku_reborn2 = Label(kanna, text="    ").grid(row=2, column=3)
        label_newbind_kanna_haku_reborn2 = Label(kanna, text=newbind_kanna_haku_reborn2).grid(row=2, column=3)
        entry_kanna_haku_reborn2.delete(0, END)

    def bind_kanna_shikigami_doppelganger():
        newbind_kanna_shikigami_doppelganger = entry_kanna_shikigami_doppelganger.get()
        label_newbind_kanna_shikigami_doppelganger = Label(kanna, text="    ").grid(row=3, column=3)
        label_newbind_kanna_shikigami_doppelganger = Label(kanna, text=newbind_kanna_shikigami_doppelganger).grid(row=3, column=3)
        entry_kanna_shikigami_doppelganger.delete(0, END)


    # Variables
    current = StringVar()
    current.set(current_selected_class)

    # Objects
    class_selector_label = Label(kanna, text="Select your class: ").grid(row=0, column=0, pady=20, padx=20)
    class_selector_menu = OptionMenu(kanna, current, *classes)
    confirm_selection = Button(kanna, text="Confirm", command=kanna_confirm_selection).grid(row=0, column= 2, padx=20)
    activation_button = Button(kanna, text="Activate Autobuffer", width=60, command=kanna_activate_autobuffer).grid(row=8, column=0, columnspan=5, padx=20, pady=5)
    entry_kanna_circle_of_suppression = Entry(kanna)
    entry_kanna_haku_reborn2 = Entry(kanna)
    entry_kanna_shikigami_doppelganger = Entry(kanna)
    confirm_kanna_circle_of_suppression = Button(kanna, text="Bind", command=bind_kanna_circle_of_suppression).grid(row=1, column=2)
    confirm_kanna_haku_reborn2 = Button(kanna, text="Bind", command=bind_kanna_haku_reborn2).grid(row=2, column=2)
    confirm_kanna_shikigami_doppelganger = Button(kanna, text="Bind", command=bind_kanna_shikigami_doppelganger).grid(row=3, column=2)
    label_newbind_kanna_circle_of_suppression = Label(kanna, text=newbind_kanna_circle_of_suppression).grid(row=1, column=3)
    label_newbind_kanna_haku_reborn2 = Label(kanna, text=newbind_kanna_haku_reborn2).grid(row=2, column=3)
    label_newbind_kanna_shikigami_doppelganger = Label(kanna, text=newbind_kanna_shikigami_doppelganger).grid(row=3, column=3)


    # Image Objects
    display_kanna_circle_of_suppression = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/kanna/kanna_circle_of_suppression.png"))
    display2_kanna_circle_of_suppression = Label(image=display_kanna_circle_of_suppression).grid(row=1, column=0)
    display_kanna_haku_reborn2 = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/kanna/kanna_haku_reborn2.png"))
    displa2_kanna_haku_reborn2 = Label(image=display_kanna_haku_reborn2).grid(row=2, column=0)
    display_kanna_shikigami_doppelganger = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/kanna/kanna_shikigami_doppelganger.png"))
    display2_kanna_shikigami_doppelganger = Label(image=display_kanna_shikigami_doppelganger).grid(row=3, column=0)


    # Placement
    class_selector_menu.grid(row=0, column=1)
    entry_kanna_circle_of_suppression.grid(row=1, column=1)
    entry_kanna_haku_reborn2.grid(row=2, column=1)
    entry_kanna_shikigami_doppelganger.grid(row=3, column=1)

    kanna.mainloop()

# Kain Menu
if current_selected_class == classes[7]:
    kain = Tk()
    kain.title("Maplestory Autobuffer | Kain")
    kain.iconbitmap("C:\Python\Maplestory_autobuff_V2\Maplestory.ico")
    kain.geometry("470x170")

    kain_activation = False
    newbind_kain_dragon_fang = ("F4")
    newbind_kain_lasting_grudge = ("F5")


    def kain_confirm_selection():
        global start
        global current_selected_class
        current_selected_class = current.get()
        kain.destroy()

    def kain_activate_autobuffer():
        global kain_activation
        kain_activation = True
        kain.destroy()


    def bind_kain_dragon_fang():
        newbind_kain_dragon_fang = entry_kain_dragon_fang.get()
        label_newbind_kain_dragon_fang = Label(kain, text="    ").grid(row=1, column=3)
        label_newbind_kain_dragon_fang = Label(kain, text=newbind_kain_dragon_fang).grid(row=1, column=3)
        entry_kain_dragon_fang.delete(0, END)

    def bind_kain_lasting_grudge():
        newbind_kain_lasting_grudge = entry_kain_lasting_grudge.get()
        label_newbind_kain_lasting_grudge = Label(kain, text="    ").grid(row=2, column=3)
        label_newbind_kain_lasting_grudge = Label(kain, text=newbind_kain_lasting_grudge).grid(row=2, column=3)
        entry_kain_lasting_grudge.delete(0, END)


    # Variables
    current = StringVar()
    current.set(current_selected_class)

    # Objects
    class_selector_label = Label(kain, text="Select your class: ").grid(row=0, column=0, pady=20, padx=20)
    class_selector_menu = OptionMenu(kain, current, *classes)
    confirm_selection = Button(kain, text="Confirm", command=kain_confirm_selection).grid(row=0, column= 2, padx=20)
    activation_button = Button(kain, text="Activate Autobuffer", width=60, command=kain_activate_autobuffer).grid(row=3, column=0, columnspan=5, padx=20, pady=5)
    entry_kain_dragon_fang = Entry(kain)
    entry_kain_lasting_grudge = Entry(kain)
    confirm_kain_dragon_fang = Button(kain, text="Bind", command=bind_kain_dragon_fang).grid(row=1, column=2)
    confirm_kain_lasting_grudge = Button(kain, text="Bind", command=bind_kain_lasting_grudge).grid(row=2, column=2)
    label_newbind_kain_dragon_fang = Label(kain, text=newbind_kain_dragon_fang).grid(row=1, column=3)
    label_newbind_kain_lasting_grudge = Label(kain, text=newbind_kain_lasting_grudge).grid(row=2, column=3)


    # Image Objects
    display_kain_dragon_fang = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/kain/kain_dragon_fang.png"))
    display2_kain_dragon_fang = Label(image=display_kain_dragon_fang).grid(row=1, column=0)
    display_kain_lasting_grudge = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/kain/kain_lasting_grudge.png"))
    displa2_kain_lasting_grudge = Label(image=display_kain_lasting_grudge).grid(row=2, column=0)

    # Placement
    class_selector_menu.grid(row=0, column=1)
    entry_kain_dragon_fang.grid(row=1, column=1)
    entry_kain_lasting_grudge.grid(row=2, column=1)

    kain.mainloop()

# Mercedes Menu
if current_selected_class == classes[8]:
    mercedes = Tk()
    mercedes.title("Maplestory Autobuffer | Mercedes")
    mercedes.iconbitmap("C:\Python\Maplestory_autobuff_V2\Maplestory.ico")
    mercedes.geometry("470x135")

    mercedes_activation = False
    newbind_mercedes_elemental_knights = ("F3")

    def mercedes_confirm_selection():
        global start
        global current_selected_class
        current_selected_class = current.get()
        mercedes.destroy()

    def mercedes_activate_autobuffer():
        global mercedes_activation
        mercedes_activation = True
        mercedes.destroy()


    def bind_mercedes_elemental_knights():
        newbind_mercedes_elemental_knights = entry_mercedes_elemental_knights.get()
        label_newbind_mercedes_elemental_knights = Label(mercedes, text="    ").grid(row=1, column=3)
        label_newbind_mercedes_elemental_knights = Label(mercedes, text=newbind_mercedes_elemental_knights).grid(row=1, column=3)
        entry_mercedes_elemental_knights.delete(0, END)

    # Variables
    current = StringVar()
    current.set(current_selected_class)

    # Objects
    class_selector_label = Label(mercedes, text="Select your class: ").grid(row=0, column=0, pady=20, padx=20)
    class_selector_menu = OptionMenu(mercedes, current, *classes)
    confirm_selection = Button(mercedes, text="Confirm", command=mercedes_confirm_selection).grid(row=0, column= 2, padx=20)
    activation_button = Button(mercedes, text="Activate Autobuffer", width=60, command=mercedes_activate_autobuffer).grid(row=3, column=0, columnspan=5, padx=20, pady=5)
    entry_mercedes_elemental_knights = Entry(mercedes)
    confirm_mercedes_elemental_knights = Button(mercedes, text="Bind", command=bind_mercedes_elemental_knights).grid(row=1, column=2)
    label_newbind_mercedes_elemental_knights = Label(mercedes, text=newbind_mercedes_elemental_knights).grid(row=1, column=3)


    # Image Objects
    display_mercedes_elemental_knights = ImageTk.PhotoImage(Image.open("C:/Python/Maplestory_autobuff_V2/classes/mercedes/mercedes_elemental_knights.png"))
    display2_mercedes_elemental_knights = Label(image=display_mercedes_elemental_knights).grid(row=1, column=0)

    # Placement
    class_selector_menu.grid(row=0, column=1)
    entry_mercedes_elemental_knights.grid(row=1, column=1)

    mercedes.mainloop()

if current_selected_class == classes[0]:
    while phantom_activation == True:
        locate_phantom_heroic_memories = pyautogui.locateOnScreen(phantom_heroic_memories, confidence=0.9)
        locate_phantom_godesses_blessing = pyautogui.locateOnScreen(phantom_goddesses_blessing, confidence=0.9)
        if locate_phantom_heroic_memories != None:
            keyboard.press(str(newbind_phantom_heroic_memories))
            keyboard.release(str(newbind_phantom_heroic_memories))
        if locate_phantom_godesses_blessing != None:
            keyboard.press(str(newbind_phantom_goddesses_blessing))
            keyboard.release(str(newbind_phantom_goddesses_blessing))

if current_selected_class == classes[1]:
    while adele_activation == True:
        locate_adele_divine_wrath = pyautogui.locateOnScreen(adele_divine_wrath, confidence=0.9)
        locate_adele_goddesses_blessing = pyautogui.locateOnScreen(adele_goddesses_blessing, confidence=0.9)
        locate_adele_hunting_decree = pyautogui.locateOnScreen(adele_hunting_decree, confidence=0.9)
        locate_adele_legacy_restoration = pyautogui.locateOnScreen(adele_legacy_restoration, confidence=0.9)
        locate_adele_weapon_aura = pyautogui.locateOnScreen(adele_weapon_aura, confidence=0.9)
        locate_adele_aether_forge = pyautogui.locateOnScreen(adele_aether_forge, confidence=0.9)
        locate_adele_aetherial_arms = pyautogui.locateOnScreen(adele_aetherial_arms, confidence=0.9)
        if locate_adele_divine_wrath != None:
            keyboard.press(str(newbind_adele_divine_wrath))
            keyboard.release(str(newbind_adele_divine_wrath))
        if locate_adele_goddesses_blessing != None:
            keyboard.press(str(newbind_adele_goddesses_blessing))
            keyboard.release(str(newbind_adele_goddesses_blessing))
        if locate_adele_hunting_decree == None:
            keyboard.press(str(newbind_adele_hunting_decree))
            keyboard.release(str(newbind_adele_hunting_decree))
        if locate_adele_legacy_restoration == None:
            keyboard.press(str(newbind_adele_legacy_restoration))
            keyboard.release(str(newbind_adele_legacy_restoration))
        if locate_adele_weapon_aura != None:
            keyboard.press(str(newbind_adele_weapon_aura))
            keyboard.release(str(newbind_adele_weapon_aura))
        if locate_adele_aether_forge == None:
            keyboard.press(str(newbind_adele_aether_forge))
            keyboard.release(str(newbind_adele_aether_forge))
        if locate_adele_aetherial_arms == None:
            keyboard.press(str(newbind_adele_aetherial_arms))
            keyboard.release(str(newbind_adele_aetherial_arms))

if current_selected_class == classes[2]:
    while bishop_activation == True:
        locate_bishop_decent_hyper_body = pyautogui.locateOnScreen(bishop_divine_protection, confidence=0.9)
        locate_bishop_goddesses_blessing = pyautogui.locateOnScreen(bishop_goddesses_blessing, confidence=0.9)
        locate_bishop_epic_adventure = pyautogui.locateOnScreen(bishop_epic_adventure, confidence=0.9)
        locate_bishop_infinity = pyautogui.locateOnScreen(bishop_infinity, confidence=0.9)
        locate_bishop_magic_guard = pyautogui.locateOnScreen(bishop_magic_guard, confidence=0.9)
        locate_bishop_teleport_boost = pyautogui.locateOnScreen(bishop_teleport_boost, confidence=0.9)
        locate_bishop_teleport_mastery = pyautogui.locateOnScreen(bishop_teleport_mastery, confidence=0.9)
        if locate_bishop_divine_protection == None:
            keyboard.press(str(newbind_bishop_divine_protection))
            keyboard.release(str(newbind_bishop_divine_protection))
        if locate_bishop_goddesses_blessing != None:
            keyboard.press(str(newbind_bishop_goddesses_blessing))
            keyboard.release(str(newbind_bishop_goddesses_blessing))
        if locate_bishop_epic_adventure != None:
            keyboard.press(str(newbind_bishop_epic_adventure))
            keyboard.release(str(newbind_bishop_epic_adventure))
        if locate_bishop_infinity != None:
            keyboard.press(str(newbind_bishop_infinity))
            keyboard.release(str(newbind_bishop_infinity))
        if locate_bishop_magic_guard == None:
            keyboard.press(str(newbind_bishop_magic_guard))
            keyboard.release(str(newbind_bishop_magic_guard))
        if locate_bishop_teleport_boost == None:
            keyboard.press(str(newbind_bishop_teleport_boost))
            keyboard.release(str(newbind_bishop_teleport_boost))
        if locate_bishop_teleport_mastery == None:
            keyboard.press(str(newbind_bishop_teleport_mastery))
            keyboard.release(str(newbind_bishop_teleport_mastery))
            
if current_selected_class == classes[3]:
    while pathfinder_activation == True:
        locate_pathfinder_epic_adventure = pyautogui.locateOnScreen(pathfinder_epic_adventure, confidence=0.9)
        if locate_pathfinder_epic_adventure != None:
            keyboard.press(str(newbind_pathfinder_epic_adventure))
            keyboard.release(str(newbind_pathfinder_epic_adventure))

if current_selected_class == classes[4]:
    while luminous_activation == True:
        locate_luminous_heroic_memories = pyautogui.locateOnScreen(luminous_heroic_memories, confidence=0.9)
        locate_luminous_light_speed_boost = pyautogui.locateOnScreen(luminous_light_speed_boost, confidence=0.9)
        if locate_luminous_heroic_memories != None:
            keyboard.press(str(newbind_luminous_heroic_memories))
            keyboard.release(str(newbind_luminous_heroic_memories))
        if locate_luminous_light_speed_boost != None:
            keyboard.press(str(newbind_luminous_light_speed_boost))
            keyboard.release(str(newbind_luminous_light_speed_boost))

if current_selected_class == classes[5]:
    while evan_activation == True:
        locate_evan_decent_hyper_body = pyautogui.locateOnScreen(evan_decent_hyper_body, confidence=0.9)
        locate_evan_heroic_memories = pyautogui.locateOnScreen(evan_heroic_memories, confidence=0.9)
        locate_evan_magic_guard = pyautogui.locateOnScreen(evan_magic_guard, confidence=0.9)
        if locate_evan_decent_hyper_body != None:
            keyboard.press(str(newbind_evan_decent_hyper_body))
            keyboard.release(str(newbind_evan_decent_hyper_body))
        if locate_evan_heroic_memories != None:
            keyboard.press(str(newbind_evan_heroic_memories))
            keyboard.release(str(newbind_evan_heroic_memories))
        if locate_evan_magic_guard == None:
            keyboard.press(str(newbind_evan_magic_guard))
            keyboard.release(str(newbind_evan_magic_guard))

if current_selected_class == classes[6]:
    while kanna_activation == True:
        locate_kanna_circle_of_suppression = pyautogui.locateOnScreen(kanna_circle_of_suppression, confidence=0.9)
        locate_kanna_haku_reborn2 = pyautogui.locateOnScreen(kanna_haku_reborn2, confidence=0.9)
        locate_kanna_shikigami_doppelganger = pyautogui.locateOnScreen(kanna_shikigami_doppelganger, confidence=0.9)
        if locate_kanna_circle_of_suppression != None:
            keyboard.press(str(newbind_kanna_circle_of_suppression))
            keyboard.release(str(newbind_kanna_circle_of_suppression))
        if locate_kanna_haku_reborn2 != None:
            keyboard.press(str(newbind_kanna_haku_reborn2))
            keyboard.release(str(newbind_kanna_haku_reborn2))
        if locate_kanna_shikigami_doppelganger != None:
            keyboard.press(str(newbind_kanna_shikigami_doppelganger))
            keyboard.release(str(newbind_kanna_shikigami_doppelganger))

if current_selected_class == classes[7]:
    while kain_activation == True:
        locate_kain_dragon_fang = pyautogui.locateOnScreen(kain_dragon_fang, confidence=0.9)
        locate_kain_godesses_blessing = pyautogui.locateOnScreen(kain_lasting_grudge, confidence=0.9)
        if locate_kain_dragon_fang != None:
            keyboard.press(str(newbind_kain_dragon_fang))
            keyboard.release(str(newbind_kain_dragon_fang))
        if locate_kain_godesses_blessing != None:
            keyboard.press(str(newbind_kain_lasting_grudge))
            keyboard.release(str(newbind_kain_lasting_grudge))

if current_selected_class == classes[8]:
    while mercedes_activation == True:
        locate_mercedes_elemental_knights = pyautogui.locateOnScreen(mercedes_elemental_knights, confidence=0.9)
        if locate_mercedes_elemental_knights != None:
            keyboard.press(str(newbind_mercedes_elemental_knights))
            keyboard.release(str(newbind_mercedes_elemental_knights))
