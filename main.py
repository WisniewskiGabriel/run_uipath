import subprocess
import logging
import os

logging.warning('STARTANDO')

command1 = r'cd C:\tools\jenkins\workspace\teste_python'
command2 = r'C:\Users\User\AppData\Local\Programs\UiPath\Studio\UiRobot.exe execute -p teste_run_with_message_box'
subprocess.run(command1, shell=True)
subprocess.run(command2, shell=True)
