#!/usr/bin/env python
# https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Script_Launcher.py
import PySimpleGUI as sg
import glob
import ntpath
import subprocess

LOCATION_OF_YOUR_SCRIPTS = ''
TRANSPARENCY = .6       # how transparent the window looks. 0 = invisible, 1 = normal window

# Execute the command.  Will not see the output from the command until it completes.

def open_file_vscode(command, *args):
    expanded_args = []
    for a in args:
        expanded_args.append(a)
        # expanded_args += a
    try:
        sp = subprocess.Popen(['code', command, expanded_args], shell=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except:
        out = ''
    return out

def execute_command_blocking(command, *args):
    expanded_args = []
    for a in args:
        expanded_args.append(a)
        # expanded_args += a
    try:
        sp = subprocess.Popen(['python', command, expanded_args], shell=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except:
        out = ''
    return out

# Executes command and immediately returns.  Will not see anything the script outputs


def execute_command_nonblocking(command, *args):
    expanded_args = []
    for a in args:
        expanded_args += a
    try:
        sp = subprocess.Popen(["python",command, expanded_args], shell=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        pass


def Launcher2():
    sg.theme('GreenTan')

    filelist = glob.glob(LOCATION_OF_YOUR_SCRIPTS+'*.py')
    namesonly = []
    for file in filelist:
        namesonly.append(ntpath.basename(file))

    layout = [
        [sg.Listbox(values=namesonly, size=(30, 19),
                    select_mode=sg.SELECT_MODE_EXTENDED, key='demolist'),
         sg.Output(size=(88, 20), font='Courier 10')],
        [sg.Button('Run'), sg.Button('Open code'), sg.Button('EXIT')],
    ]

    window = sg.Window('Python Script launcher', layout, alpha_channel=TRANSPARENCY,)

    # ---===--- Loop taking in user input  --- #
    while True:
        event, values = window.read()
        if event in ('EXIT', None):
            break           # exit button clicked
        if event == 'Open code':
            for index, file in enumerate(values['demolist']):
                print('Open  %s by VS Code' % file)
                window.refresh()          # make the print appear immediately
                
                open_file_vscode(LOCATION_OF_YOUR_SCRIPTS + file)
        elif event == 'Run':
            for index, file in enumerate(values['demolist']):
                print('Launching %s' % file)
                window.refresh()          # make the print appear immediately
                execute_command_blocking(LOCATION_OF_YOUR_SCRIPTS + file)

    window.close()


if __name__ == '__main__':
    Launcher2()
