from colorama import Fore
import math
import time
import sys


MCR = False


def MR():
    KI = 1
    global CR_G
    global CR_2_4
    global CR_2_2
    global CR_4_2
    global CR_4_4
    global SG
    global RPV_Temp_Sub
    global RPV_Press
    global RPV_Temp
    global RPV_Temp_PN
    global RPV_Temp_Pos_Neg
    global RPV_Water_Level
    global MP
    global ESRV
    global FWP1
    global FWP2
    global SMKI
    global HPCI
    global LPCI
    global SDC1
    global SDC2
    global SCRAM
    global ARP
    CR_2_4 = 0
    CR_2_2 = 0
    CR_4_2 = 0
    CR_4_4 = 0
    SG = 0
    CR_G = "N/A"
    RPV_Temp = 23.00
    RPV_Press = 1.00
    RPV_Water_Level = 480
    MP = False
    ESRV = False
    FWP1 = False
    FWP2 = False
    SMKI = 1
    RPV_Temp_Sub = 0.00
    Start_Run = 0
    HPCI = False
    LPCI = False
    SDC1 = False
    SDC2 = False
    SCRAM = False
    ARP = True


    def Engineering_handbook():
        print("-------- Engineering handbook -------")
        print(" ")
        print("         ----Quick Start----         ")
        print(" ")
        print("1. go to the switch board using 'sm' ")
        print("2. Engage main power by entering '1' ")
        print("3. Go back to the control panel using 'e' ")
        print("4. go to the control rod selection menu using 'crs' ")
        print("5. Use 'o' to raise the control rods increasing steam pressure")
        print("6. Experiment and play with the other functions ")
        print(" ")
        print("             **CONTROLS**    ")
        print(" ")
        print("Remove selected control rod/s 10%: i ")
        print("Insert selected control rod/s 10%: o ")
        print("Switch Board: sm ")
        print("Emergency Controls: em ")
        print("Menu: m")
        print("Control Rod Selection crs ")
        print("Control Rod Withrawal/Insertion Map rm ")
        print("Alert Menu al")
        print(" ")
        print("    **STATISTICS AND CALCULATIONS**   ")
        print(" ")
        print("See 'stats.txt' for more information")


    def Switch_Menu():
        global MP
        global FWP1
        global FWP2
        global ESRV
        global SMKI
        SMKI = 1
        while SMKI == 1:
            print("---Switch menu---")
            print("")

            
            if MP == True:
                MP_name = "ON"
                print(Fore.GREEN + "1. Main Power", MP_name)
            elif MP == False:
                MP_name = "OFF"
                print(Fore.RED + "1. Main Power", MP_name)
            else:
                print(Fore.RED + "Error: invalid Switch menu status: switch 1 Main Power")

            if MP == False:
                print(" ")
            elif MP == True:
                if FWP1 == True:
                    FWP1_name = "ON"
                    print(Fore.GREEN + "2. Feed Water Pump #1", FWP1_name)
                elif FWP1 == False:
                    FWP1_name = "OFF"
                    print(Fore.RED + "2. Feed Water Pump #1", FWP1_name)
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: switch 2 FWP #1")     
            else:
                print(Fore.RED + "Error: invalid Switch menu status: switch 2 FWP #1")

            if MP == False:
                print(" ")
            elif MP == True:
                if FWP2 == True:
                    FWP2_name = "ON"
                    print(Fore.GREEN + "3. Feed Water Pump #2", FWP2_name)
                elif FWP2 == False:
                    FWP2_name = "OFF"
                    print(Fore.RED + "3. Feed Water Pump #2", FWP2_name)
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: switch 3 FWP #2")
            else:
                print(Fore.RED + "Error: invalid Switch menu status: switch 3 FWP #2")

            if MP == False:
                print(" ")
            elif MP == True:
                if ESRV == False:
                    ESRV_name = "CLOSED"
                    print(Fore.RED + "4. Emergency Steam Relif Valve", ESRV_name)
                elif ESRV == True:
                    ESRV_name = "OPEN"
                    print(Fore.GREEN + "4. Emergency Steam Relif Valve", ESRV_name)
                elif MP == False:
                    print("")
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: switch 4 ESRV") 
            else:
                print(Fore.RED + "Error: invalid Switch menu status")
            

            Switch_Commands = input(Fore.WHITE + "Command: ")

            if Switch_Commands == "1":
                if MP == True:
                    MP = False
                elif MP == False:
                    MP = True
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: switch 1 MP")

            elif Switch_Commands == "2":
                if FWP1 == True:
                    FWP1 = False
                elif FWP1 == False:
                    FWP1 = True
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: switch 2 FWP1")

            elif Switch_Commands == "3":
                if FWP2 == True:
                    FWP2 = False
                elif FWP2 == False:
                    FWP2 = True
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: switch 3 FWP2")
            
            elif Switch_Commands == "4":
                if ESRV == True:
                    ESRV = False
                elif ESRV == False:
                    ESRV = True
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: switch 1 ESRV")
            elif Switch_Commands == "e":
                SMKI = 2

            for i in range(10):
                print("")


    def Emergency_Menu():

        global HPCI
        global LPCI
        global SDC1
        global SDC2
        global SCRAM
        global ARP
        SMKI = 1
        while SMKI == 1:
            print(Fore.WHITE + "---Emergency Control---")
            if SCRAM == True:
                print(Fore.RED + "SCRAM TRIGGERED")
            else:
                print(Fore.WHITE + " ")
            if MP == False:
                print(" ")
            elif MP == True:
                if HPCI == True:
                    HPCI_name = "ON"
                    print(Fore.GREEN + "1. High pressure core injection ", HPCI_name)
                elif HPCI == False:
                    HPCI_name = "OFF"
                    print(Fore.RED + "1. High pressure core injection ", HPCI_name)
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: Emergency switch status HPCI")

            elif MP == False:
                print(" ")
            elif MP == True:
                if LPCI == True:
                    LPCI_name = "ON"
                    print(Fore.GREEN + "2. Low pressure core injection ", LPCI_name)
                elif LPCI == False:
                    LPCI_name = "OFF"
                    print(Fore.RED + "2. Low pressure core injection ", LPCI_name)
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: Emergency switch status LPCI")

            if MP == False:
                print(" ")
            elif MP == True:
                if SDC1 == True:
                    SDC1_name = "ON"
                    print(Fore.GREEN + "3. Shutdown Cooling Pump #1 ", SDC1_name)
                elif SDC1 == False:
                    SDC1_name = "OFF"
                    print(Fore.RED + "3. Shutdown Cooling Pump #1 ", SDC1_name)
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: Emergency switch status SDC1")

            if MP == False:
                print(" ")
            elif MP == True:
                if SDC2 == True:
                    SDC2_name = "ON"
                    print(Fore.GREEN + "4. Shutdown Cooling Pump #2 ", SDC2_name)
                elif SDC2 == False:
                    SDC2_name = "OFF"
                    print(Fore.RED + "4. Shutdown Cooling Pump #2 ", SDC2_name)
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: Emergency switch status SDC2")

            if MP == False:
                print(" ")
            elif MP == True:
                if SCRAM == True:
                    SCRAM_name = "ON"
                    print(Fore.GREEN + "5. Single Control Rod Axe Man ", SCRAM_name)
                elif SCRAM == False:
                    SCRAM_name = "OFF"
                    print(Fore.RED + "5. Single Control Rod Axe Man ", SCRAM_name)
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: Emergency switch status SCRAM")

            if MP == False:
                print(" ")
            elif MP == True:
                if ARP == True:
                    ARP_name = "ON"
                    print(Fore.GREEN + "6. Automatic Reactor Protection", ARP_name)
                elif ARP == False:
                    ARP_name = "OFF"
                    print(Fore.RED + "6. Automatic Reactor Protection", ARP_name)
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: Emergency switch status ARP")
                    
            Emergency_Commands = input(Fore.WHITE + "Command: ")

            if Emergency_Commands == "1":
                if HPCI == True:
                    HPCI = False
                elif HPCI == False:
                    HPCI = True
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: Emergency Switch 1 HPCI")
            
            elif Emergency_Commands == "2":   
                if LPCI == True:
                    LPCI = False
                elif LPCI == False:
                    LPCI = True
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: Emergency Switch 2 LPCI")

            elif Emergency_Commands == "3":   
                if SDC1 == True:
                    SDC1 = False
                elif SDC1 == False:
                    SDC1 = True
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: emergency switch 3 SDC1")

            elif Emergency_Commands == "4":   
                if SDC2 == True:
                    SDC2 = False
                elif SDC2 == False:
                    SDC2 = True
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: emergency switch 4 SDC2")

            elif Emergency_Commands == "5":
                if SCRAM == False:
                    print(Fore.RED + "SCRAM TRIGGERED")
                    SCRAM = True
                elif SCRAM == True:
                    SCRAM = False
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: emergency switch 5 SCRAM")
                
            elif Emergency_Commands == "6":
                if ARP == False:
                    print(Fore.RED + "ARP SET")
                    ARP = True
                elif ARP == True:
                    print(Fore.RED + "ARP DISABLED")
                    ARP = False
                else:
                    print(Fore.RED + "Error: invalid Switch menu status: emergency switch 5 SCRAM")
                
                


            elif Emergency_Commands == "e":
                SMKI = 2
            for i in range(10):
                print("")


    def CR_mode_select():
        if MP == True:
            MP_name = "GROUP"
            print(Fore.GREEN + "1. Movement mode", MP_name)
        if MP == False:
            MP_name = "SINGLE"
            print(Fore.RED + "1. Movement mode", MP_name)
        else:
            print(Fore.RED + "Error: invalid control rod mode select status: switch 1 Movement mode")


    def CR_Select():
        global CR_G
        if MP == False:
            print(" ")
        elif MP == True:
            print("---Control Rod Select---")
            print(" ")
            print("1. Group 1 (2-4)")
            print("2. Group 2 (2-2)")
            print("3. Group 3 (4-2)")
            print("4. Group 4 (4-4)")
            print("5. Automatic")

            CR_Select = input("Command: ")

            if CR_Select == "1":
                CR_G = "2-4"
            elif CR_Select == "2":
                CR_G = "2-2"
            elif CR_Select == "3":
                CR_G = "4-2"
            elif CR_Select == "4":
                CR_G = "4-4"
            elif CR_Select == "5":
                WIP()
            else:
                print("error lol")
                input(":")


    def Detail_Rod_Map():
        if MP == False:
            print(" ")
        elif MP == True:
            print("Rod 2-4: ", CR_4_2, "Rod 4-4: ", CR_4_4)
            print(" ")
            print("Rod 2-2: ", CR_2_2, "Rod 4-2: ", CR_4_2)
            print("")
            input("Press enter to continue")


    def Check_E_Switches():
        global HPCI
        global LPCI
        global SDC1
        global SDC2
        global CR_2_4
        global CR_2_2
        global CR_4_2
        global CR_4_4
        if MP == False:
            print(" ")
        elif MP == True:
            if HPCI == True:
                RPV_Water_Level = RPV_Water_Level + 30
                RPV_Temp_Sub = RPV_Temp_Sub + 20
            elif LPCI == True:
                if RPV_Press > 0.2:
                    RPV_Water_Level = RPV_Water_Level + 30
                    RPV_Temp_Sub = RPV_Temp_Sub + 20
            elif SDC1 == True:
                RPV_Water_Level = RPV_Water_Level + 30
                RPV_Temp_Sub = RPV_Temp_Sub + 20
                print(Fore.RED + "Shutdown initiated")
            elif SDC2 == True:
                RPV_Water_Level = RPV_Water_Level + 30
                RPV_Temp_Sub = RPV_Temp_Sub + 20
                print(Fore.RED + "Shutdown initiated")
            elif SCRAM == True:
                if CR_2_4 > 0:
                    while CR_2_4 > 0:
                        CR_2_4 = CR_2_4 - 100
                if CR_2_2 > 0:
                    while CR_2_2 > 0:
                        CR_2_2 = CR_2_2 - 100
                if CR_4_2> 0:
                    while CR_4_2 > 0:
                        CR_4_2 = CR_4_2 - 100
                if CR_4_4 > 0:
                    while CR_4_4 > 0:
                        CR_4_4 = CR_4_4 - 100
                        
            for i in range(10):
                print("")
        

    def check_switches(RPV_Water_Level):
        global RPV_Temp_Sub
        if FWP1 == True:
            RPV_Temp_Sub = RPV_Temp_Sub + 0.005
            RPV_Water_Level = RPV_Water_Level + 10
        if FWP2 == True:
            RPV_Temp_Sub = RPV_Temp_Sub + 0.005
            RPV_Water_Level = RPV_Water_Level + 10
        if RPV_Temp < 100:
            RPV_Water_Level = RPV_Water_Level - RPV_Temp/1000
        if ESRV == True:
            RPV_Press - 0.5
        

    def find_reactivity():
        global Reactivity
        A = CR_2_4 + CR_2_2 + CR_4_2 + CR_4_4
        CRW_mean = A/4
        R1 = CRW_mean * 10
        Reactivity = R1 * 2.5


    def find_water_level():
        global RPV_Water_Level
        if FWP1 == True:
            RPV_Water_Level = RPV_Water_Level + 10
        elif FWP2 == True:
            RPV_Water_Level = RPV_Water_Level + 10
        if RPV_Temp > 100:
            if RPV_Press > 1.0:
                while RPV_Press > 1.0:
                    RPV_Water_Level - 0.5


    def find_temp():
        global RPV_Temp
        global RPV_Temp_PN
        global R_div1000
        global RPV_Temp_Pos_Neg
        global RPV_Temp_Sub
        RPV_Temp_Sub
        R_div1000 = Reactivity/1000
        RPV_Temp_PN = (Reactivity/1000) - RPV_Temp_Sub
        if RPV_Temp_PN > 0:
            str(RPV_Temp_PN)
            RPV_Temp_Pos_Neg = "+"
        elif RPV_Temp_PN < 0:
            str(RPV_Temp_PN)
            RPV_Temp_Pos_Neg = "-"
        elif RPV_Temp_PN == 0:
            RPV_Temp_Pos_Neg = "*****"
        RPV_Temp = RPV_Temp + R_div1000
        RPV_Temp = RPV_Temp - RPV_Temp_Sub
        RPV_Temp = round(RPV_Temp, 2)


    def find_press(RPV_Temp):
        global RPV_Press
        Press = 1.0
        if RPV_Temp > 98:
            a = 8.14019
            b = 1810.94
            c = 244.485
            d = b/(c+RPV_Temp)
            NLp = a - d
            RPV_Press = math.log10(NLp)
            RPV_Press = RPV_Press + 0.88
            RPV_Press = round(RPV_Press, 2)
            
        elif RPV_Temp < 99:
            x = 8.07131
            y = 1730.63
            z = 233.426
            e = y/(z+RPV_Temp)
            NLp = x - e
            RPV_Press = math.log10(NLp)
        RPV_Press = RPV_Press + 0.88
        RPV_Press = round(RPV_Press, 2)


    def Print_CRW(CR_G):
        if CR_G == "2-4":
            print("Control rod withdrawal: ",CR_2_4, "%" )
        elif CR_G == "4-2":
            print("Control rod withdrawal: ",CR_4_2, "%" )
        elif CR_G == "2-2":
            print("Control rod withdrawal: ",CR_2_2, "%" )
        elif CR_G == "4-4":
            print("Control rod withdrawal: ",CR_4_4, "%" )
        elif CR_G == "N/A":
            print("Not applicable")


    def Alert_List():
        pass

    def Check_params():
        pass


    def Alert_Pop(x):
        pass


    def Reactor_Start_Up():
        global CR_2_4
        global CR_4_2
        global CR_2_2
        global CR_4_4
        global RPV_Temp
        global RPV_Press
        global MP
        if Start_Run == 1:
            RPV_Temp = 500
            MP = True
        else:
            pass
        while KI < 2:

            find_reactivity()
            find_temp()
            find_press(RPV_Temp)
            find_water_level()
            check_switches(RPV_Water_Level)

            Check_E_Switches()

            print(Fore.WHITE + "---MCR SL Control Room---")
            print("")
            if MP == False:
                for i in range(6):
                    print("")
                    
            elif MP == True:
                Print_CRW(CR_G)
                print("Selected group: ", CR_G)
                print("Reactor Period: ", RPV_Temp_Pos_Neg, RPV_Temp_PN)
                print("RPV Temp: ", RPV_Temp, " C˚")
                print("RPV Pressure: ", RPV_Press, " Bar ")
                print("RPV Reactivity: ", Reactivity, "C/S")
                print("RPV Water Level: ", RPV_Water_Level, "Cm")
            DC = input("Command: ")
            if DC == "sm":
                for i in range(13):
                    print("")
                Switch_Menu()
            if MP == False:
                    print("")
            elif MP == True:
                for i in range(6):
                    print("")

                if DC == "o":
                    if MCR == True:
                        if CR_G == "2-4":
                            if CR_2_4 == 100:
                                print(Fore.RED + "Control rod withdrawal block")
                                time.sleep(1.5)
                            else:
                                CR_2_4 = CR_2_4 + 10
                        elif CR_G == "2-2":
                            if CR_2_2 == 100:
                                print(Fore.RED + "Control rod withdrawal block")
                                time.sleep(1.5)
                            else:
                                CR_2_2 = CR_2_2 + 10
                        elif CR_G == "4-2":
                            if CR_4_2 == 100:
                                print(Fore.RED + "Control rod withdrawal block")
                                time.sleep(1.5)
                            else:
                                CR_4_2 = CR_4_2 + 10
                        elif CR_G == "4-4":
                            if CR_4_4 == 100:
                                print(Fore.RED + "Control rod withdrawal block")
                                time.sleep(1.5)
                            else:
                                CR_4_4 = CR_4_4 + 10
                        else:
                            print(Fore.RED + "No Control Group Selected")
                            time.sleep(1.5)

                elif DC == "i":
                    if CR_G == "2-4":
                        if CR_2_4 == 0:
                            print(Fore.RED + "Control rod insertion block")
                            time.sleep(2.5)
                        else:
                            CR_2_4 = CR_2_4 - 10
                    elif CR_G == "2-2":
                        if CR_2_2 == 0:
                            print(Fore.RED + "Control rod insertion block")
                            time.sleep(2.5)
                        else:
                            CR_2_2 = CR_2_2 - 10
                    elif CR_G == "2-4":
                        if CR_2_4 == 0:
                            print(Fore.RED + "Control rod insertion block")
                            time.sleep(2.5)
                        else:
                            CR_2_4 = CR_2_4 - 10
                    elif CR_G == "4-4":
                        if CR_4_4 == 0:
                            print(Fore.RED + "Control rod insertion block")
                            time.sleep(2.5)
                        else:
                            CR_4_4 = CR_4_4 - 10
                    else:
                        print(Fore.RED + "No Control Group Selected")
                        time.sleep(1.5)

                elif DC == "crs":
                    CR_Select()

                elif DC == "rm":
                    Detail_Rod_Map()

                elif DC == "e":
                    break

                elif DC == "m":
                    start_up()

                elif DC == "em":
                    Emergency_Menu()
                
                elif DC == "al":
                    Alert_List()

                elif DC == "crm":
                    CR_mode_select()

                elif DC == "sdm":
                    if RPV_Temp <= 30:
                        print("Shutting down for maintainance ")
                        MP = False

                elif DC == "":
                    pass

                else:
                    print(Fore.RED + "Invalid command")

            else:
                print("error")


    def Reactor_Running_params():
        global Start_Run
        global MP
        Start_Run = 1
        MP = True
        Reactor_Start_Up()


    def start_up():
        for i in range(7):
            print(" ")
        print("---MCR SL---")
        print("1. Reactor start up")
        print("2. Reactor running")
        print("3. Engineering handbook ")
        print("4. Exit")

        IC = input("Select Option: ")


        print("Option: " + IC)
        for i in range(13):
            print("")

        if IC == "1":
            Reactor_Start_Up()
        elif IC == "2":
            Reactor_Running_params()
        elif IC == "3":
            Engineering_handbook()
        elif IC == "4":
            try:
                sys.exit()
            except SystemExit:
                print('Program closing')
    start_up()


