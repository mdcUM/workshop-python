# Workshop-python

A tiny Python project used in MDC TechDev Workshop 1. It calls a free public API
and prints a random piece of advice to your terminal — a quick way to confirm
that Python and pip are working on your machine.

## What's in here

- `app.py` — the whole program (about 35 lines)
- `requirements.txt` — the two small libraries it depends on

## Requirements

- Python 3.8 or newer
- pip (comes with Python)
- An internet connection (the script calls a public API)

## Setup

1. **Clone this repository** (if you haven't already):
   ```bash
   git clone https://github.com/mdcUM/workshop-python
   cd workshop-python
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   > Windows users: if `pip` isn't recognized, try `python -m pip install -r requirements.txt`

3. **Run the program:**
   ```bash
   python3 app.py
   ```
   > Windows users: use `python app.py` instead of `python3 app.py`

## What you should see

```
✨ Random Advice Generator ✨

"Don't be afraid to ask questions."

Press Enter for more advice, or type 'q' to quit:
```

Press **Enter** to get another piece of advice, or type **q** and press Enter to quit.

## Troubleshooting

- **"python3: command not found" / "python: command not found"** — Python isn't
  installed yet, or your terminal needs to be restarted after installing it.
- **"No module named requests" (or colorama)** — step 2 above didn't run, or it
  installed to a different Python than the one running `app.py`. Try step 2 again.
- **No internet connection** — this script needs internet access to fetch advice
  from the API.
