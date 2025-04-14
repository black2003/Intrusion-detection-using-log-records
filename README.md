# Sql-Injection-Detection

## This project presents a machine learning-based web application designed to detect IoT Intrusion **attacks** by analyzing **log records**.

- **Objective**: To enhance cybersecurity by automatically identifying potential attack patterns in system logs using a trained ML model.
- **Core Functionality**:
    - Accepts user-provided log data through a web interface.
    - Utilizes a pre-trained model (`model.h5`) to classify inputs as either benign or indicative of Intrustion/ cyberattack.
    - Provides real-time feedback on potential threats.

### Steps to execute:
- git clone the repo into the desired location
- install python on your system
- - if you are on linux, execute `sudo apt install python3`
  - if on windows, download python form "https://www.python.org/downloads/"

- there are two ways to install dependencies:
#### For manual installation 
- execute `pip install -r requirements.txt`
#### For auto installation (if only you are on linux)
- execute `chmod +x auto_setup.sh`
- then execute `./auto_setup.sh`
- it will automatically install all the necessary requirements and then even launch the program
