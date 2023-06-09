#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.3),
    on Апрель 03, 2021, at 14:43
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import os  # handy system and path functions

import pandas as pd
from psychopy import gui, visual, core, data, logging
from psychopy.constants import (NOT_STARTED, STARTED, FINISHED)
from psychopy.hardware import keyboard

outputDF = pd.DataFrame()
outputDF['null1'] = ['null']
outputDF['null2'] = ['null']
outputDF['null3'] = ['null']
outputDF['null4'] = ['null']
outputDF['null5'] = ['null']
outputDF['null6'] = ['null']

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.3'
expName = 'main'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
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
                                 originPath='C:\\Users\\Rusel\\Downloads\\Эксперимент\\main_lastrun.py',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction1"
instruction1Clock = core.Clock()
instructin_text = visual.TextStim(win=win, name='instructin_text',
                                  text='Сейчас перед вами будут появлятся фотографии внимательно рассмотртите их\nДля продолжения нажмите пробел',
                                  font='Arial',
                                  pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                  color='white', colorSpace='rgb', opacity=1.0,
                                  languageStyle='LTR',
                                  depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
image1floor = visual.ImageStim(
    win=win,
    name='image1floor',
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "sleep"
sleepClock = core.Clock()
text = visual.TextStim(win=win, name='text',
                       text=None,
                       font='Open Sans',
                       pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
                       color='white', colorSpace='rgb', opacity=None,
                       languageStyle='LTR',
                       depth=0.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instruction_text = visual.TextStim(win=win, name='instruction_text',
                                   text='Вам будет предъявлен ряд вопросов о Вас. \n\nВопросы с вариантами ответов предполагают выбор одного из пунктов. Открытые вопросы –– самостоятельный ввод ответа.\n\nВаша задача будет заключаться в том, чтобы дать ответы на все вопросы.\n\nНажмите spacebar или enter для продолжения',
                                   font='Arial',
                                   pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                   color='white', colorSpace='rgb', opacity=None,
                                   languageStyle='LTR',
                                   depth=0.0);
instr_resp = keyboard.Keyboard()

# Initialize components for Routine "question1"
question1Clock = core.Clock()
question_text1 = visual.TextStim(win=win, name='question_text1',
                                 text='Пол.\n\n1. Мужской\n2. Женский\n\nВыберите в соответствии с числом.',
                                 font='Arial',
                                 pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                 color='white', colorSpace='rgb', opacity=1.0,
                                 languageStyle='LTR',
                                 depth=0.0);
resp1 = keyboard.Keyboard()

# Initialize components for Routine "question2_4"
question2_4Clock = core.Clock()
answer_text2_4 = visual.TextBox2(
    win, text='', font='Arial',
    pos=(0, 0), letterHeight=0.05,
    size=None, borderWidth=1.0,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=False, italic=False,
    lineSpacing=0.5,
    padding=None,
    anchor='center',
    fillColor=None, borderColor=None,
    flipHoriz=False, flipVert=False,
    editable=True,
    name='answer_text2_4',
    autoLog=True,
)
question_text2_4 = visual.TextStim(win=win, name='question_text2_4',
                                   text='',
                                   font='Arial',
                                   pos=(0, .3), height=0.05, wrapWidth=None, ori=0.0,
                                   color='white', colorSpace='rgb', opacity=1.0,
                                   languageStyle='LTR',
                                   depth=-1.0);
resp2_4 = keyboard.Keyboard()
instr2_4 = visual.TextStim(win=win, name='instr2_4',
                           text='',
                           font='Arial',
                           pos=(0, -.3), height=0.05, wrapWidth=None, ori=0.0,
                           color='white', colorSpace='rgb', opacity=1.0,
                           languageStyle='LTR',
                           depth=-3.0);

# Initialize components for Routine "question_5"
question_5Clock = core.Clock()
question_text5 = visual.TextStim(win=win, name='question_text5',
                                 text='Вопрос 5. Уровень образования:\n\n1. Неполное среднее\n2. Среднее\n3. Среднее специальное\n4. Неполное/ незаконченное высшее\n5. Высшее\n6. Имеется ученая степень\n\nВыберите в соответствии с числом.',
                                 font='Arial',
                                 pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                 color='white', colorSpace='rgb', opacity=1.0,
                                 languageStyle='LTR',
                                 depth=0.0);
resp5 = keyboard.Keyboard()

# Initialize components for Routine "question_6"
question_6Clock = core.Clock()
answer_text6 = visual.TextBox2(
    win, text=' ', font='Arial',
    pos=(0, 0), letterHeight=0.05,
    size=None, borderWidth=1.0,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=False, italic=False,
    lineSpacing=0.5,
    padding=None,
    anchor='center',
    fillColor=None, borderColor=None,
    flipHoriz=False, flipVert=False,
    editable=True,
    name='answer_text6',
    autoLog=True,
)
question_text6 = visual.TextStim(win=win, name='question_text6',
                                 text='Вопрос 6. Ваша профессия:',
                                 font='Arial',
                                 pos=(0, .3), height=0.05, wrapWidth=None, ori=0.0,
                                 color='white', colorSpace='rgb', opacity=None,
                                 languageStyle='LTR',
                                 depth=-1.0);
resp6 = keyboard.Keyboard()
instr6 = visual.TextStim(win=win, name='instr6',
                         text='Нажмите на стрелку клавиатуры -> для продолжения',
                         font='Arial',
                         pos=(0, -.3), height=0.05, wrapWidth=None, ori=0.0,
                         color='white', colorSpace='rgb', opacity=1.0,
                         languageStyle='LTR',
                         depth=-3.0);

# Initialize components for Routine "question_7"
question_7Clock = core.Clock()
question_text7 = visual.TextStim(win=win, name='question_text7',
                                 text='Вопрос 7. Род Вашей деятельности:\n\n1. Связан с людьми\n2. Не связан с людьми\n3. Затрудняюсь ответить\n\nВыберите соответствие чтобы продолжить.\n',
                                 font='Arial',
                                 pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                 color='white', colorSpace='rgb', opacity=1.0,
                                 languageStyle='LTR',
                                 depth=0.0);
resp7 = keyboard.Keyboard()

# Initialize components for Routine "question8_10"
question8_10Clock = core.Clock()
question_text8_10 = visual.TextStim(win=win, name='question_text8_10',
                                    text='',
                                    font='Arial',
                                    pos=(0, .3), height=0.05, wrapWidth=None, ori=0.0,
                                    color='white', colorSpace='rgb', opacity=None,
                                    languageStyle='LTR',
                                    depth=0.0);
resp8_10 = keyboard.Keyboard()
choices_text = visual.TextStim(win=win, name='choices_text',
                               text='',
                               font='Arial',
                               pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                               color='white', colorSpace='rgb', opacity=1.0,
                               languageStyle='LTR',
                               depth=-2.0);
instr = visual.TextStim(win=win, name='instr',
                        text='Выберите в соответствии с числом.',
                        font='Arial',
                        pos=(0, -.3), height=0.05, wrapWidth=None, ori=0.0,
                        color='white', colorSpace='rgb', opacity=1.0,
                        languageStyle='LTR',
                        depth=-3.0);

# Initialize components for Routine "question11_16"
question11_16Clock = core.Clock()
question_text11_16 = visual.TextStim(win=win, name='question_text11_16',
                                     text='',
                                     font='Arial',
                                     pos=(0, .3), height=0.05, wrapWidth=None, ori=0.0,
                                     color='white', colorSpace='rgb', opacity=None,
                                     languageStyle='LTR',
                                     depth=0.0);
resp11_16 = keyboard.Keyboard()
choices_text11_16 = visual.TextStim(win=win, name='choices_text11_16',
                                    text='1. Правая рука\n2. Левая рука',
                                    font='Arial',
                                    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                    color='white', colorSpace='rgb', opacity=None,
                                    languageStyle='LTR',
                                    depth=-2.0);
instr11_16 = visual.TextStim(win=win, name='instr11_16',
                             text='Выберите в соответствии с числом',
                             font='Arial',
                             pos=(0, -.3), height=0.05, wrapWidth=None, ori=0.0,
                             color='white', colorSpace='rgb', opacity=1.0,
                             languageStyle='LTR',
                             depth=-3.0);

# Initialize components for Routine "instruction3"
instruction3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
                         text='Этап 3.\nСначало на короткое время вам будет предложено посмотреть лицо\nДалее вам надо будет выбрать однин из двух вариантов соответсвующий этому лицу его части.\nдля выбора используйте стрелочки влево и вправо\nДля продолжения нажмите пробел',
                         font='Open Sans',
                         pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                         color='white', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "X"
XClock = core.Clock()
imageX = visual.ImageStim(
    win=win,
    name='imageX',
    image='крест1.png', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 1.3),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "image_test"
image_testClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image',
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "routine_3x"
routine_3xClock = core.Clock()
image3x = visual.ImageStim(
    win=win,
    name='image3x',
    image='крест1.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 1.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "imagechoise"
imagechoiseClock = core.Clock()
image_left = visual.ImageStim(
    win=win,
    name='image_left',
    image='sin', mask=None,
    ori=0.0, pos=(-.5, 0), size=(1, 0.3),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_right = visual.ImageStim(
    win=win,
    name='image_right',
    image='sin', mask=None,
    ori=0.0, pos=(.5, 0), size=(1, 0.3),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "X"
XClock = core.Clock()
imageX = visual.ImageStim(
    win=win,
    name='imageX',
    image='крест1.png', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 1.3),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "imagetest2"
imagetest2Clock = core.Clock()
image_test2 = visual.ImageStim(
    win=win,
    name='image_test2',
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "routine_3x"
routine_3xClock = core.Clock()
image3x = visual.ImageStim(
    win=win,
    name='image3x',
    image='крест1.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 1.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "imagechoise2"
imagechoise2Clock = core.Clock()
image_left2 = visual.ImageStim(
    win=win,
    name='image_left2',
    image='sin', mask=None,
    ori=0.0, pos=(-0.4, 0), size=(0.5, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_right2 = visual.ImageStim(
    win=win,
    name='image_right2',
    image='sin', mask=None,
    ori=0.0, pos=(0.4, 0), size=(0.5, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "End_text"
EndClock = core.Clock()
End_text = visual.TextStim(win=win, name='End_text',
                           text='Спасибо за уделенное время!\nНажмите на пробел для завершения',
                           font='Arial',
                           pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                           color='white', colorSpace='rgb', opacity=None,
                           languageStyle='LTR',
                           depth=0.0);
End_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instruction1Components = [instructin_text, key_resp]
for thisComponent in instruction1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction1"-------
while continueRoutine:
    # get current time
    t = instruction1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instructin_text* updates
    if instructin_text.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        instructin_text.frameNStart = frameN  # exact frame index
        instructin_text.tStart = t  # local t and not account for scr refresh
        instructin_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructin_text, 'tStartRefresh')  # time at next scr refresh
        instructin_text.setAutoDraw(True)

    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space', 'Enter'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction1"-------
for thisComponent in instruction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructin_text.started', instructin_text.tStartRefresh)
thisExp.addData('instructin_text.stopped', instructin_text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys', key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential',
                           extraInfo=expInfo, originPath=-1,
                           trialList=data.importConditions('этап1.xlsx'),
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

    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    image1floor.setImage(imagefile)
    # keep track of which components have finished
    trialComponents = [image1floor]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draвw components on each frame

        # *image1floor* updates
        if image1floor.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            image1floor.frameNStart = frameN  # exact frame index
            image1floor.tStart = t  # local t and not account for scr refresh
            image1floor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1floor, 'tStartRefresh')  # time at next scr refresh
            image1floor.setAutoDraw(True)
        if image1floor.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image1floor.tStartRefresh + 5.0 - frameTolerance:
                # keep track of stop time/frame for later
                image1floor.tStop = t  # not accounting for scr refresh
                image1floor.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image1floor, 'tStopRefresh')  # time at next scr refresh
                image1floor.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image1floor.started', image1floor.tStartRefresh)
    trials.addData('image1floor.stopped', image1floor.tStopRefresh)

    # ------Prepare to start Routine "sleep"-------
    continueRoutine = True
    routineTimer.add(15.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    sleepComponents = [text]
    for thisComponent in sleepComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sleepClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "sleep"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = sleepClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sleepClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 15.0 - frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sleepComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "sleep"-------
    for thisComponent in sleepComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    thisExp.nextEntry()

# completed 1.0 repeats of 'trials'

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
instr_resp.keys = []
instr_resp.rt = []
_instr_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [instruction_text, instr_resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instruction_text* updates
    if instruction_text.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        instruction_text.frameNStart = frameN  # exact frame index
        instruction_text.tStart = t  # local t and not account for scr refresh
        instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text, 'tStartRefresh')  # time at next scr refresh
        instruction_text.setAutoDraw(True)

    # *instr_resp* updates
    waitOnFlip = False
    if instr_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        instr_resp.frameNStart = frameN  # exact frame index
        instr_resp.tStart = t  # local t and not account for scr refresh
        instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
        instr_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_resp.status == STARTED and not waitOnFlip:
        theseKeys = instr_resp.getKeys(keyList=['space', 'enter'], waitRelease=False)
        _instr_resp_allKeys.extend(theseKeys)
        if len(_instr_resp_allKeys):
            instr_resp.keys = _instr_resp_allKeys[-1].name  # just the last key pressed
            instr_resp.rt = _instr_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instr_resp.keys in ['', [], None]:  # No response was made
    instr_resp.keys = None
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "question1"-------
continueRoutine = True
# update component parameters for each repeat
resp1.keys = []
resp1.rt = []
_resp1_allKeys = []
# keep track of which components have finished
question1Components = [question_text1, resp1]
for thisComponent in question1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
question1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "question1"-------
while continueRoutine:
    # get current time
    t = question1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=question1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *question_text1* updates
    if question_text1.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        question_text1.frameNStart = frameN  # exact frame index
        question_text1.tStart = t  # local t and not account for scr refresh
        question_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(question_text1, 'tStartRefresh')  # time at next scr refresh
        question_text1.setAutoDraw(True)

    # *resp1* updates
    waitOnFlip = False
    if resp1.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        resp1.frameNStart = frameN  # exact frame index
        resp1.tStart = t  # local t and not account for scr refresh
        resp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp1, 'tStartRefresh')  # time at next scr refresh
        resp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp1.status == STARTED and not waitOnFlip:
        theseKeys = resp1.getKeys(keyList=['1', '2'], waitRelease=False)
        _resp1_allKeys.extend(theseKeys)
        if len(_resp1_allKeys):
            resp1.keys = _resp1_allKeys[-1].name  # just the last key pressed
            resp1.rt = _resp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in question1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "question1"-------
for thisComponent in question1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if resp1.keys in ['', [], None]:  # No response was made
    resp1.keys = None
thisExp.nextEntry()
answer = ''
if resp1.keys == '1':
    answer = ['Мужской']
elif resp1.keys == '2':
    answer = ['Женский']

outputDF['ПОЛ'] = answer
thisExp.addData('Пол', resp1.keys)
# the Routine "question1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
question2_4_loop = data.TrialHandler(nReps=1.0, method='sequential',
                                     extraInfo=expInfo, originPath=-1,
                                     trialList=data.importConditions('test_images.xlsx', selection='0:3'),
                                     seed=None, name='question2_4_loop')
thisExp.addLoop(question2_4_loop)  # add the loop to the experiment
thisQuestion2_4_loop = question2_4_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisQuestion2_4_loop.rgb)
if thisQuestion2_4_loop != None:
    for paramName in thisQuestion2_4_loop:
        exec('{} = thisQuestion2_4_loop[paramName]'.format(paramName))

for thisQuestion2_4_loop in question2_4_loop:
    currentLoop = question2_4_loop
    # abbreviate parameter names if possible (e.g. rgb = thisQuestion2_4_loop.rgb)
    if thisQuestion2_4_loop != None:
        for paramName in thisQuestion2_4_loop:
            exec('{} = thisQuestion2_4_loop[paramName]'.format(paramName))

    # ------Prepare to start Routine "question2_4"-------
    continueRoutine = True
    # update component parameters for each repeat
    answer_text2_4.setText(' ')
    question_text2_4.setText(question)
    resp2_4.keys = []
    resp2_4.rt = []
    _resp2_4_allKeys = []
    instr2_4.setText('Нажмите на стрелку клавиатуры -> для продолжения')
    # keep track of which components have finished
    question2_4Components = [answer_text2_4, question_text2_4, resp2_4, instr2_4]
    for thisComponent in question2_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    question2_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "question2_4"-------
    while continueRoutine:
        # get current time
        t = question2_4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=question2_4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *answer_text2_4* updates
        if answer_text2_4.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            answer_text2_4.frameNStart = frameN  # exact frame index
            answer_text2_4.tStart = t  # local t and not account for scr refresh
            answer_text2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer_text2_4, 'tStartRefresh')  # time at next scr refresh
            answer_text2_4.setAutoDraw(True)

        # *question_text2_4* updates
        if question_text2_4.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            question_text2_4.frameNStart = frameN  # exact frame index
            question_text2_4.tStart = t  # local t and not account for scr refresh
            question_text2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_text2_4, 'tStartRefresh')  # time at next scr refresh
            question_text2_4.setAutoDraw(True)

        # *resp2_4* updates
        waitOnFlip = False
        if resp2_4.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            resp2_4.frameNStart = frameN  # exact frame index
            resp2_4.tStart = t  # local t and not account for scr refresh
            resp2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp2_4, 'tStartRefresh')  # time at next scr refresh
            resp2_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp2_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp2_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp2_4.status == STARTED and not waitOnFlip:
            theseKeys = resp2_4.getKeys(keyList=['right'], waitRelease=False)
            _resp2_4_allKeys.extend(theseKeys)
            if len(_resp2_4_allKeys):
                resp2_4.keys = _resp2_4_allKeys[-1].name  # just the last key pressed
                resp2_4.rt = _resp2_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # *instr2_4* updates
        if instr2_4.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            instr2_4.frameNStart = frameN  # exact frame index
            instr2_4.tStart = t  # local t and not account for scr refresh
            instr2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr2_4, 'tStartRefresh')  # time at next scr refresh
            instr2_4.setAutoDraw(True)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question2_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "question2_4"-------
    for thisComponent in question2_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    outputDF['{}'.format(question_text2_4.text)] = answer_text2_4.text
    question2_4_loop.addData('{}'.format(question_text2_4.text), answer_text2_4.text)
    answer_text2_4.reset()
    # check responses
    if resp2_4.keys in ['', [], None]:  # No response was made
        resp2_4.keys = None
    # the Routine "question2_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 1.0 repeats of 'question2_4_loop'


# ------Prepare to start Routine "question_5"-------
continueRoutine = True
# update component parameters for each repeat
resp5.keys = []
resp5.rt = []
_resp5_allKeys = []
# keep track of which components have finished
question_5Components = [question_text5, resp5]
for thisComponent in question_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
question_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "question_5"-------
while continueRoutine:
    # get current time
    t = question_5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=question_5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *question_text5* updates
    if question_text5.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        question_text5.frameNStart = frameN  # exact frame index
        question_text5.tStart = t  # local t and not account for scr refresh
        question_text5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(question_text5, 'tStartRefresh')  # time at next scr refresh
        question_text5.setAutoDraw(True)

    # *resp5* updates
    waitOnFlip = False
    if resp5.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        resp5.frameNStart = frameN  # exact frame index
        resp5.tStart = t  # local t and not account for scr refresh
        resp5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp5, 'tStartRefresh')  # time at next scr refresh
        resp5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp5.status == STARTED and not waitOnFlip:
        theseKeys = resp5.getKeys(keyList=['1', '2', '3', '4', '5', '6'], waitRelease=False)
        _resp5_allKeys.extend(theseKeys)
        if len(_resp5_allKeys):
            resp5.keys = _resp5_allKeys[-1].name  # just the last key pressed
            resp5.rt = _resp5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in question_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "question_5"-------
for thisComponent in question_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if resp5.keys in ['', [], None]:  # No response was made
    resp5.keys = None
thisExp.nextEntry()
if resp5.keys == '1':
    resp5.keys = 'Неполное среднее'
elif resp5.keys == '2':
    resp5.keys = 'Среднее'
elif resp5.keys == '3':
    resp5.keys = 'Среднее специальное'
elif resp5.keys == '4':
    resp5.keys = 'Неполное / незаконченное высшее'
elif resp5.keys == '5':
    resp5.keys = 'Высшее'
else:
    resp5.keys = 'Имеется учёная степень'

thisExp.addData('Образование', resp5.keys)
outputDF['Образование'] = [resp5.keys]

# the Routine "question_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "question_6"-------
continueRoutine = True
# update component parameters for each repeat
resp6.keys = []
resp6.rt = []
_resp6_allKeys = []
# keep track of which components have finished
question_6Components = [answer_text6, question_text6, resp6, instr6]
for thisComponent in question_6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
question_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "question_6"-------
while continueRoutine:
    # get current time
    t = question_6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=question_6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *answer_text6* updates
    if answer_text6.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        answer_text6.frameNStart = frameN  # exact frame index
        answer_text6.tStart = t  # local t and not account for scr refresh
        answer_text6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(answer_text6, 'tStartRefresh')  # time at next scr refresh
        answer_text6.setAutoDraw(True)

    # *question_text6* updates
    if question_text6.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        question_text6.frameNStart = frameN  # exact frame index
        question_text6.tStart = t  # local t and not account for scr refresh
        question_text6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(question_text6, 'tStartRefresh')  # time at next scr refresh
        question_text6.setAutoDraw(True)

    # *resp6* updates
    waitOnFlip = False
    if resp6.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        resp6.frameNStart = frameN  # exact frame index
        resp6.tStart = t  # local t and not account for scr refresh
        resp6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp6, 'tStartRefresh')  # time at next scr refresh
        resp6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp6.status == STARTED and not waitOnFlip:
        theseKeys = resp6.getKeys(keyList=['right'], waitRelease=False)
        _resp6_allKeys.extend(theseKeys)
        if len(_resp6_allKeys):
            resp6.keys = _resp6_allKeys[-1].name  # just the last key pressed
            resp6.rt = _resp6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # *instr6* updates
    if instr6.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        instr6.frameNStart = frameN  # exact frame index
        instr6.tStart = t  # local t and not account for scr refresh
        instr6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr6, 'tStartRefresh')  # time at next scr refresh
        instr6.setAutoDraw(True)

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in question_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "question_6"-------
for thisComponent in question_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Ваша профессия', answer_text6.text)
outputDF['Профессия'] = [answer_text6.text]
answer_text6.reset()
# check responses
if resp6.keys in ['', [], None]:  # No response was made
    resp6.keys = None
thisExp.nextEntry()
# the Routine "question_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "question_7"-------
continueRoutine = True
# update component parameters for each repeat
resp7.keys = []
resp7.rt = []
_resp7_allKeys = []
# keep track of which components have finished
question_7Components = [question_text7, resp7]
for thisComponent in question_7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
question_7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "question_7"-------
while continueRoutine:
    # get current time
    t = question_7Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=question_7Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *question_text7* updates
    if question_text7.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        question_text7.frameNStart = frameN  # exact frame index
        question_text7.tStart = t  # local t and not account for scr refresh
        question_text7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(question_text7, 'tStartRefresh')  # time at next scr refresh
        question_text7.setAutoDraw(True)

    # *resp7* updates
    waitOnFlip = False
    if resp7.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        resp7.frameNStart = frameN  # exact frame index
        resp7.tStart = t  # local t and not account for scr refresh
        resp7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp7, 'tStartRefresh')  # time at next scr refresh
        resp7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp7.status == STARTED and not waitOnFlip:
        theseKeys = resp7.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        _resp7_allKeys.extend(theseKeys)
        if len(_resp7_allKeys):
            resp7.keys = _resp7_allKeys[-1].name  # just the last key pressed
            resp7.rt = _resp7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in question_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "question_7"-------
for thisComponent in question_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if resp7.keys in ['', [], None]:  # No response was made
    resp7.keys = None
thisExp.nextEntry()
if resp7.keys == '1':
    resp7.keys = 'Связан с людьми'
elif resp7.keys == '2':
    resp7.keys = 'Не связан с людьми'
else:
    resp7.keys = 'Затрудняюсь ответить'

thisExp.addData('Род деятельности', resp7.keys)
outputDF['Род деятельности'] = [resp7.keys]
# the Routine "question_7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
question8_10_loop = data.TrialHandler(nReps=1.0, method='sequential',
                                      extraInfo=expInfo, originPath=-1,
                                      trialList=data.importConditions('test_images.xlsx', selection='3:6'),
                                      seed=None, name='question8_10_loop')
thisExp.addLoop(question8_10_loop)  # add the loop to the experiment
thisQuestion8_10_loop = question8_10_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisQuestion8_10_loop.rgb)
if thisQuestion8_10_loop != None:
    for paramName in thisQuestion8_10_loop:
        exec('{} = thisQuestion8_10_loop[paramName]'.format(paramName))

