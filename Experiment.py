### Import ###
from psychopy import visual, core, event, gui, data
import glob
import random
import pandas as pd

# define window
win_box = visual.Window(color = "white", size=(1440, 847), pos=(0,0))
win_box.flip()

### collecting basic data ###
## Get nicknames ##
# define dialogue boxes
dialog_1 = gui.Dlg(title = "Participant nicknames")
dialog_1.addText('Welcome to the experiment! First we need some data from you.\nFill out a nickname or initials for each participant below:')
dialog_1.addField("Participant 1: ")
dialog_1.addField("Participant 2: ")
dialog_1.addText('How long have you known each other?')
dialog_1.addField("Relationship length: ")

# show dialog
dialog_1.show()
if dialog_1.OK:
    # save nickname variables
    P1_nn = dialog_1.data[0]
    P2_nn = dialog_1.data[1]
    r_len = dialog_1.data[2]
elif dialog_1.Cancel:
    core.quit()

## Get info from P1 ##
# dialog instructing P2 to leave
dialog_2 = gui.Dlg(title = "{} please leave".format(P2_nn))
dialog_2.addText('{}, please get up and leave. {} has to fill out info without {} looking at the screen. {} will call {} back when instructed to do so.'.format(P2_nn, P1_nn, P2_nn, P1_nn, P2_nn))
dialog_2.show()

# dialog collecting data from P1
dialog_3 = gui.Dlg(title = "{} information".format(P1_nn))
dialog_3.addText('{}, please fill out the following information on yourself without {} being able to see the screen.'.format(P1_nn, P2_nn))
dialog_3.addField("Age:")
dialog_3.addField("Gender:", choices = ["-","Female", "Male", "Other"])
dialog_3.addField("Nationality:")
dialog_3.addText('How would you describe your relationship with {}'.format(P2_nn))
dialog_3.addField("Relationship type:", choices = ["-","Friends", "Family", "Romantic"])
dialog_3.addText('{} continue to the next task. Do NOT call {} back yet'.format(P1_nn, P2_nn))

dialog_3.show()
if dialog_3.OK:
    P1_age = dialog_3.data[0]
    P1_gender = dialog_3.data[1]
    P1_nationality = dialog_3.data[2]
    P1_r_type = dialog_3.data[3]
elif dialog_3.Cancel:
    core.quit()

win_box.close

## IOS for P1 ##
P1_IOS = 0

# define window
win_full = visual.Window(color = "white", fullscr = True)
# load stimuli
IOS_text = visual.ImageStim(win_full, image = "stimuli/IOS_text.png")
# draw img to the canvas
IOS_text.draw()
# flip the screen 
win_full.flip()
# wait for the participant to choose
key = event.waitKeys(keyList = ["1", "2", "3", "4", "5", "6", "7", "escape"])

if key[0] == "escape":
    core.quit()
elif (key[0] == "1"):
    P1_IOS = 1
elif (key[0] == "2"):
    P1_IOS = 2
elif (key[0] == "3"):
    P1_IOS = 3
elif (key[0] == "4"):
    P1_IOS = 4
elif (key[0] == "5"):
    P1_IOS = 5
elif (key[0] == "6"):
    P1_IOS = 6
elif (key[0] == "7"):
    P1_IOS = 7

# define window
win_full.close
win_box.flip()

## Get info from P2 ##
# dialog instructing P1 to leave
dialog_4 = gui.Dlg(title = "{} please leave".format(P1_nn))
dialog_4.addText('{}, please get up and leave. {} has to fill out info without {} looking at the screen. {} will call {} back when instructed to do so.'.format(P1_nn, P2_nn, P1_nn, P2_nn, P1_nn))
dialog_4.show()

