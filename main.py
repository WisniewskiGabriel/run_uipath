import subprocess
import logging
import os

logging.warning('STARTANDO')

command = r'C:\\Users\\User\\AppData\\Local\\Programs\\UiPath\\Studio\\UiRobot.exe execute --process teste_run_with_message_box'
subprocess.run(command, shell=True)