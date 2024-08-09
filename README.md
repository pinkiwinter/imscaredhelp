# Overview

This repository contains a Python script that demonstrates various system manipulation and file encryption techniques. The script is designed for educational purposes only to showcase different functionalities that can be achieved with Python libraries and modules. It includes features such as file encryption, mouse movement simulation, window jittering, and interaction with system processes.

**Note:** This script is potentially harmful if used inappropriately. Use responsibly and only for educational purposes in a controlled environment.

## Features

1. **File Encryption**:
   - Encrypts files in common user directories (Documents, Desktop, Downloads, AppData) using AES encryption.
   - Files are encrypted with a randomly generated key and appended with an `.enc` extension.

2. **Mouse Shaking**:
   - Simulates random mouse movements to potentially disrupt user interactions.

3. **Application Launching**:
   - Periodically opens random applications (Notepad, Command Prompt, Calculator) and performs Google searches with pre-defined queries.

4. **Window Jittering**:
   - Moves all currently open windows randomly on the screen.

5. **System Messages**:
   - Displays random message boxes at regular intervals with random text.

6. **Taskbar Hiding**:
   - Hides the Windows taskbar to obscure the user's interface.

7. **Task Manager Termination**:
   - Continuously attempts to terminate the Task Manager process to prevent users from stopping the script.

8. **Startup Persistence**:
   - Copies the script to the Windows Startup folder to ensure it runs on system boot.

## Requirements

- `pyautogui`
- `random`
- `time`
- `subprocess`
- `webbrowser`
- `pygetwindow`
- `ctypes`
- `Crypto` (from `pycryptodome`)
- `psutil`
- `shutil`

## Usage

1. **Setup**:
   - Ensure you have the required libraries installed using `pip install pyautogui pygetwindow pycryptodome psutil`.

2. **Execution**:
   - Run the script as a standalone Python file. It will execute various functions concurrently in separate threads.

3. **Responsibility**:
   - **Important:** This script should not be used to cause harm or disrupt normal system operations. It is provided solely for learning and understanding the potential impacts of system manipulation techniques.

## Disclaimer

The use of this script for malicious purposes is illegal and unethical. Always ensure you have proper authorization before executing such scripts on any system. The authors of this script are not responsible for any misuse or damage caused by it.

---

Feel free to fork this repository and experiment with the code for educational purposes. Contributions and improvements are welcome, but please ensure that any modifications align with ethical guidelines and legal standards.