for thisQuestion8_10_loop in question8_10_loop:
    currentLoop = question8_10_loop
    # abbreviate parameter names if possible (e.g. rgb = thisQuestion8_10_loop.rgb)
    if thisQuestion8_10_loop != None:
        for paramName in thisQuestion8_10_loop:
            exec('{} = thisQuestion8_10_loop[paramName]'.format(paramName))

    # ------Prepare to start Routine "question8_10"-------
    continueRoutine = True
    # update component parameters for each repeat
    question_text8_10.setText(question)
    resp8_10.keys = []
    resp8_10.rt = []
    _resp8_10_allKeys = []
    choices_text.setText(choices)
    # keep track of which components have finished
    question8_10Components = [question_text8_10, resp8_10, choices_text, instr]
    for thisComponent in question8_10Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    question8_10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "question8_10"-------
    while continueRoutine:
        # get current time
        t = question8_10Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=question8_10Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *question_text8_10* updates
        if question_text8_10.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            question_text8_10.frameNStart = frameN  # exact frame index
            question_text8_10.tStart = t  # local t and not account for scr refresh
            question_text8_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_text8_10, 'tStartRefresh')  # time at next scr refresh
            question_text8_10.setAutoDraw(True)

        # *resp8_10* updates
        waitOnFlip = False
        if resp8_10.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            resp8_10.frameNStart = frameN  # exact frame index
            resp8_10.tStart = t  # local t and not account for scr refresh
            resp8_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp8_10, 'tStartRefresh')  # time at next scr refresh
            resp8_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp8_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp8_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp8_10.status == STARTED and not waitOnFlip:
            theseKeys = resp8_10.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _resp8_10_allKeys.extend(theseKeys)
            if len(_resp8_10_allKeys):
                resp8_10.keys = _resp8_10_allKeys[-1].name  # just the last key pressed
                resp8_10.rt = _resp8_10_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # *choices_text* updates
        if choices_text.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            choices_text.frameNStart = frameN  # exact frame index
            choices_text.tStart = t  # local t and not account for scr refresh
            choices_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choices_text, 'tStartRefresh')  # time at next scr refresh
            choices_text.setAutoDraw(True)

        # *instr* updates
        if instr.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            instr.frameNStart = frameN  # exact frame index
            instr.tStart = t  # local t and not account for scr refresh
            instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr, 'tStartRefresh')  # time at next scr refresh
            instr.setAutoDraw(True)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question8_10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "question8_10"-------
    for thisComponent in question8_10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp8_10.keys in ['', [], None]:  # No response was made
        resp8_10.keys = None
    if resp8_10.keys == '1':
        if question_text8_10.text == 'Вопрос 8. Какая память, на Ваш взгляд, развита у Вас лучше?':
            resp8_10.keys = 'Зрительная'
        if question_text8_10.text == 'Вопрос 9. Как Вы оцениваете свою способность запоминать лица?':
            resp8_10.keys = 'Запоминание лиц дается быстро и легко'
        if question_text8_10.text == 'Вопрос 10. Если бы Вы встретили знакомого человека спустя несколько лет после последней встречи, узнали бы Вы его?':
            resp8_10.keys = 'Да'
    elif resp8_10.keys == '2':
        if question_text8_10.text == 'Вопрос 8. Какая память, на Ваш взгляд, развита у Вас лучше?':
            resp8_10.keys = 'Слуховая'
        if question_text8_10.text == 'Вопрос 9. Как Вы оцениваете свою способность запоминать лица?':
            resp8_10.keys = 'Запоминание лиц не вызывает явных затруднений'
        if question_text8_10.text == 'Вопрос 10. Если бы Вы встретили знакомого человека спустя несколько лет после последней встречи, узнали бы Вы его?':
            resp8_10.keys = 'Скорее да, чем нет'
    elif resp8_10.keys == '3':
        if question_text8_10.text == 'Вопрос 8. Какая память, на Ваш взгляд, развита у Вас лучше?':
            resp8_10.keys = 'Моторная'
        if question_text8_10.text == 'Вопрос 9. Как Вы оцениваете свою способность запоминать лица?':
            resp8_10.keys = 'Запоминание лиц дается с трудом'
        if question_text8_10.text == 'Вопрос 10. Если бы Вы встретили знакомого человека спустя несколько лет после последней встречи, узнали бы Вы его?':
            resp8_10.keys = 'Скорее нет, чем да'
    elif resp8_10.keys == '4':
        if question_text8_10.text == 'Вопрос 8. Какая память, на Ваш взгляд, развита у Вас лучше?':
            resp8_10.keys = 'Вкусовая'
        if question_text8_10.text == 'Вопрос 9. Как Вы оцениваете свою способность запоминать лица?':
            resp8_10.keys = 'Запоминание лиц практически невозможно'
        if question_text8_10.text == 'Вопрос 10. Если бы Вы встретили знакомого человека спустя несколько лет после последней встречи, узнали бы Вы его?':
            resp8_10.keys = 'Нет'
    question8_10_loop.addData('{}'.format(question_text8_10.text), resp8_10.keys)
    outputDF['{}'.format(question_text8_10.text)] = [resp8_10.keys]
    # the Routine "question8_10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 1.0 repeats of 'question8_10_loop'


