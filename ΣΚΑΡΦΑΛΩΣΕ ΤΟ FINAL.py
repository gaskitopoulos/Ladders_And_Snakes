import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import random
import time

#functions for the game

def roll_dice():
    a=random.randint(1,6)
    return a


def endgame(a,b):
    if a>b:
        s="Νικητής είναι ο/η "+name1+", με τελικό σκόρ: "+str(a)+" - "+str(b)
        messagebox.showinfo("Τέλος παιχνιδιού",s)
    else:
        s="Νικητής είναι ο/η "+name2+", με τελικό σκόρ: "+str(a)+" - "+str(b)
        messagebox.showinfo("Τέλος παιχνιδιού",s)
    button_rolldice.configure(state=DISABLED)
    global replay_button
    replay_button=tk.Button(text="ΞΑΝΑΠΑΙΞΕ ΑΠΟ ΤΗΝ ΑΡΧΗ",command=replay_game,bg="#e6ccb3")
    replay_button.pack()

def replay_game():
    newgame=messagebox.askquestion("ΝΕΟ ΠΑΙΧΝΙΔΙ","Είστε βέβαιοι ότι θέλετε να ξεκινήσετε νέο παιχνίδι;\nΠρώτος παίζει ο παίκτης που έχασε στο προηγούμενο παιχνίδι.")
    if newgame=="yes":
        label_position1["text"]=0
        label_position2["text"]=0
        update_table()
        button_rolldice.configure(state=NORMAL)
        label_round["text"]=1
        replay_button.forget()
       
   
       

def update_table():
    for i in range (100):
        if label_position1["text"]==label_up[i]["text"] and label_position1["text"]!=label_position2["text"]:
            label_up[i].config(bg=color1)
            label_down[i].config(bg=color1)
                       
        elif label_position1["text"]==label_position2["text"] and label_position1["text"]==label_up[i]["text"]:
            label_up[i].config(bg=color1)
            label_down[i].config(bg=color2)
                       
        elif label_position2["text"]==label_up[i]["text"] and label_position1["text"]!=label_position2["text"]:
            label_up[i].config(bg=color2)
            label_down[i].config(bg=color2)
                       
        else:
            label_up[i].config(bg="#e6ccb3")
            label_down[i].config(bg="#e6ccb3")

def playgame():
    button_rolldice.configure(state=DISABLED)
    result=roll_dice()
    result_label.configure(text=result)
    label_dice_show2.configure(text=result)
    turn=int(label_turn["text"])
    label_turn["text"]=turn+1
    position1=int(label_position1["text"])
    position2=int(label_position2["text"])
    if int(label_turn["text"])%2==0:
        #Παίζει ο 1ος παίκτης
        for j in range(result):
            label_position1["text"]+=1
            if label_position1["text"]>99:
                label_position1["text"]=100
            update_table()
            window.update()
            time.sleep(0.5)

        if label_position1["text"] in ladders:
            x=ladder_res[ladders.index(label_position1["text"])]-ladders[ladders.index(label_position1["text"])]
            label_ladder["text"]="ΠΕΤΥΧΕΣ ΣΚΑΛΑ!"
            if x>0:
                label_ladder_move["text"]="ΑΝΕΒΑΙΝΕΙΣ "+str(abs(x))+"!"
            else:
                label_ladder_move["text"]="ΚΑΤΕΒΑΙΝΕΙΣ "+str(abs(x))+"!"
            label_ladder.grid(row=4,column=0,columnspan=2)
            label_ladder_move.grid(row=5,column=0,columnspan=2)
            window.update()
            time.sleep(1.2)
            for j in range (abs(x)):
                if x>0:
                    label_position1["text"]+=1
                else:
                    label_position1["text"]-=1
                update_table()
                window.update()
                time.sleep(0.15)
            label_ladder_move.grid_forget()
            label_ladder.grid_forget()
               
                   
               
               
    elif int(label_turn["text"])%2!=0:
        #Παίζει ο δεύτερος παίκτης
        for j in range(result):
            label_position2["text"]+=1
            if label_position2["text"]>99:
                label_position2["text"]=100
            update_table()
            window.update()
            time.sleep(0.5)

        if label_position2["text"] in ladders:
            x=ladder_res[ladders.index(label_position2["text"])]-ladders[ladders.index(label_position2["text"])]
            label_ladder["text"]="ΠΕΤΥΧΕΣ ΣΚΑΛΑ!"
            if x>0:
                label_ladder_move["text"]="ΑΝΕΒΑΙΝΕΙΣ "+str(abs(x))+"!"
            else:
                label_ladder_move["text"]="ΚΑΤΕΒΑΙΝΕΙΣ "+str(abs(x))+"!"
            label_ladder.grid(row=4,column=0,columnspan=2)
            label_ladder_move.grid(row=5,column=0,columnspan=2)
            window.update()
            time.sleep(1.2)
            for j in range (abs(x)):
                if x>0:
                    label_position2["text"]+=1
                else:
                    label_position2["text"]-=1
                update_table()
                window.update()
                time.sleep(0.15)
            label_ladder_move.grid_forget()
            label_ladder.grid_forget()

    window.update()
    if int(label_turn["text"])%2==0:
        label_name_updates.configure(text=name2)
    else:
        label_name_updates.configure(text=name1)
        label_round["text"]+=1
    label_dice_show2.configure(text="-")
    result_label.configure(text="-")
    if label_position1["text"]==100 or label_position2["text"]==100:
        endgame(label_position1["text"],label_position2["text"])
    else:
        button_rolldice.configure(state=NORMAL)
    window.update()



