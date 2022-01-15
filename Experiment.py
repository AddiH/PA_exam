### Import ###
from psychopy import visual, core, event, gui, data
import glob
import random
import pandas as pd

### GUI collecting data ###
# define dialogue box
dialog = gui.Dlg(title = "Participant nicknames")
dialog.addField("Participant 1 nickname: ")
dialog.addField("Participant 2 nickname: ")

# show dialog
dialog.show()
if dialog.OK:
    P1nn = dialog.data[0]
    P2nn = dialog.data[1]
elif dialog.Cancel:
    core.quit()



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