#################
# Participant 1 is RIGHT/BLUE/"P" KEY
# Participant 2 is LEFT/YELLOW/"W" KEY
#################


### Import ###
from psychopy import visual, core, event, gui, data
import random
import pandas as pd

### Collecting basic data ###
# define white box window
win_box = visual.Window(color = "white", size=(1440, 847), pos=(0,0))

## Get nicknames ##
# define dialogue box
dialog_1 = gui.Dlg(title = "Participant nicknames")
dialog_1.addText('Welcome to the experiment! First we need some data from you.\nFill out a nickname or initials for each participant below:')
dialog_1.addField("Participant 1: ")
dialog_1.addField("Participant 2: ")
dialog_1.addText('How many years have you known each other?')
dialog_1.addField("Relationship length: ")

# show dialog 1
dialog_1.show()
if dialog_1.OK:
    # save variables
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
dialog_3.addText('Please confirm that you have normal or corrected to normal vision, that you are right handed and not coloblind.')
dialog_3.addField("Are you left or right handed?", choices = ["-", "Right", "Left", "Ambidextrous"])
dialog_3.addField("Is your vision normal or corrected to normal?", choices = ["-", "Yes", "No"])
dialog_3.addField("Are you colorblind?", choices = ["-", "No", "Yes", "Yes, but I can clearly tell the difference between blue and yellow"])
dialog_3.addField("Age:")
dialog_3.addField("Gender:", choices = ["-","Female", "Male", "Other"])
dialog_3.addField("Nationality:")
dialog_3.addText('How would you describe your relationship with {}?'.format(P2_nn))
dialog_3.addField("Relationship type:", choices = ["-","Friends", "Family", "Romantic"])
dialog_3.addText('{} continue to the next task. Do NOT call {} back yet'.format(P1_nn, P2_nn))

dialog_3.show()
if dialog_3.OK:
    P1_handedness = dialog_3.data[0]
    P1_vision = dialog_3.data[1]
    P1_colorvision= dialog_3.data[2]
    P1_age = dialog_3.data[3]
    P1_gender = dialog_3.data[4]
    P1_nationality = dialog_3.data[5]
    P1_r_type = dialog_3.data[6]
elif dialog_3.Cancel:
    core.quit()

## IOS for P1 ##

# load IOS
IOS_text = visual.ImageStim(win_box, image = "stimuli/IOS_text.png")
# draw to canvas
IOS_text.draw()
# flip the screen 
win_box.flip()

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

# reset to white screen
win_box.flip()

## Get info from P2 ##
# dialog instructing P1 to leave
dialog_4 = gui.Dlg(title = "{} please leave".format(P1_nn))
dialog_4.addText('{}, please get up and leave. {} has to fill out info without {} looking at the screen. {} will call {} back when instructed to do so.'.format(P1_nn, P2_nn, P1_nn, P2_nn, P1_nn))
dialog_4.show()

# dialog collecting data from P2
dialog_5 = gui.Dlg(title = "{} information".format(P1_nn))
dialog_5.addText('{}, please fill out the following information on yourself without {} being able to see the screen.'.format(P1_nn, P2_nn))
dialog_5.addText('Please confirm that you have normal or corrected to normal vision, that you are right handed and not coloblind.')
dialog_5.addField("Are you left or right handed?", choices = ["-", "Right", "Left", "Ambidextrous"])
dialog_5.addField("Is your vision normal or corrected to normal?", choices = ["-", "Yes", "No"])
dialog_5.addField("Are you colorblind?", choices = ["-", "No", "Yes", "Yes, but I can clearly tell the difference between blue and yellow"])
dialog_5.addField("Age:")
dialog_5.addField("Gender:", choices = ["-","Female", "Male", "Other"])
dialog_5.addField("Nationality:")
dialog_5.addText('How would you describe your relationship with {}?'.format(P2_nn))
dialog_5.addField("Relationship type:", choices = ["-","Friends", "Family", "Romantic"])
dialog_5.addText('{} continue to the next task. Do NOT call {} back yet'.format(P1_nn, P2_nn))

