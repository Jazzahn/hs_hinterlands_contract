import random

ctype = ""
employer = ""
opp_ctype = ""
employers = {
                2 : "Civilian organization (rebels, militia, business group)",
                3 : "Planetary Government (the government of this specific system)",
                4 : "Mercenary subcontract",
                5 : "Corporation",
                6 : "House Government (the sovereign government that includes this system)",
                7 : "House Government",
                8 : "Noble (local)",
                9 : "Corporation",
                10 : "Plantary Government",
                11 : "House Government",
                12 : "Mercenary subcontract"
                }

ctypes = { 
            "Expedition" : ["Standard Expedition", "Pirate Hunt", "Guerilla Operation"],
            "Garrison" : ["Cadre Duty", "Standard Garrison"],
            "Raid" : "Raid",
            "Invasion" : "Invasion"
            }

opp_ctypes = { 
                "Expedition" : ["Garrison", "Raid"],
                "Garrison" : ["Expedition", "Raid", "Invasion"],
                "Raid" : ["Expedition", "Garrison", "Raid", "Invasion"],
                "Invasion" : ["Expediton", "Garrison", "Raid", "Invasion"]
                }

clength = 0

contractmods = { 
    "paymod" : 0,
    "supportmod" : 0,
    "transmod" : 0,
    "salvagemod" : 0,
    "commandmod" : 0
}

opp_contractmods = {
    "paymod" : 0,
    "supportmod" : 0,
    "oppransmod" : 0,
    "salvagemod" : 0,
    "commandmod" : 0
}


paymod = 0
supportmod = 0
transmod = 0
salvagemod = 0
commandmod = 0

opp_paymod = 0
opp_supportmod = 0
opp_transmod = 0
opp_salvagemod = 0
opp_commandmod = 0

