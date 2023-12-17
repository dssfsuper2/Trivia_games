import console_version
import ctk_trivia

version = int(input('Choose a game : 0-simple trivia 1-custom tkinter trivia:\n'))

if version == 0:
    console_version.play()
if version == 1:
    ctk_trivia.main()
else:
    print('This version does not exist.')
