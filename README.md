# qooxdoo Widget Browser Automation

This project uses Python and Playwright's synchronous API to open the qooxdoo
Widget Browser. The original `widget.py` script is kept as a reference, and
the `pages/` and `tests/` folders contain the Page Object Model implementation
and pytest suite.

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

Run the original reference script from this folder:

```powershell
python widget.py
```

The browser window is visible while the script works through the widget pages.

## Run the POM test suite

Run all tests from this folder:

```powershell
python -m pytest tests -v
```

The test suite uses pytest-playwright's `page` fixture to open Chromium and
exercises the Form, Tree and VirtualTree, List, Table, Toolbar/Menu, Window,
Tab, Control, Embed, EmbedFrame, Basic, and Misc demos.
