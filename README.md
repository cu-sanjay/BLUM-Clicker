<p align="center">
  <img src="https://github.com/user-attachments/assets/fab94859-c95e-41ae-862d-d4189dcbc190" alt="Logo" width="100" height="100">
</p>

<h1 align="center">Auto Clicker for $BLUM Mining Game</h1>

<h1 align="center">
  
  ![Auto Clicker](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
  ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-green.svg)
  ![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)
  
</h1>

A Python-based **Auto Clicker (ANTI-BAN PROOF)** designed specifically for use with the **$BLUM Mining Game** on Telegram. The clicker detects specific in-game patterns, helping players automate their clicks and avoid obstacles. This tool can help you score **220+ points** in the game, though accuracy may vary. 

> [!IMPORTANT]  
> Do not move the cursor while the auto-clicker is running, as it may click on obstacles (bombs) in the game. If the game gets stuck or the clicker hangs, press **Z** to exit.

## What is $BLUM?

**$BLUM** is a token used in the Blum Mining Game, which is a Telegram-based game where users can mine $BLUM tokens by playing mini-games. The game involves clicking tasks, where avoiding bombs and scoring high points leads to rewards in $BLUM tokens. 

Start playing and mining $BLUM by joining the official Telegram game via this link: **[$Blum Mining on Telegram](https://t.me/blum/app?startapp=ref_V37PFWaO9g)**.

## Features

- **High Score Assistance**: Helps users achieve **220+ score** in the $BLUM mining game.
- **Window-Specific Automation**: Targets the $BLUM game window on Telegram for precise clicks.
- **Start Delay**: Set a delay (in seconds) before the auto-clicker begins.
- **Pause/Resume**: Press **q** at any time to pause and resume the clicking.
- **Exit Button**: Press **z** to stop the clicker and exit the program.
- **Random Click Offsets**: Slightly randomized click positions help avoid bot detection.

## Requirements

- **Python 3.8+**
- Required Python modules:
  - pyautogui
  - pygetwindow
  - pynput
  - keyboard

You can install the dependencies using:

```bash
pip install pyautogui pygetwindow pynput keyboard
```

## How It Works

1. **Window Detection**: The script prompts you to input the window name (e.g., **TelegramDesktop**). It monitors the window to ensure it is active before clicking.

2. **Custom Delay**: You can specify a delay (in seconds) before the clicker begins. This allows you to prepare the game window.

3. **Auto Clicker**: After the delay, the clicker automatically begins clicking within the game window to help score points. 

4. **Control the Script**:
   - **Pause/Resume**: Press **Q** to pause or resume the clicking if needed.
   - **Exit**: Press **Z** to exit the clicker entirely.

## Running Guide

### Option 1: Manual Running Using Commands

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/cu-sanjay/BLUM-Clicker
   cd BLUM-Clicker
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script**:
   ```bash
   python blum.py
   ```

4. **Follow the On-Screen Prompts**:
   - Enter the window name for Telegram (**1** for TelegramDesktop).
   - Set a delay (in seconds) before starting the clicker.
   - The clicker will then begin clicking in the game after the delay.

### Option 2: Running Using `INSTALL.bat` and `START.bat`

#### Step 1: Installation with `INSTALL.bat`

1. **Run `INSTALL.bat`** to automatically install the required libraries:
   - This file installs all necessary Python dependencies for the script.
   - Just double-click the `INSTALL.bat` file, and the installation process will complete automatically.

#### Step 2: Start with `START.bat`

1. **Run `START.bat`** to launch the auto-clicker:
   - Default settings: 2 seconds delay and targeting **TelegramDesktop**.
   - The script will start, and you can pause with **Q** or exit with **Z**.
  
2. **Gameplay**:
   - The clicker will automatically click in the game after the delay.
   - **Q** pauses/resumes the clicker, and **Z** exits the program.

## Benefits

This auto-clicker helps players in the **$BLUM Mining Game** by automating clicks and scoring over **200 points**. With less manual effort, players can focus on their strategy while the script takes care of repetitive actions.

## Telegram Blum Mining Game Link

Start playing and mining **$BLUM** tokens by playing the game on Telegram. [**Mine the $BLUM on Telegram**](https://t.me/blum/app?startapp=ref_V37PFWaO9g)

---

## Disclaimer
> [!CAUTION]
> This script is for educational purposes only. Use of auto-clickers in games or applications may violate their terms of service, so please check the rules before using it. The developers are not responsible for any misuse.