# set up handler to look after randomisation of conditions etc
question11_16_loop = data.TrialHandler(nReps=1.0, method='sequential',
                                       extraInfo=expInfo, originPath=-1,
                                       trialList=data.importConditions('test_images.xlsx', selection='6:12'),
                                       seed=None, name='question11_16_loop')
thisExp.addLoop(question11_16_loop)  # add the loop to the experiment
thisQuestion11_16_loop = question11_16_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisQuestion11_16_loop.rgb)
if thisQuestion11_16_loop != None:
    for paramName in thisQuestion11_16_loop:
        exec('{} = thisQuestion11_16_loop[paramName]'.format(paramName))

for thisQuestion11_16_loop in question11_16_loop:
    currentLoop = question11_16_loop
    # abbreviate parameter names if possible (e.g. rgb = thisQuestion11_16_loop.rgb)
    if thisQuestion11_16_loop != None:
        for paramName in thisQuestion11_16_loop:
            exec('{} = thisQuestion11_16_loop[paramName]'.format(paramName))

    # ------Prepare to start Routine "question11_16"-------
    continueRoutine = True
    # update component parameters for each repeat
    question_text11_16.setText(question)
    resp11_16.keys = []
    resp11_16.rt = []
    _resp11_16_allKeys = []
    # keep track of which components have finished
    question11_16Components = [question_text11_16, resp11_16, choices_text11_16, instr11_16]
    for thisComponent in question11_16Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    question11_16Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "question11_16"-------
    while continueRoutine:
        # get current time
        t = question11_16Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=question11_16Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *question_text11_16* updates
        if question_text11_16.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            question_text11_16.frameNStart = frameN  # exact frame index
            question_text11_16.tStart = t  # local t and not account for scr refresh
            question_text11_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_text11_16, 'tStartRefresh')  # time at next scr refresh
            question_text11_16.setAutoDraw(True)

        # *resp11_16* updates
        waitOnFlip = False
        if resp11_16.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            resp11_16.frameNStart = frameN  # exact frame index
            resp11_16.tStart = t  # local t and not account for scr refresh
            resp11_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp11_16, 'tStartRefresh')  # time at next scr refresh
            resp11_16.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp11_16.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp11_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp11_16.status == STARTED and not waitOnFlip:
            theseKeys = resp11_16.getKeys(keyList=['1', '2'], waitRelease=False)
            _resp11_16_allKeys.extend(theseKeys)
            if len(_resp11_16_allKeys):
                resp11_16.keys = _resp11_16_allKeys[-1].name  # just the last key pressed
                resp11_16.rt = _resp11_16_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # *choices_text11_16* updates
        if choices_text11_16.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            choices_text11_16.frameNStart = frameN  # exact frame index
            choices_text11_16.tStart = t  # local t and not account for scr refresh
            choices_text11_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choices_text11_16, 'tStartRefresh')  # time at next scr refresh
            choices_text11_16.setAutoDraw(True)

        # *instr11_16* updates
        if instr11_16.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            instr11_16.frameNStart = frameN  # exact frame index
            instr11_16.tStart = t  # local t and not account for scr refresh
            instr11_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr11_16, 'tStartRefresh')  # time at next scr refresh
            instr11_16.setAutoDraw(True)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question11_16Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "question11_16"-------
    for thisComponent in question11_16Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp11_16.keys in ['', [], None]:  # No response was made
        resp11_16.keys = None
    if resp11_16.keys == '1':
        resp11_16.keys = 'Правая рука'
    else:
        resp11_16.keys = 'Левая рука'

    question11_16_loop.addData('{}'.format(question_text11_16.text), resp11_16.keys)
    outputDF['{}'.format(question_text11_16.text)] = [resp11_16.keys]
    # the Routine "question11_16" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 1.0 repeats of 'question11_16_loop'