def play():
    global label_ladder_move,label_ladder,button_rolldice,result_label,label_dice_show2,label_turn,label_position1,label_position2,label_up,label_down,ladders,label_name_updates,label_round,ladder_res
    rules_frame.forget()
    button_frame.forget()
    mainframeplayers.forget()
    frameplayers1.forget()
    frameplayers2.forget()
    framequarter.forget()
    game_frame=tk.Frame(master=window)
    game_frame.pack()

    #***********************************************

    #declare variables and lists for the main game
   
    dice_result=0
    position1=position2=0
    label_turn=tk.Label(text="1")
    label_position1=tk.Label(text="0")
    label_position2=tk.Label(text="0")
    rounds=1
    table_spot=[]
    label_up=[]
    label_down=[]
    ladders=   [1,4,9,21,28,36,51,71,80,16,34,49,47,56,62,64,87,93,95,98]
    ladder_res=[17,14,20,41,48,46,68,90,100,6,15,24,29,53,22,60,45,73,75,77]
    list_of_numbers=[100,99,98,97,96,95,94,93,92,91,
                     81,82,83,84,85,86,87,88,89,90,
                     80,79,78,77,76,75,74,73,72,71,
                     61,62,63,64,65,66,67,68,69,70,
                     60,59,58,57,56,55,54,53,52,51,
                     41,42,43,44,45,46,47,48,49,50,
                     40,39,38,37,36,35,34,33,32,31,
                     21,22,23,24,25,26,27,28,29,30,
                     20,19,18,17,16,15,14,13,12,11,
                     1,2,3,4,5,6,7,8,9,10]

    #***********************************************

    #create the information frame on the left of the main table

    info_frame=tk.Frame(master=game_frame,bg="#804000")
    info_frame.grid(row=0,column=0,sticky="nsew")
    label_title_info=tk.Label(master=info_frame,text="Πληροφορίες παικτών",font="ARIAL 14",bg="#804000")
    label_title_info.grid(row=0,column=0,columnspan=2)
    label_name1=tk.Label(master=info_frame,text=name1,padx=2,bg="#804000",font="ARIAL 14")
    label_name1.grid(row=1,column=0)
    label_name2=tk.Label(master=info_frame,text=name2,bg="#804000",font="ARIAL 14")
    label_name2.grid(row=2,column=0)
    label_position1=tk.Label(master=info_frame,text=position1,bg=color1,padx=5,font="ARIAL 14",width=3)
    label_position1.grid(row=1,column=1)
    label_position2=tk.Label(master=info_frame,text=position2,bg=color2,padx=5,font="ARIAL 14",width=3)
    label_position2.grid(row=2,column=1)


    #***********************************************

    #create the updates frame on the rigth

    updates_frame=tk.Frame(master=game_frame,bg="#804000")
    updates_frame.grid(row=0,column=2,sticky="nsew")

    label_title_updates=tk.Label(master=updates_frame,text="Εξέλιξη παιχνιδιού",bg="#804000",font="ARIAL 14")
    label_title_updates.grid(row=0,column=0,columnspan=2,sticky="nsew")
    label_string_round=tk.Label(master=updates_frame,text="Γύρος Νο",bg="#804000",font="ARIAL 14")
    label_string_round.grid(row=1,column=0)
    label_round=tk.Label(master=updates_frame,text=rounds,bg="#804000",font="ARIAL 14")
    label_round.grid(row=1,column=1)
    label_string_name=tk.Label(master=updates_frame,text="Σειρά σου,",bg="#804000",font="ARIAL 14")
    label_string_name.grid(row=2,column=0)
    label_name_updates=tk.Label(master=updates_frame,text=name1,width=10,bg="#804000",font="ARIAL 14")
    label_name_updates.grid(row=2,column=1)
    label_dice_show1=tk.Label(master=updates_frame,text="Έφερες -->",bg="#804000",font="ARIAL 14")
    label_dice_show1.grid(row=3,column=0)
    label_dice_show2=tk.Label(master=updates_frame,text="-",bg="#804000",font="ARIAL 14")
    label_dice_show2.grid(row=3,column=1)
    label_ladder=tk.Label(master=updates_frame,text="",bg="#804000",font="ARIAL 14",fg="#e6ccb3")
    label_ladder_move=tk.Label(master=updates_frame,text="",bg="#804000",font="ARIAL 14",fg="#e6ccb3")

    #***********************************************

    #***********************************************

    #create the main table for the game

    table_frame=tk.Frame(master=game_frame,padx=150,bg="#804000")
    table_frame.grid(row=0,column=1)
    counter=0
    for i in range(10):
        for j in range(10):
            table_spot.append(tk.Frame(master=table_frame,relief="sunken",borderwidth=1,highlightbackground="black", highlightthickness=1))
            table_spot[counter].grid(row=i,column=j)
            label_up.append(tk.Label(master=table_spot[counter],text=list_of_numbers[counter],bg="#e6ccb3",fg="black",width=5))
            label_up[counter].pack()
            if i==9 and j==0:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|+16",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==9 and j==3:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|+10",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==9 and j==8:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|+11",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==7 and j==0:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|+20",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==7 and j==7:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|+20",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==6 and j==4:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|+10",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==4 and j==9:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|+17",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==2 and j==9:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|+19",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==2 and j==0:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|+20",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==8 and j==4:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|-10",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==6 and j==6:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|-19",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==5 and j==8:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|-25",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==5 and j==6:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|-18",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==4 and j==4:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|-3",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==3 and j==1:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|-40",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==3 and j==3:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|-4",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==1 and j==6:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|-42",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==0 and j==7:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|-20",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==0 and j==5:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|-20",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            elif i==0 and j==2:
                label_down.append(tk.Label(master=table_spot[counter],text="|=|-19",bg="#e6ccb3",fg="black",width=5))
                label_down[counter].pack()
            else:
                label_down.append(tk.Label(master=table_spot[counter],text="",bg="#e6ccb3",width=5))
                label_down[counter].pack()
            counter+=1


    #***********************************************

    #create the button for the dice

    dice_frame=tk.Frame(master=window,pady=50,bg="#804000")
    dice_frame.pack()
    button_rolldice=tk.Button(master=dice_frame,text="Ρίξε το ζάρι...",width=20,pady=10,command=playgame,state=NORMAL,bg="#e6ccb3")
    button_rolldice.grid(row=0,column=0)
    result_frame=tk.Frame(master=dice_frame,relief="sunken",borderwidth=1,padx=50,bg="#e6ccb3")
    result_frame.grid(row=0,column=1)
    result_label=tk.Label(master=result_frame,text=dice_result,pady=10,bg="#e6ccb3")
    result_label.pack()