# dialog collecting data from P1
dialog_5 = gui.Dlg(title = "{} information".format(P2_nn))
dialog_5.addText('{}, please fill out the following information on yourself without {} being able to see the screen.'.format(P2_nn, P1_nn))
dialog_5.addField("Age:")
dialog_5.addField("Gender:", choices = ["-","Female", "Male", "Other"])
dialog_5.addField("Nationality:")
dialog_5.addText('How would you describe your relationship with {}'.format(P1_nn))
dialog_5.addField("Relationship type:", choices = ["-","Friends", "Family", "Romantic"])
dialog_5.addText('{} continue to the next task. Do NOT call {} back yet'.format(P2_nn, P1_nn))

dialog_5.show()
if dialog_5.OK:
    P2_age = dialog_5.data[0]
    P2_gender = dialog_5.data[1]
    P2_nationality = dialog_5.data[2]
    P2_r_type = dialog_5.data[3]
elif dialog_5.Cancel:
    core.quit()

## IOS for P2 ##
P2_IOS = 0

# define window
win = visual.Window(color = "white", fullscr = True)
# load stimuli
IOS_text = visual.ImageStim(win, image = "stimuli/IOS_text.png")
# draw img to the canvas
IOS_text.draw()
# flip the screen 
win.flip()
# wait for the participant to choose
key = event.waitKeys(keyList = ["1", "2", "3", "4", "5", "6", "7", "escape"])
# Quit if escape is pressed
if key[0] == "escape":
    core.quit()
    # define P2_IOS
elif (key[0] == "1"):
    P2_IOS = 1
elif (key[0] == "2"):
    P2_IOS = 2
elif (key[0] == "3"):
    P2_IOS = 3
elif (key[0] == "4"):
    P2_IOS = 4
elif (key[0] == "5"):
    P2_IOS = 5
elif (key[0] == "6"):
    P2_IOS = 6
elif (key[0] == "7"):
    P2_IOS = 7

# define window
win = visual.Window(color = "white", size=(1440, 847), pos=(0,0))
win.flip()

### Welcome text ###
# define window
win = visual.Window(color = "white", fullscr = True)
# prepare welcome text 
text = visual.TextStim(win, text = "{}, please switch with {}. It is {}'s turn to fill out info. Press any key to continue.".format(P1_nn, P2_nn))
# draw it to the canvas
text.draw()
# flip the screen 
win.flip()
# wait for the participant to press any key
event.waitKeys()





### Welcome text ###
# define window
win = visual.Window(color = "black", fullscr = True)
# prepare welcome text 
text = visual.TextStim(win, text = "Welcome to the experiment!\nPress any key to start...")
# draw it to the canvas
text.draw()
# flip the screen 
win.flip()
# wait for the participant to press any key
event.waitKeys()

### Instruction text ###

### IOS for both participants ###

### Instruction text ###

### Practise trials ###

### Experiment ###

### Logfile ###

# get the date and time to meake unique logfilename
date = data.getDateStr()
# random ID
ID = random.randint(10000, 99999)
# name columns
columns = ["timestamp", 
    "ID", 
    "r_len",
    "P1_nn", 
    "P1_age",
    "P1_gender",
    "P1_nationality",
    "P1_r_type",
    "P1_IOS", 
    "P2_nn",
    "P2_age",
    "P2_gender",
    "P2_nationality",
    "P2_r_type",
    "P2_IOS", ]
# logfile dataframe
logfile = pd.DataFrame(columns = columns)
# logfilename
logfilename = "logfiles/{}_{}.csv".format(date, ID)

logfile = logfile.append({
    "timestamp": date,
    "ID": ID,
    "r_len" : r_len,
    "P1_nn" : P1_nn,
    "P1_age" : P1_age,
    "P1_gender" : P1_gender,
    "P1_nationality" : P1_nationality,
    "P1_r_type" : P1_r_type,
    "P1_IOS": P1_IOS,
    "P2_nn": P2_nn,
    "P2_age" : P2_age,
    "P2_gender" : P2_gender,
    "P2_nationality" : P2_nationality,
    "P2_r_type" : P2_r_type,
    "P2_IOS": P2_IOS},  ignore_index = True)


### Goodbye text ###

### Saving logfile ###
logfile.to_csv(logfilename)