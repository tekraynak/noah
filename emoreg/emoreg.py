#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b12),
    on Thu Feb 28 08:15:00 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.0b12'
expName = 'emoreg_test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/tekraynak/Box/TEK/NOAH/psychopy/emoreg/emoreg.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "look_instructions"
look_instructionsClock = core.Clock()
import numpy as np
look_text = visual.TextStim(win=win, name='look_text',
    text='LOOK = pay attention to the picture and allow yourself to respond naturally to it',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "decrease_instructions"
decrease_instructionsClock = core.Clock()

decrease_text = visual.TextStim(win=win, name='decrease_text',
    text='DECREASE = think of something to tell yourself about the picture that makes you feel less negative',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "rate_instructions"
rate_instructionsClock = core.Clock()

rate_instructions_img = visual.ImageStim(
    win=win, name='rate_instructions_img',
    image='images/emoreg_rating_scale.png', mask=None,
    ori=0, pos=(0, 0), size=(2,2.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ready"
readyClock = core.Clock()
ready_text = visual.TextStim(win=win, name='ready_text',
    text='Press your thumb when you are ready to begin.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "wait_for_scanner"
wait_for_scannerClock = core.Clock()
waiting_for_scanner_text = visual.TextStim(win=win, name='waiting_for_scanner_text',
    text='waiting for scanner ...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);


# Initialize components for Routine "cue"
cueClock = core.Clock()

cue_instruction = visual.TextStim(win=win, name='cue_instruction',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "image"
imageClock = core.Clock()

show_image = visual.ImageStim(
    win=win, name='show_image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.75,1.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "rate"
rateClock = core.Clock()

rating_image = visual.ImageStim(
    win=win, name='rating_image',
    image='images/emoreg_rating_scale.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')


# Initialize components for Routine "end"
endClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='THANK YOU!',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "look_instructions"-------
t = 0
look_instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
win.setColor('green')
look_end = event.BuilderKeyResponse()
# keep track of which components have finished
look_instructionsComponents = [look_text, look_end]
for thisComponent in look_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "look_instructions"-------
while continueRoutine:
    # get current time
    t = look_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *look_text* updates
    if t >= 0.0 and look_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        look_text.tStart = t
        look_text.frameNStart = frameN  # exact frame index
        look_text.setAutoDraw(True)
    
    # *look_end* updates
    if t >= 0.0 and look_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        look_end.tStart = t
        look_end.frameNStart = frameN  # exact frame index
        look_end.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if look_end.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in look_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "look_instructions"-------
for thisComponent in look_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "look_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "decrease_instructions"-------
t = 0
decrease_instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
win.setColor('blue')
decrease_end = event.BuilderKeyResponse()
# keep track of which components have finished
decrease_instructionsComponents = [decrease_text, decrease_end]
for thisComponent in decrease_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "decrease_instructions"-------
while continueRoutine:
    # get current time
    t = decrease_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *decrease_text* updates
    if t >= 0.0 and decrease_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        decrease_text.tStart = t
        decrease_text.frameNStart = frameN  # exact frame index
        decrease_text.setAutoDraw(True)
    
    # *decrease_end* updates
    if t >= 0.0 and decrease_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        decrease_end.tStart = t
        decrease_end.frameNStart = frameN  # exact frame index
        decrease_end.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if decrease_end.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in decrease_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "decrease_instructions"-------
for thisComponent in decrease_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "decrease_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "rate_instructions"-------
t = 0
rate_instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
win.setColor('black')
rate_end = event.BuilderKeyResponse()
# keep track of which components have finished
rate_instructionsComponents = [rate_end, rate_instructions_img]
for thisComponent in rate_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "rate_instructions"-------
while continueRoutine:
    # get current time
    t = rate_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *rate_end* updates
    if t >= 0.0 and rate_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        rate_end.tStart = t
        rate_end.frameNStart = frameN  # exact frame index
        rate_end.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if rate_end.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *rate_instructions_img* updates
    if t >= 0.0 and rate_instructions_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        rate_instructions_img.tStart = t
        rate_instructions_img.frameNStart = frameN  # exact frame index
        rate_instructions_img.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rate_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rate_instructions"-------
for thisComponent in rate_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "rate_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ready_end = event.BuilderKeyResponse()
# keep track of which components have finished
readyComponents = [ready_text, ready_end]
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ready"-------
while continueRoutine:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready_text* updates
    if t >= 0.0 and ready_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready_text.tStart = t
        ready_text.frameNStart = frameN  # exact frame index
        ready_text.setAutoDraw(True)
    
    # *ready_end* updates
    if t >= 0.0 and ready_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready_end.tStart = t
        ready_end.frameNStart = frameN  # exact frame index
        ready_end.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ready_end.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wait_for_scanner"-------
t = 0
wait_for_scannerClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
scanner_trigger = event.BuilderKeyResponse()

# keep track of which components have finished
wait_for_scannerComponents = [scanner_trigger, waiting_for_scanner_text]
for thisComponent in wait_for_scannerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "wait_for_scanner"-------
while continueRoutine:
    # get current time
    t = wait_for_scannerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *scanner_trigger* updates
    if t >= 0.0 and scanner_trigger.status == NOT_STARTED:
        # keep track of start time/frame for later
        scanner_trigger.tStart = t
        scanner_trigger.frameNStart = frameN  # exact frame index
        scanner_trigger.status = STARTED
        # keyboard checking is just starting
    if scanner_trigger.status == STARTED:
        theseKeys = event.getKeys(keyList=['asciicircum'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *waiting_for_scanner_text* updates
    if t >= 0.0 and waiting_for_scanner_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        waiting_for_scanner_text.tStart = t
        waiting_for_scanner_text.frameNStart = frameN  # exact frame index
        waiting_for_scanner_text.setAutoDraw(True)
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_for_scannerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait_for_scanner"-------
for thisComponent in wait_for_scannerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# set interal clock time for when scanner is triggered
scannerTriggerOnset = globalClock.getTime()
thisExp.addData('scannerTriggerOnset', scannerTriggerOnset)
# the Routine "wait_for_scanner" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../emoreg/emoreg_procedure_list.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "cue"-------
    t = 0
    cueClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    cueOnset = globalClock.getTime() - scannerTriggerOnset
    thisExp.addData('cueOnset', np.round(cueOnset, 2))
    
    if instruction == "LOOK":
        win.setColor('green')  # or 'blue' or whatever
        instructionIsLook = 1
        instructionIsDecrease = 0
    elif instruction == "DECREASE":
        win.setColor('blue')
        instructionIsLook = 0
        instructionIsDecrease = 1
        
    thisExp.addData('instruction', instruction)
    thisExp.addData('instructionIsLook', instructionIsLook)
    thisExp.addData('instructionIsDecrease', instructionIsDecrease)
    
    
    cue_instruction.setText(instruction)
    # keep track of which components have finished
    cueComponents = [cue_instruction]
    for thisComponent in cueComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "cue"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = cueClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *cue_instruction* updates
        if t >= 0.0 and cue_instruction.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue_instruction.tStart = t
            cue_instruction.frameNStart = frameN  # exact frame index
            cue_instruction.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if cue_instruction.status == STARTED and t >= frameRemains:
            cue_instruction.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cue"-------
    for thisComponent in cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    cueOffset = globalClock.getTime() - scannerTriggerOnset
    thisExp.addData('cueOffset', np.round(cueOffset, 2))
    
    
    # ------Prepare to start Routine "image"-------
    t = 0
    imageClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    imageOnset = globalClock.getTime() - scannerTriggerOnset
    thisExp.addData('imageOnset', np.round(imageOnset, 2))
    show_image.setImage(image)
    # keep track of which components have finished
    imageComponents = [show_image]
    for thisComponent in imageComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "image"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = imageClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *show_image* updates
        if t >= 0.0 and show_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            show_image.tStart = t
            show_image.frameNStart = frameN  # exact frame index
            show_image.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if show_image.status == STARTED and t >= frameRemains:
            show_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in imageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "image"-------
    for thisComponent in imageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    imageOffset = globalClock.getTime() - scannerTriggerOnset
    thisExp.addData('imageOffset', np.round(imageOffset, 2))
    
    # ------Prepare to start Routine "rate"-------
    t = 0
    rateClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    rateOnset = globalClock.getTime() - scannerTriggerOnset
    thisExp.addData('rateOnset', np.round(rateOnset, 2))
    
    win.setColor('black')
    emo_rating = event.BuilderKeyResponse()
    # keep track of which components have finished
    rateComponents = [rating_image, emo_rating]
    for thisComponent in rateComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "rate"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rateClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *rating_image* updates
        if t >= 0.0 and rating_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_image.tStart = t
            rating_image.frameNStart = frameN  # exact frame index
            rating_image.setAutoDraw(True)
        frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rating_image.status == STARTED and t >= frameRemains:
            rating_image.setAutoDraw(False)
        
        # *emo_rating* updates
        if t >= 0.0 and emo_rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            emo_rating.tStart = t
            emo_rating.frameNStart = frameN  # exact frame index
            emo_rating.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(emo_rating.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if emo_rating.status == STARTED and t >= frameRemains:
            emo_rating.status = STOPPED
        if emo_rating.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if emo_rating.keys == []:  # then this was the first keypress
                    emo_rating.keys = theseKeys[0]  # just the first key pressed
                    emo_rating.rt = emo_rating.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rate"-------
    for thisComponent in rateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rateOffset = globalClock.getTime() - scannerTriggerOnset
    thisExp.addData('rateOffset', np.round(rateOffset, 2))
    # check responses
    if emo_rating.keys in ['', [], None]:  # No response was made
        emo_rating.keys=None
    trials.addData('emo_rating.keys',emo_rating.keys)
    if emo_rating.keys != None:  # we had a response
        trials.addData('emo_rating.rt', emo_rating.rt)
    
    # ------Prepare to start Routine "rest"-------
    t = 0
    restClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    restOnset = globalClock.getTime() - scannerTriggerOnset
    thisExp.addData('restOnset', np.round(restOnset, 2))
    
    
    # need to fix drift across trials
    restOffsetShouldBe = np.round(cueOnset, 0) + 2 + 7 + 4 + rest_duration
    restDurationWithPad = restOffsetShouldBe - restOnset
    
    thisExp.addData('restDurationWithPad', restDurationWithPad)
    thisExp.addData('restOffsetShouldBe', restOffsetShouldBe)
    
    
    # keep track of which components have finished
    restComponents = [ISI]
    for thisComponent in restComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "rest"-------
    while continueRoutine:
        # get current time
        t = restClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(restDurationWithPad)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    restOffset = globalClock.getTime() - scannerTriggerOnset
    thisExp.addData('restOffset', np.round(restOffset, 2))
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [end_text]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if t >= 0.0 and end_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_text.tStart = t
        end_text.frameNStart = frameN  # exact frame index
        end_text.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if end_text.status == STARTED and t >= frameRemains:
        end_text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)








# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
