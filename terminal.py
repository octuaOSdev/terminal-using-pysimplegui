import sys
import PySimpleGUI as sg
import logging
import os # import the os module

def custom_command():
    
    pass

def custom_command_2():
    
    pass

def custom_command_3():
    print("commands:help,retry,pause")
    pass

def main():
    logging.basicConfig(filename='terminal.log', level=logging.DEBUG)
    commands = {
        "exit": custom_command,
        "retry": custom_command_2,
        "help": custom_command_3
    }

    layout = [[sg.Multiline(size=(80, 20), key='-OUTPUT-', disabled=True, autoscroll=True)],
              [sg.Input(key='-IN-'), sg.Button('Enter'), sg.Exit]]

    window = sg.Window('Terminal', layout)

    while True:
        event, values = window.read()
        
            

        user_input = values['-IN-']
        window['-IN-'].update('')
        window['-OUTPUT-'].print(user_input)

        if user_input == "":
            logging.warning(f"field cannot be empty!")
            user_input = "none"

        

        command_parts = user_input.split()
        command = command_parts[0]
        params = command_parts[1:]

        if command in commands:
            
            logging.info(f"Command '{command}' executed successfully with parameters {params}")
        else:
            window['-OUTPUT-'].print(f"Command '{command}' not found.")
            logging.warning(f"Command '{command}' not found.")

    window.close()

if __name__ == "__main__":
    main()

