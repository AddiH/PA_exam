### Import ###
from psychopy import visual, core, event, gui, data
import glob
import random
import pandas as pd

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
    P1nn = dialog_1.data[0]
    P2nn = dialog_1.data[1]
    r_length = dialog_1.data[2]
elif dialog_1.Cancel:
    core.quit()

## Get info from P1 ##
# dialog instructing P2 to leave
dialog_2 = gui.Dlg(title = "{} please leave".format(P2nn))
dialog_2.addText('{}, please get up and leave. {} has to fill out info without {} looking at the screen. {} will call {} back when instructed to do so'.format(P2nn, P1nn, P2nn, P1nn, P2nn))
dialog_2.show()

# dialog collecting data from P1
dialog_3 = gui.Dlg(title = "{} information".format(P1nn))
dialog_3.addText('{}, please fill out the following information on yourself without {} being able to see the screen.'.format(P1nn, P2nn))
dialog_3.addField("Age:")
dialog_3.addField("Gender:", choices = ["-","Female", "Male", "Other"])
dialog_3.addField("Nationality:")
dialog_3.addText('How would you describe your relationship with {}'.format(P2nn))
dialog_3.addField("Relationship type:", choices = ["-","Friends", "Family", "Romantic"])
dialog_3.addText('{} continue to the next task. Do NOT call {} back yet'.format(P1nn, P2nn))

dialog_3.show()
if dialog_3.OK:
    P1_age = dialog_3.data[0]
    P1_gender = dialog_3.data[1]
    P1_nationality = dialog_3.data[2]
    P1_r_type = dialog_3.data[3]
elif dialog_3.Cancel:
    core.quit()

## IOS for P1 ##


### Logfile ###

# get the date and time to meake unique logfilename
date = data.getDateStr()
# random ID
ID = random.randint(10000, 99999)
# name columns
columns = ["timestamp", "ID", "Participant 1 nickname", "Participant 2 nickname"]
# logfile dataframe
logfile = pd.DataFrame(columns = columns)
# logfilename
logfilename = "logfiles/{}_{}.csv".format(ID,date)


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
logfile = logfile.append({
    "timestamp": date,
    "ID": ID,
    "Participant 1 nickname": P1nn,
    "Participant 2 nickname": P2nn},  ignore_index = True)


### Goodbye text ###

### Saving logfile ###
logfile.to_csv(logfilename)