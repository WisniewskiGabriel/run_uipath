import subprocess
import logging
import os

username = os.environ.get('USERNAME')

logging.warning('User: '+username)

command = r'C:\\Users\\'+username+'\\AppData\\Local\\Programs\\UiPath\\Studio\\UiRobot.exe execute --process teste_run_with_message_box'
subprocess.run(command, shell=True)