# ------Prepare to start Routine "instruction3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instruction3Components = [text_3, key_resp_3]
for thisComponent in instruction3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction3"-------
while continueRoutine:
    # get current time
    t = instruction3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)

    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction3"-------
for thisComponent in instruction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys', key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random',
                             extraInfo=expInfo, originPath=-1,
                             trialList=data.importConditions('этап3.xlsx', selection='0:36'),
                             seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

left_stimuls = []
right_stimuls = []
stimuls = []
user_answers = []
correct_answers = []
time_answers = []
for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))

    # ------Prepare to start Routine "X"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    XComponents = [imageX]
    for thisComponent in XComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    XClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "X"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = XClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=XClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *imageX* updates
        if imageX.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            imageX.frameNStart = frameN  # exact frame index
            imageX.tStart = t  # local t and not account for scr refresh
            imageX.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageX, 'tStartRefresh')  # time at next scr refresh
            imageX.setAutoDraw(True)
        if imageX.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageX.tStartRefresh + 1.0 - frameTolerance:
                # keep track of stop time/frame for later
                imageX.tStop = t  # not accounting for scr refresh
                imageX.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageX, 'tStopRefresh')  # time at next scr refresh
                imageX.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in XComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "X"-------
    for thisComponent in XComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('imageX.started', imageX.tStartRefresh)
    trials_2.addData('imageX.stopped', imageX.tStopRefresh)

    # ------Prepare to start Routine "image_test"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    image.setImage(imagetest)
    # keep track of which components have finished
    image_testComponents = [image]
    for thisComponent in image_testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    image_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "image_test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = image_testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=image_testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 1.0 - frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in image_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "image_test"-------
    for thisComponent in image_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('image.started', image.tStartRefresh)
    trials_2.addData('image.stopped', image.tStopRefresh)
    stimuls.append(image.image)

    # ------Prepare to start Routine "routine_3x"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    routine_3xComponents = [image3x]
    for thisComponent in routine_3xComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_3xClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "routine_3x"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = routine_3xClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_3xClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *image3x* updates
        if image3x.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            image3x.frameNStart = frameN  # exact frame index
            image3x.tStart = t  # local t and not account for scr refresh
            image3x.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image3x, 'tStartRefresh')  # time at next scr refresh
            image3x.setAutoDraw(True)
        if image3x.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image3x.tStartRefresh + 0.2 - frameTolerance:
                # keep track of stop time/frame for later
                image3x.tStop = t  # not accounting for scr refresh
                image3x.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image3x, 'tStopRefresh')  # time at next scr refresh
                image3x.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_3xComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "routine_3x"-------
    for thisComponent in routine_3xComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('image3x.started', image3x.tStartRefresh)
    trials_2.addData('image3x.stopped', image3x.tStopRefresh)

    # ------Prepare to start Routine "imagechoise"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_left.setImage(imageleft)
    image_right.setImage(imageright)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    imagechoiseComponents = [image_left, image_right, key_resp_6]
    for thisComponent in imagechoiseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    imagechoiseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "imagechoise"-------
    while continueRoutine:
        # get current time
        t = imagechoiseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=imagechoiseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *image_left* updates
        if image_left.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            image_left.frameNStart = frameN  # exact frame index
            image_left.tStart = t  # local t and not account for scr refresh
            image_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_left, 'tStartRefresh')  # time at next scr refresh
            image_left.setAutoDraw(True)

        # *image_right* updates
        if image_right.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            image_right.frameNStart = frameN  # exact frame index
            image_right.tStart = t  # local t and not account for scr refresh
            image_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_right, 'tStartRefresh')  # time at next scr refresh
            image_right.setAutoDraw(True)

        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # was this correct?
                if (key_resp_6.keys == str(corans)) or (key_resp_6.keys == corans):
                    key_resp_6.corr = 1
                else:
                    key_resp_6.corr = 0
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in imagechoiseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "imagechoise"-------
    for thisComponent in imagechoiseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('image_left.started', image_left.tStartRefresh)
    trials_2.addData('image_left.stopped', image_left.tStopRefresh)
    trials_2.addData('image_right.started', image_right.tStartRefresh)
    trials_2.addData('image_right.stopped', image_right.tStopRefresh)
    left_stimuls.append(image_left.image)
    right_stimuls.append(image_right.image)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
        # was no response the correct answer?!
        if str(corans).lower() == 'none':
            key_resp_6.corr = 1;  # correct non-response
        else:
            key_resp_6.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_6.keys', key_resp_6.keys)
    user_answers.append(key_resp_6.keys)
    trials_2.addData('key_resp_6.corr', key_resp_6.corr)
    if key_resp_6.corr == 1:
        correct_answers.append('Правильно')
    else:
        correct_answers.append('Неправильно')
    if key_resp_6.keys != None:  # we had a response
        time_answers.append('{:.4} секунд'.format(key_resp_6.rt))
        trials_2.addData('key_resp_6.rt', key_resp_6.rt)
    trials_2.addData('key_resp_6.started', key_resp_6.tStartRefresh)
    trials_2.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
    # the Routine "imagechoise" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