dialog_5.show()
if dialog_5.OK:
    P2_handedness = dialog_5.data[0]
    P2_vision = dialog_5.data[1]
    P2_colorvision= dialog_5.data[2]
    P2_age = dialog_5.data[5]
    P2_gender = dialog_5.data[4]
    P2_nationality = dialog_5.data[5]
    P2_r_type = dialog_5.data[6]
elif dialog_5.Cancel:
    core.quit()

## IOS for P2 ##

IOS_text.draw()
win_box.flip()

key = event.waitKeys(keyList = ["1", "2", "3", "4", "5", "6", "7", "escape"])

if key[0] == "escape":
    core.quit()
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

### Welcome text ###
# define window
win = visual.Window(color = "black", fullscr = True)

# prepare welcome text 
text = visual.TextStim(win, text = "Welcome to the experiment! \n {} please sit to the right of the computer, and place your right index finger on the P button. \n {} please sit on the left and place your left index finger on the W button. \n Press spacebar to continue.".format(P1_nn, P2_nn))
text.draw()
win.flip()
event.waitKeys(keyList = ["space"])
text = visual.TextStim(win, text = "A circle will be shown on the screen.\n {} will press P when the circle is blue. \n {} will press W when the circle is yellow. \n Please answer as fast as possible, while still answering correctly.\n Press spacebar to start the practise trials.".format(P1_nn, P2_nn))
text.draw()
win.flip()
event.waitKeys(keyList = ["space"])

### Instruction text ###

### Practise trials ###
# Load in all stimuli
BR = visual.ImageStim(win, image = "stimuli/BR.png")
BL = visual.ImageStim(win, image = "stimuli/BL.png")
YR = visual.ImageStim(win, image = "stimuli/YR.png")
YL = visual.ImageStim(win, image = "stimuli/YL.png")
BM = visual.ImageStim(win, image = "stimuli/BM.png")
YM= visual.ImageStim(win, image = "stimuli/YM.png")
f_cross = visual.ImageStim(win, image = "stimuli/fix_cross.png")
#
## Include 2 of each stimuli in pactise trials
#prac_order = [BR, BL, YR, YL, BM, YM] * 2
## randomise order
#random.shuffle(prac_order)
#
#for stim in prac_order:
#    f_cross.draw()
#    win.flip()
#    core.wait(1)
#    stim.draw()
#    win.flip()
#    # wait for the participant to press W or P or esc
#    key = event.waitKeys(keyList = ["w", "p", "escape"], maxWait=(1.5))
#
## if escape if pressed - end the experiment
#    # if no key is pressed, show "too slow"
#    if key == None:
#        text = visual.TextStim(win, text = "Too slow")
#        text.draw()
#        win.flip()
#        core.wait(2)
#    # if esc is pressed quit the experiment
#    elif key[0] == "escape":
#        core.quit()
#    # if w is pressed when a  yellow circle is shown, show "correct"
#    elif (key [0] == "w" and (stim == YR or stim == YL or stim == YM)):
#        text = visual.TextStim(win, text = "Correct", color = "green")
#        text.draw()
#        win.flip()
#        core.wait(2)
#    # if p is pressed when a  blue circle is shown, show "correct"
#    elif (key [0] == "p" and (stim == BR or stim == BL or stim == BM)):
#        text = visual.TextStim(win, text = "Correct", color = "green")
#        text.draw()
#        win.flip()
#        core.wait(2)
#    # if the wrong key is pressed, show "error"
#    else:  
#        text = visual.TextStim(win, text = "Error", color = "red")
#        text.draw()
#        win.flip()
#        core.wait(2)


### Logfile ###
# name columns
columns = ["timestamp", 
    "experiment_ID", 
    "subject",
    "r_len",
    "handedness",
    "vision",
    "colorvision",
    "age",
    "gender",
    "nationality",
    "r_type",
    "IOS", 
    "key_press",
    "rt",
    "trial_stim"]
