## Program Overview

This program automates interactions with specific windows of a graphical user interface (GUI) using the `pywinauto` library. It focuses on searching for windows, sending key commands, and copying data between fields. Below is a detailed explanation of the program.

### Dependencies

The program relies on the following Python libraries:
- `pywinauto`: Used for GUI automation.
- `time`: Used to introduce delays between actions.

### Functions

#### `GetWindow(name)`

This function iterates through all open windows on the desktop and returns the first window whose title contains the specified `name`.

- **Parameters**:
  - `name`: A string representing part of the window's title.
- **Returns**:
  - The window object if found; otherwise, `None`.

#### `SendCmd(n, cmd, delay=0.2)`

This function sends a specific keyboard command multiple times with a delay between each command.

- **Parameters**:
  - `n`: The number of times to send the command.
  - `cmd`: The keyboard command to send.
  - `delay`: The delay between each command (default is 0.2 seconds).

### Main Function

#### `Run(ertek)`

This function performs a series of actions to interact with specific windows and copy data between fields. The steps are as follows:

1. **Focus on the initial window**:
   - Searches for the window with the title "EMP(1)/102 Bekötés megjelenítése: kezdő kép".
   - Sets focus on the window and sends `Ctrl+F` to open the search functionality.

2. **Navigate and input data**:
   - Searches for the window titled "EMP(1)/102 Data Finder(adatkereső): Közműbekötés keresése".
   - Sets focus on this window, navigates through fields using `Tab` and `Right` keys, and inputs the `ertek` (parameter value).
   - Sends `Enter` to confirm the input.

3. **Copy data**:
   - Focuses on the window titled "EMP(1)/102 Bekötés megjelenítése:".
   - Selects all text (`Ctrl+A`) and copies it (`Ctrl+C`).
   - Navigates through tabs and copies specific data fields using `Ctrl+Y` and `Ctrl+C`.

4. **Handle alternative windows**:
   - If the expected window is not found, it looks for a window titled "EMP(1)/102 Információ" and sets focus on it.
   - Closes the window and performs final actions.

### Execution Flow

The program reads lines from a file located at `"C:\\Users\\G3909\\Desktop\\forras.txt"`, which contains values to be input into the application. For each line, it calls the `Run` function with the line's value.

- **File Handling**:
  - Opens the file in read mode.
  - Reads each line and calls `Run` with the cleaned line value.
  - Introduces a delay of 200 seconds between each execution to ensure proper processing time.

### Usage

To use this program:
1. Ensure that the `pywinauto` library is installed.
2. Create a text file (`forras.txt`) with the input values.
3. Run the script.

This automation can be useful for repetitive tasks in GUI applications, especially when dealing with data entry and extraction.

### Important Notes

- The window titles must match exactly for the program to work correctly.
- Ensure that the target application is running and the windows are available.
- Adjust delays (`time.sleep`) as necessary based on system performance.