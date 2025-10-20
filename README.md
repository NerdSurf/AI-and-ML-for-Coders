# AI-and-ML-for-Coders
Follow along with me as I go through and learn to program AI and Machine Learning algorithms, models, and more. Utilizing the AI and Machine Learning for Coders Textbook by O'Reilly,
feel free to make up your own repository and follow along!

Disclaimer:
This repository documents my personal learning process as I work through AI and Machine Learning for Coders by Laurence Moroney (O’Reilly, 2021).
All code, notes, and explanations here are my own unless otherwise stated. Small code snippets or concepts inspired by the book are used under fair use for educational purposes.

# 🧠 Project Setup Guide

If you'd like to follow along or create your own experiments, here’s how to get started:

```bash
# 1. Clone or create your project folder
git clone <your-repo-url>
cd AI-and-ML-for-Coders

# 2. Create and activate a virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

# Recommended Folder Structure
Your folder structure should look something like this:

<pre> AI-and-ML-for-Coders/
├─ .idea/               # IDE settings (PyCharm, optional)
├─ .venv/               # Virtual environment (do NOT commit)
├─ src/                 # Code and chapter notes
│  └─ chapter_1/
│     └─ intro_to_tensorflow.py
├─ README.md
└─ requirements.txt
</pre>

# Configure Your IDE
In PyCharm: 
- Right-click the src/ folder → Mark Directory As → Sources Root

In VS Code:
- Add this to .vscode/settings.json:

```json
{ "python.analysis.extraPaths": ["./src"] }
```

# Running Code

Always run from the project root so imports work correctly:

```bash
python -m chapter_1.intro_to_tensorflow
```

# Chapter README.md navigation
- [Chapter 1: Introduction to TensorFlow](src/chapter_1/README.md)
