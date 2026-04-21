![Mind's Eye](static/Mindseyebanner.png)

**By Wizardwerks Enterprise Labs**

[![Play Now](https://img.shields.io/badge/Play%20Now-Live%20Demo-ff8c00?style=flat-square)](https://mindseye.up.railway.app)

---

Mind's Eye is a browser-based memory card matching game built in Python and Flask. Test your focus and recall across three difficulty tiers — the board gets harder, the clock keeps running, and your score lives on the leaderboard until someone beats it.

![Python](https://img.shields.io/badge/Python-3.10+-ffd000?style=flat-square&logo=python&logoColor=black)
![Flask](https://img.shields.io/badge/Flask-3.0-ff8c00?style=flat-square&logo=flask&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## Features

- **Three difficulty modes** — Easy (8 pairs), Medium (12 pairs), Hard (16 pairs)
- **Live HUD** — move counter and timer running in real time throughout each game
- **Persistent leaderboard** — top 10 scores per difficulty saved to disk, ranked by fewest moves then fastest time
- **Initials entry** — enter your 3-letter tag when you win and claim your spot
- **16 unique symbols** — each game draws from a pool of emoji-based card faces
- **Retro aesthetic** — Press Start 2P pixel font, dark terminal background, scanline grid, orange and teal color scheme consistent with the Wizardwerks design language

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.10+, Flask 3.0 |
| Session | Flask server-side sessions |
| Storage | JSON flat file (scores.json) |
| Frontend | Vanilla HTML/CSS/JS |
| Fonts | Press Start 2P, VT323 |

---

## Installation

```bash
pip install flask
```

## Running Mind's Eye

```bash
python app.py
```

Open your browser to: **http://localhost:5000**

---

## How to Play

1. Select a difficulty — **Easy**, **Medium**, or **Hard**
2. Click **START** to begin
3. Flip any card to reveal its symbol
4. Flip a second card — if the symbols match, they stay revealed
5. If they don't match, both cards flip back after a short delay
6. Clear all pairs to win
7. Enter your initials to save your score to the leaderboard

The leaderboard ranks by **fewest moves first**, then **fastest time** as a tiebreaker.

---

## Project Structure

```
mindseye/
├── app.py               # Flask application & game logic
├── requirements.txt
├── README.md
├── scores.json          # Persistent leaderboard storage
├── static/
│   └── mindseye.png     # App icon
└── templates/
    └── index.html       # Single-page game UI
```

---

## Part of the Wizardwerks Universe

Mind's Eye is a standalone game — but it shares the same design DNA as the rest of the Wizardwerks portfolio. Same fonts. Same dark aesthetic. Same attention to making something feel complete rather than just functional.

- 🛡️ [Arcane Defense Suite](https://github.com/JMitchTech/ARCANE-Defense-Suite) — Cybersecurity platform
- 🏢 [Wizardwerks HomeLab](https://github.com/JMitchTech/wizardwerks-homelab) — Enterprise infrastructure lab
- 🏔️ [SARPack](https://github.com/JMitchTech/SARPack) — Wilderness rescue operations platform
- 🚛 [LanePRO](https://github.com/JMitchTech/LanePRO) — Transportation management system

---

*Built by Wizardwerks Enterprise Labs*