#***********************************************

def register():
    rules_frame.forget()
    button_frame.forget()
    global entryname1,entryname2,color1,color2,clicked1,clicked2
    global mainframeplayers,frameplayers1,titleplayers,frameplayers2,framequarter
    mainframeplayers=tk.Frame(master=window,bg="#804000")
    mainframeplayers.pack()
    frameplayers1=tk.Frame(master=mainframeplayers,bg="#804000")
    frameplayers1.pack()
    frameplayers2=tk.Frame(master=mainframeplayers,pady=50,bg="#804000")
    frameplayers2.pack()
    colors = [
        "Μωβ",
        "Κόκκινο",
        "Πράσινο",
        "Γαλάζιο",
    ]
    clicked1 = StringVar()
    clicked2 = StringVar()
    name1=StringVar()
    name2=StringVar()
    color1=StringVar()
    color2=StringVar()
    clicked1.set("Μωβ")
    clicked2.set("Κόκκινο")
    ttk.Style().configure('pad.TEntry', padding='5 5 5 5')
    for i in range(3):
        for j in range(2):
            framequarter=tk.Frame(master=frameplayers2,bg="#804000")
            framequarter.grid(row=i,column=j)
            if i==0 and j==0:
                for k in range(2):
                    if k==0:
                        labelplayer=tk.Label(master=framequarter,text="Όνομα παίκτη 1: ",bg="#804000",font="ARIAL 14")
                        labelplayer.grid(row=k,column=j)
                    else:
                        labelplayer=tk.Label(master=framequarter,text="Όνομα παίκτη 2: ",bg="#804000",font="ARIAL 14")
                        labelplayer.grid(row=k,column=j)
            elif i==0 and j==1:
                entryname1=ttk.Entry(master=framequarter,style='pad.TEntry')
                entryname1.grid(row=0,column=j)
                entryname2=ttk.Entry(master=framequarter,style='pad.TEntry')
                entryname2.grid(row=1,column=j)
            elif i==2 and j==0:
                for k in range(2):
                    if k==0:
                        colorplayer=tk.Label(master=framequarter,text="Χρώμα παίκτη 1: ",bg="#804000",font="ARIAL 14",pady=5)
                        colorplayer.grid(row=k,column=j)
                    else:
                        colorplayer=tk.Label(master=framequarter,text="Χρώμα παίκτη 2: ",bg="#804000",font="ARIAL 14",pady=5)
                        colorplayer.grid(row=k,column=j)
            elif i==2 and j==1:
                drop1=tk.OptionMenu(framequarter,clicked1,*colors)
                drop1.config(bg="#e6ccb3",height=1,width=10,pady=5)
                drop2=tk.OptionMenu(framequarter,clicked2,*colors)
                drop2.config(bg="#e6ccb3",width=10,pady=5)
                drop1.grid(row=0,column=0)
                drop2.grid(row=1,column=0)
                   
                   
    frameplayers3=tk.Frame(master=mainframeplayers,pady=50,bg="#804000")
    frameplayers3.pack()
    submitbutton=tk.Button(master=frameplayers3,text="Καταχώρηση και ξεκινάμε",command=button_submit,bg="#e6ccb3")
    submitbutton.pack()

