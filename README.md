# qooxdoo Widget Browser Automation

This project uses Python and Playwright's synchronous API to open the qooxdoo
Widget Browser and interact with its Form, Tree, List, Table, Toolbar/Menu,
Window, Tab, Control, Embed, EmbedFrame, Basic, and Misc pages.

## Prerequisites

- Python 3.10 or newer
- Internet access to open the Widget Browser

## Install dependencies

From this folder, create and activate a virtual environment, then install the
packages:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Install the Playwright browser

Install Playwright's Chromium browser:

```powershell
python -m playwright install chromium
```

## Run the automation

Run the script from this folder:

```powershell
python widget.py
```

The browser window is visible while the script works through the widget pages.
