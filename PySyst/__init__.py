# PySyst - Init

''' This is the __init__.py file. '''

'''
Copyright 2023 Aniketh Chavare

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

# Imports
import sys
import wmi
import requests
import platform
import webbrowser
import importlib_metadata
from bs4 import BeautifulSoup
from colorama import Fore, Style

# Variables - Package Information
__name__ = "PySyst"
__version__ = "1.1.2"
__description__ = "This Python package alters your computer's settings and files and includes various system-related functions."
__license__ = "Apache License 2.0"
__author__ = "Aniketh Chavare"
__author_email__ = "anikethchavare@outlook.com"
__github_url__ = "https://github.com/anikethchavare/PySyst"
__pypi_url__ = "https://pypi.org/project/PySyst"
__docs_url__ = "https://anikethchavare.gitbook.io/pysyst"

# Variables
os = platform.system()
os_release = platform.release()
os_version = platform.version()
pc_name = platform.node()
machine = platform.machine()
processor = platform.processor()

manufacturer = wmi.WMI().Win32_ComputerSystem()[0].Manufacturer
model = wmi.WMI().Win32_ComputerSystem()[0].Model

# Function 1 - Version Check
def version_check():
    # Variables
    system_version = importlib_metadata.version("PySyst")

    # Try/Except - Package Version
    try:
        package_version = BeautifulSoup(requests.get(__pypi_url__).text, "html.parser").body.main.find_all("div")[1].h1.text.strip().split()[1]
    except:
        package_version = system_version

    # Checking the Version
    if (system_version < package_version):
        # Checking the Environment
        if ("idlelib.run" in sys.modules):
            print("You are using PySyst version " + system_version + ", however version " + package_version + " is available.")
            print("Upgrade to the latest version for new features and improvements using this command: pip install --upgrade PySyst" + "\n")
        else:
            print(Fore.YELLOW + "You are using PySyst version " + system_version + ", however version " + package_version + " is available.")
            print(Fore.YELLOW + "Upgrade to the latest version for new features and improvements using this command: " + Fore.CYAN + "pip install --upgrade PySyst" + Style.RESET_ALL + "\n")

# Function 2 - GitHub
def github():
    # Opening PySyst's GitHub Repository
    try:
        webbrowser.open(__github_url__)
    except:
        raise Exception("An error occurred while opening the GitHub repository. Please try again.")

# Function 3 - PyPI
def pypi():
    # Opening PySyst's PyPI Page
    try:
        webbrowser.open(__pypi_url__)
    except:
        raise Exception("An error occurred while opening the PyPI page. Please try again.")

# Function 4 - Docs
def docs():
    # Opening PySyst's Docs
    try:
        webbrowser.open(__docs_url__)
    except:
        raise Exception("An error occurred while opening the docs. Please try again.")

# Running the "version_check()" Function
version_check()