#************************************************************************************

def button_submit():
    if entryname1.get()=="" or entryname2.get()=="":
        show_msg_noname()
    elif (clicked1.get()==clicked2.get()):
        same_color()
    elif entryname1.get()==entryname2.get():
        show_msg_samename()
    elif len(entryname1.get())>15 or len(entryname2.get())>15:
        message_big_name()
    else:
        global name1,name2,color1,color2
        name1=entryname1.get()
        name2=entryname2.get()
        color1=register_color(clicked1.get())
        color2=register_color(clicked2.get())
        play()

def register_color(a):
    if (a=="Μωβ"):
        return "#b366ff"
    elif (a=="Κόκκινο"):
        return "#ff4718"
    elif (a=="Πράσινο"):
        return "#79ff4d"
    else:
        return "#33adff"

def show_msg_noname():
    messagebox.showinfo("Προσοχή","Δεν έχει επιλεγεί όνομα για κάποιον παίκτη.")

def same_color():
    messagebox.showinfo("Προσοχή","Έχετε επιλέξει το ίδιο χρώμα και για τους 2 παίκτες")
   
def show_msg_samename():
    messagebox.showinfo("Προσοχή","Έχετε επιλέξει το ίδιο όνομα και για τους 2 παίκτες.")

def message_big_name():
    messagebox.showinfo("Προσοχή","Τα ονόματα των παικτών πρέπει να είναι έως 15 χαρακτήρες.")


