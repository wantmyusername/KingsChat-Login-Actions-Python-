# KingsChat Login Actions — Python

Session and action automation for [KingsChat](https://web.kingsch.at/) built with **Python + Selenium + Firefox**.

The script reads a list of accounts, logs into each one, and performs configurable actions: **publish a status**, **like**, **share**, and **comment** on a post.

## What it does

For each account in `Names.csv`:

1. Opens `https://web.kingsch.at/` and logs in.
2. Publishes a random status from `Status.txt`.
3. Opens the post URL set in `Post.txt`.
4. Optionally: **like**, **share**, and/or **comment** (random comment from `Comentarios.txt`).
5. Clears cookies and moves on to the next account.

## Files

| File | Description |
|---|---|
| `navegador.py` | Main script (Selenium / Firefox). |
| `Names.csv` | Account list, one per line: `email,password`. **Not tracked** (see `.gitignore`). |
| `Names.example.csv` | Example format for `Names.csv`. |
| `Post.txt` | Target post URL. |
| `Status.txt` | Candidate statuses (one is picked at random). |
| `Comentarios.txt` | Candidate comments (one is picked at random). |
| `geckodriver.exe` | Firefox driver for Windows. **Not tracked.** |

## Configuration

In `navegador.py`, toggle each action with these flags:

```python
oLike    = "OFF"   # Like the post        (ON / OFF)
oShare   = "OFF"   # Share the post       (ON / OFF)
oComment = "OFF"   # Comment on the post  (ON / OFF)
```

## Requirements

- Python with `selenium` (`pip install selenium`).
- Mozilla Firefox installed.
- `geckodriver` available on your `PATH`.

## Setup

Create your local, untracked `Names.csv` from the example:

```bash
cp Names.example.csv Names.csv
# then edit Names.csv with your accounts: email,password
```

## Usage

```bash
# 1. Put accounts in Names.csv (one per line: email,password)
# 2. Adjust the flags in navegador.py
# 3. Adjust Post.txt, Status.txt and Comentarios.txt
python navegador.py
```

## Notes

- The code targets **Python 2** and an old Selenium version (it uses `find_element_by_xpath`, `firefox_profile`, and `print e`). Running it today requires updating to Python 3 and Selenium 4.
- The XPaths match the site's markup and may break when the site changes.
- Use it only with your own accounts and in compliance with the platform's terms of service.