stepstable = {
    "Base Pay" : ["50%", "55%", "60%", "70%", "80%", "90%", "100%", "110%", "120%", "130%", "150%", "175%", "200%"],
    "Command Rights" : ["Integrated", "Integrated", "Integrated", "House", "House", "House", "House", "Liaison", "Liaison", "Liaison", "Independent", "Independent", "Independent"],
    "Salvage Rights" : ["None", "None", "Exchange", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"],
    "Support Rights" : ["None", "Straight/20%", "Straight/40%", "Straight/60%", "Straight/80%", "Straight/100%", "Battle/10%", "Battle/20%", "Battle/30%", "Battle/40%", "Battle/50%", "Battle/75%", "Battle/100%"],
    "Transportation Terms" : ["0%", "0%", "0%", "0%", "0%", "25%", "50%", "75%", "100%", "100%", "100%", "100%", "100%"],
}

systems = {
    1 : ["Zoetermeer", "Baker", "Leskovik", "Dompaire", "Devin", "Antares"],
    2 : ["Babeski", "Morges", "A Place", "Vulcan", "Parakoila", "Matteo"],
    3 : ["Bountiful Harvest", "Colmar", "Koniz", "Twycross", "Waldorff", "Romulus"],
    4 : ["New Exford", "Ballynure", "Zanderij", "Trell I", "Deia", "Great X"],
    5 : ["Santana", "Blumenort", "Kooken's Pleasure Pit", "Hot Springs", "Derf", "Timkovichi"],
    6 : ["Biuque", "Roadside", "Clermont", "Black Earth", "Golandrinas", " Sargasso"]
}

def twodsix ():
    return random.randint(1,6) + random.randint(1,6)

def get_ctype ():
    global ctype
    global opp_ctype
    # global paymod
    # global supportmod
    # global transmod
    # global salvagemod
    # global commandmod
    global clength
    result = twodsix()
    print(f"type: {result}")
    if 2 <= result <= 4:
        # Expedition Result
        # supportmod =+ 1
        # commandmod =+ 2
        clength = 6
        r2 = twodsix()
        if 2 <= r2 <= 9:
            ctype = ctypes["Expedition"][0]
        elif 10 <= r2 <= 11:
            ctype = ctypes["Expedition"][1]
        else:
            ctype = ctypes["Expedition"][2]
        r3 = twodsix()
        if 2 <= r3 <= 8:
            opp_ctype = opp_ctypes["Expedition"][0]
        else:
            opp_ctype = opp_ctypes["Expedition"][1]
    elif 5 <= result <= 6:
        # Garrison Result
        # paymod =+ 1
        # transmod =+ 1
        # salvagemod =- 2
        clength = 6
        r2 = twodsix()
        if 2 <= r2 <= 5:
            ctype = ctypes["Garrison"][0]
        else:
            ctype = ctypes["Garrison"][1]
        r3 = twodsix()
        if 2 <= r3 <= 4:
            opp_ctype = opp_ctypes["Garrison"][0]
        elif 5 <= r3 <= 8:
            opp_ctype = opp_ctypes["Garrison"][1]
        else:
            opp_ctype = opp_ctypes["Garrison"][2]
    elif 7 <= result <= 9:
        # Raid Result
        # salvagemod =- 1
        clength = 3
        ctype = ctypes["Raid"]
        r2 = twodsix()
        if 2 <= r2 <= 7:
            opp_ctype = opp_ctypes["Raid"][0]
        elif 8 <= r2 <= 10:
            opp_ctype = opp_ctypes["Raid"][1]
        elif r2 == 11:
            opp_ctype = opp_ctypes["Raid"][2]
        else:
            opp_ctype = opp_ctypes["Raid"][3]    
    else:
        # Invasion Result
        # supportmod =+ 2
        # salvagemod =+ 1
        # commandmod =- 2
        ctype = ctypes["Invasion"]
        # paymod =- 1
        clength = 6
        r2 = twodsix()
        if 2 <= r2 <= 4:
            opp_ctype = opp_ctypes["Invasion"][0]
        elif 5 <= r2 <= 8:
            opp_ctype = opp_ctypes["Invasion"][1]
        elif r2 == 9:
            opp_ctype = opp_ctypes["Invasion"][2]
        else:
            opp_ctype = opp_ctypes["Invasion"][3]
    return

def get_e_mods (employer, list):
    # global paymod
    # global supportmod
    # global transmod
    # global salvagemod
    # global commandmod
    if employer == "Civilian organization (rebels, militia, business group)":
        list["paymod"] =- 2
        # paymod =- 2
        list["supportmod"] =- 2
        list["transmod"] =- 1
        list["salvagemod"] =+ 4
        list["commandmod"] =+ 4
    elif employer == "Planetary Government (the government of this specific system)" or employer == "Planetary Government":
        list["supportmod"] =+ 1
        list["salvagemod"] =+ 1
    elif employer == "Mercenary subcontract":
        list["paymod"] =- 1
        list["commandmod"] =+ 3
    elif employer == "House Government (the sovereign government that includes this system)" or employer == "House Government":
        list["paymod"] =+ 1
        list["supportmod"] =+ 2
        list["transmod"] =+ 1
        list["salvagemod"] =- 2
        list["commandmod"] =- 3
    elif employer == "Corporation":
        list["paymod"] =+ 2
        list["supportmod"] =- 2
        list["transmod"] =+ 1
        list["salvagemod"] =+ 2
    else:
        list["paymod"] =+ 0
        list["supportmod"] =+ 0
        list["transmod"] =+ 0
        list["salvagemod"] =+ 0
        list["commandmod"] =+ 0
    return

def get_c_mods (type, list):
    if type == "Expedition":
        list["supportmod"] =+ 1
        list["commandmod"] =+ 2
    elif type == "Garrison":
        list["paymod"] =+ 1
        list["transmod"] =+ 1
        list["salvagemod"] =- 2
    elif type == "Raid":
        list["salvagemod"] =- 1
    else:
        list["supportmod"] =+ 2
        list["salvagemod"] =+ 1
        list["commandmod"] =- 2
        list["paymod"] =- 1
        list["transmod"] =- 1

def get_payrate (mod):
    # global paymod
    payrate = 0
    r = twodsix()
    # print(f"pay: {r}")
    if 2 <= r <= 3:
        payrate = 3
    elif 4 <= r <= 5:
        payrate = 4
    elif 6 <= r <= 7:
        payrate = 5
    elif 8 <= r <= 9:
        payrate = 6
    elif 10 <= r <= 11:
        payrate = 7
    else:
        payrate = 8
    # print (f"payrate: {payrate}")
    # print (f"mod: {mod}")
    payrate += int(mod)
    # print(f"payrate: {payrate}")
    if payrate < 0:
        payrate = 1
    elif payrate > 13:
        payrate = 13
    # print(f"payrate: {payrate}")
    return payrate

def get_support (mod):
    # global supportmod
    support = 0
    r = twodsix()
    if 2 <= r <= 5:
        support = 3
    elif 6 <= r <= 7:
        support = 4
    elif 8 <= r <= 9:
        support = 5
    elif 10 <= r <= 11:
        support = 6
    else:
        support = 7
    support += mod
    if support < 0:
        support = 1
    elif support > 13:
        support = 13
    return support

def get_transport(mod):
    # global transmod
    transport = 0
    r = twodsix()
    if 2 <= r <= 5:
        transport = 5
    elif 6 <= r <= 7:
        transport = 6
    elif 8 <= r <= 9:
        transport = 7
    elif 10 <= r <= 11:
        transport = 8
    else:
        transport = 9
    transport += mod
    if transport < 0:
        transport = 1
    elif transport > 13:
        transport = 13
    return transport

def get_salvage(mod):
    global salvagemod
    salvage = 0
    r = twodsix()
    if 2 <= r <= 5:
        salvage = 3
    elif 6 <= r <= 7:
        salvage = 4
    elif 8 <= r <= 9:
        salvage = 5
    elif 10 <= r <= 11:
        salvage = 6
    else:
        salvage = 7
    salvage += mod
    if salvage < 0:
        salvage = 1
    elif salvage > 13:
        salvage = 13
    return salvage

def get_command(mod):
    global commandmod
    command = 0
    r = twodsix()
    if 2 <= r <= 5:
        command = 3
    elif 6 <= r <= 7:
        command = 7
    elif 8 <= r <= 9:
        command = 8
    else:
        command = 11
    command += mod
    if command < 0:
        command = 1
    elif command > 13:
        command = 13
    return command   

get_ctype()
system = systems[random.randint(1,6)][random.randint(0,5)]
employer = employers[twodsix()]
get_e_mods(employer, contractmods)
get_c_mods(ctype, contractmods)
print(f"contract mods: {contractmods}")
payrate = get_payrate(contractmods["paymod"])
command = get_command(contractmods["commandmod"])
salvagerights = get_salvage(contractmods["salvagemod"])
support = get_support(contractmods["supportmod"])
transport = get_transport(contractmods["transmod"])

opp_employer = employers[twodsix()]

get_e_mods(opp_employer, opp_contractmods)
get_c_mods(opp_ctype, opp_contractmods)

opp_payrate = get_payrate(opp_contractmods["paymod"])
opp_command = get_command(opp_contractmods["commandmod"])
opp_salvagerights = get_salvage(opp_contractmods["salvagemod"])
opp_support = get_support(opp_contractmods["supportmod"])
opp_transport = get_transport(opp_contractmods["transmod"])



print("Hinterlands Contract Generator")
print(f"Contract Type: {ctype}")
print(f"Contract Length: {clength} Months")
print(f"System: {system}")
print(f"Employer: {employer}")
print(f"Base Pay: {stepstable['Base Pay'][payrate]} ({payrate})")
print(f"Command Rights: {stepstable['Command Rights'][command]} ({command})")
print(f"Salvage Rights: {stepstable['Salvage Rights'][salvagerights]} ({salvagerights})")
print(f"Support Rights: {stepstable['Support Rights'][support]} ({support})")
print(f"Transportation Terms: {stepstable['Transportation Terms'][transport]} ({transport})")

print("\nOpposition:")
print(f"Contract Type: {opp_ctype}")
print(f"Employer: {opp_employer}")
print(f"Base Pay: {stepstable['Base Pay'][opp_payrate]} ({opp_payrate})")
print(f"Command Rights: {stepstable['Command Rights'][opp_command]} ({opp_command})")
print(f"Salvage Rights: {stepstable['Salvage Rights'][opp_salvagerights]} ({opp_salvagerights})")
print(f"Support Rights: {stepstable['Support Rights'][opp_support]} ({opp_support})")
print(f"Transportation Terms: {stepstable['Transportation Terms'][opp_transport]} ({opp_transport})")

