#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b12),
    on Tue Mar 19 16:48:51 2019
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
expName = 'stroop'  # from the Builder filename that created this script
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
    originPath='/Users/tek31/Box/TEK/NOAH/psychopy/stroop/stroop.py',
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

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
import numpy as np

######################################################
# EXPERIMENTAL PARAMETERS THAT THE USER CAN MANIPULATE:
######################################################

# set number of blocks in experiment (default = 4)
# NOTE: one block = rest + incongruent + rest + congruent
numBlocks = 4

# set duration (sec) for incongruent/congruent blocks (default = 60, must be divisible by 10)
blockLength = 60

# set duration (sec) for rest periods (default = 10, must be divisible by 10)
# note this will be padded with a few varying seconds
restDuration = 10

######################################################
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='    instructions:\n\npress "space" to start',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "wait_for_scanner"
wait_for_scannerClock = core.Clock()
# current trigger: ^ (shift+6)
waiting_for_scanner_text = visual.TextStim(win=win, name='waiting_for_scanner_text',
    text='waiting for scanner ...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "rest_begin"
rest_beginClock = core.Clock()
rest_begin_crosshair = visual.TextStim(win=win, name='rest_begin_crosshair',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
# for 1st trial of task (during 1st incongruent block), allowed response time is 5 seconds
allowedRT = 5

# set 'consecutive correct/incorrect' variables for ITI yoking
numConsecutiveCorrect = 0
numConsecutiveIncorrect = 0

target_stim = visual.TextStim(win=win, name='target_stim',
    text='default text',
    font='Arial',
    pos=(0, .3), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
word1 = visual.TextStim(win=win, name='word1',
    text='default text',
    font='Arial',
    pos=(-.6, -.2), height=.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
word2 = visual.TextStim(win=win, name='word2',
    text='default text',
    font='Arial',
    pos=(-.2, -.2), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
word3 = visual.TextStim(win=win, name='word3',
    text='default text',
    font='Arial',
    pos=(.2, -.2), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
word4 = visual.TextStim(win=win, name='word4',
    text='default text',
    font='Arial',
    pos=(.6, -.2), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()

target_stim_cont = visual.TextStim(win=win, name='target_stim_cont',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
word1_cont = visual.TextStim(win=win, name='word1_cont',
    text='default text',
    font='Arial',
    pos=(-.6, -.2), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
word2_cont = visual.TextStim(win=win, name='word2_cont',
    text='default text',
    font='Arial',
    pos=(-.2, -.2), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
word3_cont = visual.TextStim(win=win, name='word3_cont',
    text='default text',
    font='Arial',
    pos=(.2, -.2), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
word4_cont = visual.TextStim(win=win, name='word4_cont',
    text='default text',
    font='Arial',
    pos=(.6, -.2), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
feedback1 = visual.TextStim(win=win, name='feedback1',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
feedback2 = visual.TextStim(win=win, name='feedback2',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
respCircle = visual.Polygon(
    win=win, name='respCircle',
    edges=100000, size=(0.1, 0.1),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-8.0, interpolate=True)

# Initialize components for Routine "rest_end"
rest_endClock = core.Clock()

rest_end_crosshair = visual.TextStim(win=win, name='rest_end_crosshair',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end"
endClock = core.Clock()

end_text = visual.TextStim(win=win, name='end_text',
    text='THANK YOU!',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

instructions_key = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [instructions_text, instructions_key]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *instructions_text* updates
    if t >= 0.0 and instructions_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_text.tStart = t
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.setAutoDraw(True)
    
    # *instructions_key* updates
    if t >= 0.0 and instructions_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_key.tStart = t
        instructions_key.frameNStart = frameN  # exact frame index
        instructions_key.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if instructions_key.status == STARTED:
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
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
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
        event.clearEvents(eventType='keyboard')
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
stroop_block_condition_order = data.TrialHandler(nReps=numBlocks, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli/stroop_block_order_4nums.csv'),
    seed=None, name='stroop_block_condition_order')
thisExp.addLoop(stroop_block_condition_order)  # add the loop to the experiment
thisStroop_block_condition_order = stroop_block_condition_order.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStroop_block_condition_order.rgb)
if thisStroop_block_condition_order != None:
    for paramName in thisStroop_block_condition_order:
        exec('{} = thisStroop_block_condition_order[paramName]'.format(paramName))

for thisStroop_block_condition_order in stroop_block_condition_order:
    currentLoop = stroop_block_condition_order
    # abbreviate parameter names if possible (e.g. rgb = thisStroop_block_condition_order.rgb)
    if thisStroop_block_condition_order != None:
        for paramName in thisStroop_block_condition_order:
            exec('{} = thisStroop_block_condition_order[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rest_begin"-------
    t = 0
    rest_beginClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    rest_beginComponents = [rest_begin_crosshair]
    for thisComponent in rest_beginComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "rest_begin"-------
    while continueRoutine:
        # get current time
        t = rest_beginClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_begin_crosshair* updates
        if t >= 0.0 and rest_begin_crosshair.status == NOT_STARTED:
            # keep track of start time/frame for later
            rest_begin_crosshair.tStart = t
            rest_begin_crosshair.frameNStart = frameN  # exact frame index
            rest_begin_crosshair.setAutoDraw(True)
        frameRemains = 0.0 + restDuration- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rest_begin_crosshair.status == STARTED and t >= frameRemains:
            rest_begin_crosshair.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rest_beginComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest_begin"-------
    for thisComponent in rest_beginComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "rest_begin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trial_list = data.TrialHandler(nReps=4, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(TrialList),
        seed=None, name='trial_list')
    thisExp.addLoop(trial_list)  # add the loop to the experiment
    thisTrial_list = trial_list.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_list.rgb)
    if thisTrial_list != None:
        for paramName in thisTrial_list:
            exec('{} = thisTrial_list[paramName]'.format(paramName))
    
    for thisTrial_list in trial_list:
        currentLoop = trial_list
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_list.rgb)
        if thisTrial_list != None:
            for paramName in thisTrial_list:
                exec('{} = thisTrial_list[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        
        ### RT and ITI ###
        # for 1st trial of task (during 1st incongruent block), allowed response time is 5 seconds
        # for 2nd trial, record the prior RT and add 300ms to it for subsequent trials
        # for trial 2-n, use titration methods below
        if Condition == 'Incongruent' and stroop_block_condition_order.thisN == 0 and trial_list.thisN == 1:
            if resp.keys:
                allowedRT = resp.rt + .3
            else: # if for some reason there is not a respone on trial 1
                allowedRT = 5000 
        
        # for CONGRUENT blocks, set ITI to the mean ITI of the prior incongruent block
        if Condition == 'Congruent' and trial_list.thisN == 0:
            if np.isfinite(meanRT):
                allowedRT = meanRT
            else:
                allowedRT = 5000
        
        # for INCONGRUENT blocks, titrate allowed reaction time (ITI)
        # if participant is correct 3 trials in a row, shorten allowed time by 300ms
        # if participant is incorrect 3 trials in a row, lengthen allowed time by 300ms
        if Condition == 'Incongruent':
            if numConsecutiveCorrect >= 3:
                allowedRT = allowedRT - .3
            if numConsecutiveIncorrect >= 3:
                allowedRT = allowedRT + .3
        
        # do not allow the ITI to get too long or too short
        if allowedRT < .4:
            allowedRT = .4
        elif allowedRT > 5:
            allowedRT = 5
        
        # record onset times for each block and trial (measured within block)
        # first, record clock as block onset for when it is the first trial
        if trial_list.thisN == 0: 
            blockOnset = globalClock.getTime() - scannerTriggerOnset
        # second, record clock as trial onset
        trialOnset = globalClock.getTime() - scannerTriggerOnset - blockOnset
        
        # log timing variables for manipulation checks
        thisExp.addData('blockOnset', blockOnset)
        thisExp.addData('trialOnset', trialOnset)
        
        
        target_stim.setColor(targetcolor, colorSpace='rgb')
        target_stim.setText(target
)
        word1.setColor(w1color, colorSpace='rgb')
        word1.setText(w1)
        word2.setColor(w2color, colorSpace='rgb')
        word2.setText(w2)
        word3.setColor(w3color, colorSpace='rgb')
        word3.setText(w3)
        word4.setColor(w4color, colorSpace='rgb')
        word4.setText(w4)
        resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        trialComponents = [target_stim, word1, word2, word3, word4, resp]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *target_stim* updates
            if t >= 0.0 and target_stim.status == NOT_STARTED:
                # keep track of start time/frame for later
                target_stim.tStart = t
                target_stim.frameNStart = frameN  # exact frame index
                target_stim.setAutoDraw(True)
            frameRemains = allowedRT - win.monitorFramePeriod * 0.75  # most of one frame period left
            if target_stim.status == STARTED and t >= frameRemains:
                target_stim.setAutoDraw(False)
            
            # *word1* updates
            if t >= 0.0 and word1.status == NOT_STARTED:
                # keep track of start time/frame for later
                word1.tStart = t
                word1.frameNStart = frameN  # exact frame index
                word1.setAutoDraw(True)
            frameRemains = allowedRT - win.monitorFramePeriod * 0.75  # most of one frame period left
            if word1.status == STARTED and t >= frameRemains:
                word1.setAutoDraw(False)
            
            # *word2* updates
            if t >= 0.0 and word2.status == NOT_STARTED:
                # keep track of start time/frame for later
                word2.tStart = t
                word2.frameNStart = frameN  # exact frame index
                word2.setAutoDraw(True)
            frameRemains = allowedRT - win.monitorFramePeriod * 0.75  # most of one frame period left
            if word2.status == STARTED and t >= frameRemains:
                word2.setAutoDraw(False)
            
            # *word3* updates
            if t >= 0.0 and word3.status == NOT_STARTED:
                # keep track of start time/frame for later
                word3.tStart = t
                word3.frameNStart = frameN  # exact frame index
                word3.setAutoDraw(True)
            frameRemains = allowedRT - win.monitorFramePeriod * 0.75  # most of one frame period left
            if word3.status == STARTED and t >= frameRemains:
                word3.setAutoDraw(False)
            
            # *word4* updates
            if t >= 0.0 and word4.status == NOT_STARTED:
                # keep track of start time/frame for later
                word4.tStart = t
                word4.frameNStart = frameN  # exact frame index
                word4.setAutoDraw(True)
            frameRemains = allowedRT - win.monitorFramePeriod * 0.75  # most of one frame period left
            if word4.status == STARTED and t >= frameRemains:
                word4.setAutoDraw(False)
            
            # *resp* updates
            if t >= 0.0 and resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp.tStart = t
                resp.frameNStart = frameN  # exact frame index
                resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = allowedRT - win.monitorFramePeriod * 0.75  # most of one frame period left
            if resp.status == STARTED and t >= frameRemains:
                resp.status = STOPPED
            if resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if resp.keys == []:  # then this was the first keypress
                        resp.keys = theseKeys[0]  # just the first key pressed
                        resp.rt = resp.clock.getTime()
                        # was this 'correct'?
                        if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                            resp.corr = 1
                        else:
                            resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # calculate mean running (1) accuracy and (2) reaction time
        # first, create arrays to store these data (overwrite during every new block)
        if trial_list.thisN == 0:
            rt_list = []
            corr_list = []
            numConsecutiveCorrect = 0
            numConsecutiveIncorrect = 0
        
        # if participant responds during the trial, add the RT to the running list
        if resp.keys:
            rt_list.append(resp.rt)
        corr_list.append(resp.corr)
        
        meanRT = np.mean(rt_list)
        meanAccuracy = np.mean(corr_list)
        
        # calculate # of consecutive correct / incorrect responses (for yoking incongruent trials)
        if resp.corr:
            numConsecutiveCorrect = numConsecutiveCorrect + 1
            numConsecutiveIncorrect = 0
        else:
            numConsecutiveCorrect = 0
            numConsecutiveIncorrect = numConsecutiveIncorrect + 1
        
        # export variables
        thisExp.addData('allowedRT', allowedRT)
        thisExp.addData('meanRT', meanRT)
        thisExp.addData('meanAccuracy', meanAccuracy)
        thisExp.addData('numConsecutiveCorrect', numConsecutiveCorrect)
        thisExp.addData('numConsecutiveIncorrect', numConsecutiveIncorrect)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys=None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trial_list (TrialHandler)
        trial_list.addData('resp.keys',resp.keys)
        trial_list.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            trial_list.addData('resp.rt', resp.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedback"-------
        t = 0
        feedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # set length of feedback window
        # for incongruent blocks, make it 1 sec
        # for congruent blocks, to control for motor response differences, pad the feedback so there are as many congruent trials as incongruent trials
        if Condition == 'Incongruent':
            feedbackLength = 1
        elif Condition == 'Congruent':
            conTrialLength = (blockLength - restDurationPad) / numCompletedTrials
            conTrialLength = np.floor(conTrialLength*10)/10 # round down to 1 decimal point
            thisExp.addData('conTrialLength', conTrialLength)
            if resp.keys:
                feedbackLength = conTrialLength - resp.rt
            else:
                feedbackLength = conTrialLength - allowedRT
        thisExp.addData('feedbackLength', feedbackLength)
        
        #############################################################################
        
        # create array of x coordinates for displaying feedback components
        xPos = [-.6, -.2, .2, .6]
        
        # two values of the xPos we want to use
        # 1) position of the correct answer
        xPosCorrAns = xPos[int(corrAns)-1]
        # 2) position of the participant's response (see below)
        
        # show feedback
        if resp.keys: 
            showCircle = 1 # show the circle component
            xPosResp = xPos[int(resp.keys)-1] # x position for displaying circle/✓/X
            msg_size = .5
            if resp.corr: # CORRECT RESPONSE
                msg = "✓" 
                msg_color = 'white'
                msg_size = .3
                yPosResp = -.3 # display ✓ just below the numbers
                msg2 = '' # do not show the correct response on a delay
            elif resp.corr == 0:
                msg = "X"
                msg_color = 'red'
                msg_size = .5 # make the X a little bigger
                yPosResp = 0 # display X directly over the numbers
                msg2 = "✓" # show the correct response on a delay
        else:# NO RESPONSE (note, resp.keys will be blank)
            showCircle = 0 # set circle component to transparent (Tim - any better way to do this?)
            target = '' # remove all stimuli
            w1 = '' # remove all stimuli
            w2 = '' # remove all stimuli
            w3 = '' # remove all stimuli
            w4 = '' # remove all stimuli
            msg = "TOO LATE!"
            msg_color = 'white'
            xPosResp = 0 # center feedback
            yPosResp = 0 # center feedback
            msg_size = .3 # make "TOO LATE" a little smaller than X
            msg2 = '' # do not show the correct response on a delay
        target_stim_cont.setColor(targetcolor, colorSpace='rgb')
        target_stim_cont.setPos((0,.3))
        target_stim_cont.setText(target)
        word1_cont.setColor(w1color, colorSpace='rgb')
        word1_cont.setText(w1)
        word2_cont.setColor(w2color, colorSpace='rgb')
        word2_cont.setText(w2)
        word3_cont.setColor(w3color, colorSpace='rgb')
        word3_cont.setText(w3)
        word4_cont.setColor(w4color, colorSpace='rgb')
        word4_cont.setText(w4)
        feedback1.setColor(msg_color, colorSpace='rgb')
        feedback1.setPos((xPosResp, yPosResp))
        feedback1.setText(msg)
        feedback1.setHeight(msg_size)
        feedback2.setPos((xPosCorrAns, -.3))
        feedback2.setText(msg2)
        respCircle.setOpacity(showCircle)
        respCircle.setPos((xPosResp, -.6))
        # keep track of which components have finished
        feedbackComponents = [target_stim_cont, word1_cont, word2_cont, word3_cont, word4_cont, feedback1, feedback2, respCircle]
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "feedback"-------
        while continueRoutine:
            # get current time
            t = feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *target_stim_cont* updates
            if t >= 0 and target_stim_cont.status == NOT_STARTED:
                # keep track of start time/frame for later
                target_stim_cont.tStart = t
                target_stim_cont.frameNStart = frameN  # exact frame index
                target_stim_cont.setAutoDraw(True)
            frameRemains = feedbackLength - win.monitorFramePeriod * 0.75  # most of one frame period left
            if target_stim_cont.status == STARTED and t >= frameRemains:
                target_stim_cont.setAutoDraw(False)
            
            # *word1_cont* updates
            if t >= 0.0 and word1_cont.status == NOT_STARTED:
                # keep track of start time/frame for later
                word1_cont.tStart = t
                word1_cont.frameNStart = frameN  # exact frame index
                word1_cont.setAutoDraw(True)
            frameRemains = feedbackLength - win.monitorFramePeriod * 0.75  # most of one frame period left
            if word1_cont.status == STARTED and t >= frameRemains:
                word1_cont.setAutoDraw(False)
            
            # *word2_cont* updates
            if t >= 0.0 and word2_cont.status == NOT_STARTED:
                # keep track of start time/frame for later
                word2_cont.tStart = t
                word2_cont.frameNStart = frameN  # exact frame index
                word2_cont.setAutoDraw(True)
            frameRemains = feedbackLength - win.monitorFramePeriod * 0.75  # most of one frame period left
            if word2_cont.status == STARTED and t >= frameRemains:
                word2_cont.setAutoDraw(False)
            
            # *word3_cont* updates
            if t >= 0.0 and word3_cont.status == NOT_STARTED:
                # keep track of start time/frame for later
                word3_cont.tStart = t
                word3_cont.frameNStart = frameN  # exact frame index
                word3_cont.setAutoDraw(True)
            frameRemains = feedbackLength - win.monitorFramePeriod * 0.75  # most of one frame period left
            if word3_cont.status == STARTED and t >= frameRemains:
                word3_cont.setAutoDraw(False)
            
            # *word4_cont* updates
            if t >= 0.0 and word4_cont.status == NOT_STARTED:
                # keep track of start time/frame for later
                word4_cont.tStart = t
                word4_cont.frameNStart = frameN  # exact frame index
                word4_cont.setAutoDraw(True)
            frameRemains = feedbackLength - win.monitorFramePeriod * 0.75  # most of one frame period left
            if word4_cont.status == STARTED and t >= frameRemains:
                word4_cont.setAutoDraw(False)
            
            # *feedback1* updates
            if t >= 0.0 and feedback1.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback1.tStart = t
                feedback1.frameNStart = frameN  # exact frame index
                feedback1.setAutoDraw(True)
            frameRemains = feedbackLength - win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedback1.status == STARTED and t >= frameRemains:
                feedback1.setAutoDraw(False)
            
            # *feedback2* updates
            if t >= .5 and feedback2.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback2.tStart = t
                feedback2.frameNStart = frameN  # exact frame index
                feedback2.setAutoDraw(True)
            frameRemains = feedbackLength - win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedback2.status == STARTED and t >= frameRemains:
                feedback2.setAutoDraw(False)
            
            # *respCircle* updates
            if t >= 0 and respCircle.status == NOT_STARTED:
                # keep track of start time/frame for later
                respCircle.tStart = t
                respCircle.frameNStart = frameN  # exact frame index
                respCircle.setAutoDraw(True)
            frameRemains = feedbackLength - win.monitorFramePeriod * 0.75  # most of one frame period left
            if respCircle.status == STARTED and t >= frameRemains:
                respCircle.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # block lengths should not go over allotted time (usually 60 sec)
        # if there is not enough time for a new trial, then terminate routine
        if globalClock.getTime() - scannerTriggerOnset - blockOnset + allowedRT + feedbackLength > blockLength:
            trial_list.finished = True
            continueRoutine = False
        
        
        # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 4 repeats of 'trial_list'
    
    
    # ------Prepare to start Routine "rest_end"-------
    t = 0
    rest_endClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # record number of trials completed in the block - need this for yoking congruent blocks
    numCompletedTrials = trial_list.thisN
    thisExp.addData('numCompletedTrials', numCompletedTrials)
    
    # need to 'pad' the resting baseline duration since trial blocks end a few seconds early
    restOnset = globalClock.getTime() - scannerTriggerOnset
    restDurationPad = ((np.ceil(restOnset/10))*10) - restOnset
    
    thisExp.addData('restOnset', restOnset)
    thisExp.addData('thisRestDuration', restDuration + restDurationPad)
    
    # keep track of which components have finished
    rest_endComponents = [rest_end_crosshair]
    for thisComponent in rest_endComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "rest_end"-------
    while continueRoutine:
        # get current time
        t = rest_endClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *rest_end_crosshair* updates
        if t >= 0.0 and rest_end_crosshair.status == NOT_STARTED:
            # keep track of start time/frame for later
            rest_end_crosshair.tStart = t
            rest_end_crosshair.frameNStart = frameN  # exact frame index
            rest_end_crosshair.setAutoDraw(True)
        frameRemains = restDurationPad - win.monitorFramePeriod * 0.75  # most of one frame period left
        if rest_end_crosshair.status == STARTED and t >= frameRemains:
            rest_end_crosshair.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rest_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest_end"-------
    for thisComponent in rest_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "rest_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed numBlocks repeats of 'stroop_block_condition_order'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
endOnset = globalClock.getTime() - scannerTriggerOnset
thisExp.addData('endOnset', endOnset)
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
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
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