# logfile dataframe
logfile = pd.DataFrame(columns = columns)
# get the date and time to meake unique logfilename
date = data.getDateStr()
# random ID for each experiment
exp_ID = random.randint(10000, 99999)
# random ID for each participant
P1_ID = random.randint(10000, 99999)
P2_ID = random.randint(10000, 99999)

### Experiment ### 
## Welcome text ##
text = visual.TextStim(win, text = "Good job! Press spacebar to continue to the experiment.")
text.draw()
win.flip()
event.waitKeys(keyList = ["space"])

## actual block of trials
#real_trials = [BR, BL, YR, YL] * 14
#filler_trials = [BM, YM] * 7
#order = real_trials + filler_trials
#random.shuffle(order)

# short version for testing
real_trials = [BR, BL, YR, YL]
filler_trials = [BM, YM]
order = real_trials + filler_trials
random.shuffle(order)

# define stopwatch
stopwatch = core.Clock()

## Experiment loop
for stim in order:
    f_cross.draw()
    win.flip()
    core.wait(1.5)
    stim.draw() 
    win.flip()
    # reset stopwatch and start recording
    stopwatch.reset()
    # wait for the participant to press W or P or esc
    key = event.waitKeys(keyList = ["w", "p", "escape"], maxWait=(1.5))
    # get the reaction time
    rt = stopwatch.getTime()
    # black screen for 1 second
    win.flip()
    core.wait(1)
    
        # record trial type
    if stim == BR:
        trial_stim = "BR"
    if stim == BL:
        trial_stim = "BL"
    if stim == YR:
        trial_stim = "YR"
    if stim == YL:
        trial_stim = "YL"
    if stim == BM:
        trial_stim = "BM"
    if stim == YM:
        trial_stim = "YM"

    # if participant did not press anything within 1.5 seconds, recod "none" key press
    if key == None:
        logfile = logfile.append({
            "timestamp" : date, 
            "experiment_ID" : exp_ID, 
            "subject" : "none",
            "r_len" : r_len,
            "handedness" : "none",
            "vision" : "none",
            "colorvision" : "none",
            "age" : "none",
            "gender" : "none",
            "nationality" : "none",
            "r_type" : "none",
            "IOS" : "none", 
            "key_press" : "none",
            "rt" : rt,
            "trial_stim" : trial_stim},  ignore_index = True)
    # if escape if pressed - end the experiment
    elif key[0] == "escape":
        core.quit()
    # record w an p keypress
    elif key [0] == "w":
        logfile = logfile.append({
            "timestamp" : date, 
            "experiment_ID" : exp_ID, 
            "subject" : P2_ID,
            "r_len" : r_len,
            "handedness" : P2_handedness,
            "vision" : P2_vision,
            "colorvision" : P2_colorvision,
            "age" : P2_age,
            "gender" : P2_gender,
            "nationality" : P2_nationality,
            "r_type" : P2_r_type,
            "IOS" : P2_IOS, 
            "key_press" : "w",
            "rt" : rt,
            "trial_stim" : trial_stim},  ignore_index = True)
    elif key [0] == "p":
        logfile = logfile.append({
            "timestamp" : date, 
            "experiment_ID" : exp_ID, 
            "subject" : P1_ID,
            "r_len" : r_len,
            "handedness" : P1_handedness,
            "vision" : P1_vision,
            "colorvision" : P1_colorvision,
            "age" : P1_age,
            "gender" : P1_gender,
            "nationality" : P1_nationality,
            "r_type" : P1_r_type,
            "IOS" : P1_IOS, 
            "key_press" : "p",
            "rt" : rt,
            "trial_stim" : trial_stim},  ignore_index = True)

### Saving logfile ###
# logfilename
logfilename = "logfiles/{}_{}.csv".format(date, exp_ID)
logfile.to_csv(logfilename)

### Goodbye text ###
text = visual.TextStim(win, text = "Thank you for your participation!")
text.draw()
win.flip()
core.wait(6)
core.quit()