# completed 1.0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='random',
                             extraInfo=expInfo, originPath=-1,
                             trialList=data.importConditions('этап3.xlsx', selection='37:72'),
                             seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))

    # ------Prepare to start Routine "X"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    XComponents = [imageX]
    for thisComponent in XComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    XClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "X"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = XClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=XClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *imageX* updates
        if imageX.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            imageX.frameNStart = frameN  # exact frame index
            imageX.tStart = t  # local t and not account for scr refresh
            imageX.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageX, 'tStartRefresh')  # time at next scr refresh
            imageX.setAutoDraw(True)
        if imageX.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageX.tStartRefresh + 1.0 - frameTolerance:
                # keep track of stop time/frame for later
                imageX.tStop = t  # not accounting for scr refresh
                imageX.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageX, 'tStopRefresh')  # time at next scr refresh
                imageX.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in XComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "X"-------
    for thisComponent in XComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('imageX.started', imageX.tStartRefresh)
    trials_3.addData('imageX.stopped', imageX.tStopRefresh)

    # ------Prepare to start Routine "imagetest2"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    image_test2.setImage(imagetest)
    # keep track of which components have finished
    imagetest2Components = [image_test2]
    for thisComponent in imagetest2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    imagetest2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "imagetest2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = imagetest2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=imagetest2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *image_test2* updates
        if image_test2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            image_test2.frameNStart = frameN  # exact frame index
            image_test2.tStart = t  # local t and not account for scr refresh
            image_test2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_test2, 'tStartRefresh')  # time at next scr refresh
            image_test2.setAutoDraw(True)
        if image_test2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_test2.tStartRefresh + 1.0 - frameTolerance:
                # keep track of stop time/frame for later
                image_test2.tStop = t  # not accounting for scr refresh
                image_test2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_test2, 'tStopRefresh')  # time at next scr refresh
                image_test2.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in imagetest2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "imagetest2"-------
    for thisComponent in imagetest2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stimuls.append(image_test2.image)
    trials_3.addData('image_test2.started', image_test2.tStartRefresh)
    trials_3.addData('image_test2.stopped', image_test2.tStopRefresh)

    # ------Prepare to start Routine "routine_3x"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    routine_3xComponents = [image3x]
    for thisComponent in routine_3xComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_3xClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "routine_3x"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = routine_3xClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_3xClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *image3x* updates
        if image3x.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            image3x.frameNStart = frameN  # exact frame index
            image3x.tStart = t  # local t and not account for scr refresh
            image3x.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image3x, 'tStartRefresh')  # time at next scr refresh
            image3x.setAutoDraw(True)
        if image3x.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image3x.tStartRefresh + 0.2 - frameTolerance:
                # keep track of stop time/frame for later
                image3x.tStop = t  # not accounting for scr refresh
                image3x.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image3x, 'tStopRefresh')  # time at next scr refresh
                image3x.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_3xComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "routine_3x"-------
    for thisComponent in routine_3xComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('image3x.started', image3x.tStartRefresh)
    trials_3.addData('image3x.stopped', image3x.tStopRefresh)

    # ------Prepare to start Routine "imagechoise2"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_left2.setImage(imageleft)
    image_right2.setImage(imageright)
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    imagechoise2Components = [image_left2, image_right2, key_resp_7]
    for thisComponent in imagechoise2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    imagechoise2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "imagechoise2"-------
    while continueRoutine:
        # get current time
        t = imagechoise2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=imagechoise2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *image_left2* updates
        if image_left2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            image_left2.frameNStart = frameN  # exact frame index
            image_left2.tStart = t  # local t and not account for scr refresh
            image_left2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_left2, 'tStartRefresh')  # time at next scr refresh
            image_left2.setAutoDraw(True)

        # *image_right2* updates
        if image_right2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            image_right2.frameNStart = frameN  # exact frame index
            image_right2.tStart = t  # local t and not account for scr refresh
            image_right2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_right2, 'tStartRefresh')  # time at next scr refresh
            image_right2.setAutoDraw(True)

        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # was this correct?
                if (key_resp_7.keys == str(corans)) or (key_resp_7.keys == corans):
                    key_resp_7.corr = 1
                else:
                    key_resp_7.corr = 0
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in imagechoise2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "imagechoise2"-------
    for thisComponent in imagechoise2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    left_stimuls.append(image_left2.image)
    right_stimuls.append(image_right2.image)
    trials_3.addData('image_left2.started', image_left2.tStartRefresh)
    trials_3.addData('image_left2.stopped', image_left2.tStopRefresh)
    trials_3.addData('image_right2.started', image_right2.tStartRefresh)
    trials_3.addData('image_right2.stopped', image_right2.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
        # was no response the correct answer?!
        if str(corans).lower() == 'none':
            key_resp_7.corr = 1;  # correct non-response
        else:
            key_resp_7.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    user_answers.append(key_resp_7.keys)
    trials_3.addData('key_resp_7.keys', key_resp_7.keys)
    if key_resp_7.corr == 1:
        correct_answers.append('Правильно')
    else:
        correct_answers.append('Неправильно')
    trials_3.addData('key_resp_7.corr', key_resp_7.corr)
    if key_resp_7.keys != None:  # we had a response
        time_answers.append('{:.4} секунд'.format(key_resp_7.rt))
        trials_3.addData('key_resp_7.rt', key_resp_7.rt)
    trials_3.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    trials_3.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    # the Routine "imagechoise2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 1.0 repeats of 'trials_3'


# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
End_resp.keys = []
End_resp.rt = []
_End_resp_allKeys = []
# keep track of which components have finished
EndComponents = [End_text, End_resp]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instruction_text* updates
    if End_text.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        End_text.frameNStart = frameN  # exact frame index
        End_text.tStart = t  # local t and not account for scr refresh
        End_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End_text, 'tStartRefresh')  # time at next scr refresh
        End_text.setAutoDraw(True)

    # *instr_resp* updates
    waitOnFlip = False
    if End_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        End_resp.frameNStart = frameN  # exact frame index
        End_resp.tStart = t  # local t and not account for scr refresh
        End_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End_resp, 'tStartRefresh')  # time at next scr refresh
        End_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(End_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(End_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if End_resp.status == STARTED and not waitOnFlip:
        theseKeys = End_resp.getKeys(keyList=['space'], waitRelease=False)
        _End_resp_allKeys.extend(theseKeys)
        if len(_End_resp_allKeys):
            End_resp.keys = _End_resp_allKeys[-1].name  # just the last key pressed
            End_resp.rt = _End_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if End_resp.keys in ['', [], None]:  # No response was made
    End_resp.keys = None
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

testDF = pd.DataFrame()
testDF['Целевые стимулы'] = stimuls
testDF['Левые стимулы'] = left_stimuls
testDF['Правые стимулы'] = right_stimuls
testDF['Ответ участника'] = user_answers
testDF['Правильный ответ'] = correct_answers
testDF['Время ответа'] = time_answers

import datetime

today = datetime.datetime.today()

with pd.ExcelWriter('outputData/{}output.xlsx'.format(today.strftime("%Y-%m-%d-%H.%M.%S")),
                    options={'mode': 'a'}) as writer:
    outputDF.to_excel(writer)
    testDF.to_excel(writer)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename + '.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