def Latest_update():
        print("Python Nuclear Reactor Simulations Alpha V2.110")
        print("")
        print("Update 2.100")
        print("Minor update")
        print(" - Added an alert list function (non functional)")
        print(" - Added Automatic function for control rod selection (non functional)")
        print(" - Fixed emergency menu")
        print(" - Added SCRAM functionality")
        print("")
        print("For other updates check the website ")
        print("https://953c79e5-39d5-4a15-87a3-766858879983-00-grkngghqv6j4.janeway.replit.dev/")
        print("ask me to start it up")
        print("")


def WIP():
    print("This is Work In Progress ")
    print("it doesnt work cos im dumb")


def Mode_Select():
    for i in range(10):
        print(" ")
    print("Python Nuclear Reactor Simulations Alpha V2.100")
    print("")
    print("---Mode Select---")
    print("1. Single Control Rod Mode")
    print("2. Multiple Control Rod Mode (Small 5x5 Core)")
    print("3. Multiple Control Rod Mode (Large *x* Core)")
    print("4. Update log ")
    print("")

    MS_Command = input("Command: ")

    if MS_Command == "1":
        MCR = False
    elif MS_Command == "2":
        MCR = True
    elif MS_Command == "3":
        WIP()
    elif MS_Command == "4":
        Latest_update()


Mode_Select()