def quit_game():
    answer=messagebox.askquestion("ΕΞΟΔΟΣ", "Είστε σίγουροι για την έξοδο;")
    if answer=="yes":
        window.destroy()


#************************************************************************************

window=tk.Tk()
window.resizable(width=False,height=False)
window.state("zoomed")
window.title('ΣΚΑΡΦΑΛΩΣΕ ΤΟ')
window.configure(bg="#804000")
window.attributes('-fullscreen', True)

title_frame=tk.Frame(pady=40,bg="#804000")
title_frame.pack()
title_label=tk.Label(master=title_frame,text="ΣΚΑΡΦΑΛΩΣΕ ΤΟ",font="ARIAL 26",bg="#804000")
title_label.pack()

rules_frame=tk.Frame(pady=20,bg="#e6ccb3",relief="sunken",borderwidth=1)
rules_frame.pack()

rules_title=tk.Label(master=rules_frame,bg="#e6ccb3",font="ARIAL 18",text="ΚΑΝΟΝΕΣ ΤΟΥ ΠΑΙΧΝΙΔΙΟΥ\n")
rules_title.grid(row=0,column=0)

list_of_rules=["-Σκοπός του παιχνιδιού είναι ο παίκτης να φτάσει στο τετράγωνο [100] του ταμπλό.","-Ο κάθε παίκτης με τη σειρά ρίχνει το ζάρι και αρχίζοντας να μετράει από το τετράγωνο [1] προχωρά τόσα τετράγωνα,",
               "όσα έδειξε ο αριθμός του ζαριού.","-Εάν ο παίκτης σταματήσει σε τετράγωνο με τη σημάνηση [|=|+] τότε ανεβαίνει και φτάνει έως το σημείο που ορίζει η σκάλα.",
               "Διαφορετικά αν σταματήσει σε τετράγωνο με τη σημάνηση [|=|-] κατεβαίνει αντίστοιχα.","-Υπάρχει δυνατότητα να βρίσκονται ταυτόχρονα σε μία θέση 2 παίκτες."]

list_of_labels_for_rules=[]
for i in range(len(list_of_rules)):
    list_of_labels_for_rules.append(tk.Label(master=rules_frame,text=list_of_rules[i],fg="black",padx=5,pady=5,bg="#e6ccb3").grid(row=i+2,column=0,sticky="w"))
   
button_frame=tk.Frame(pady=40,bg="#804000")
button_frame.pack()
button_start=tk.Button(master=button_frame,text="ΠΑΜΕ ΝΑ ΞΕΚΙΝΗΣΟΥΜΕ!",bg="#e6ccb3",command=register)
button_start.pack()
button_quit=tk.Button(text="ΕΞΟΔΟΣ",command=quit_game,bg="#e6ccb3")
button_quit.place(relx=1,x=0,y=0,anchor=NE)
           

window.mainloop()
