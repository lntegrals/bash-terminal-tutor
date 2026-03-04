# 🖥️ Bash Terminal Tutor

An interactive, fun way to learn bash terminal commands! Built for kids and beginners.

![Bash Terminal Tutor](https://img.shields.io/badge/Learning-Fun!-00ff88)

## ✨ Features

- **🎮 Interactive Terminal** - Type real commands and see actual results!
- **📚 5 Progressive Lessons** - From basics to permissions
- **⭐ Gamification** - Earn stars and achievements
- **💡 Hints System** - Get help when you're stuck
- **🎨 Kid-Friendly UI** - Bright colors, fun animations
- **📱 Works on Any Device** - Browser-based learning

## 🚀 Quick Start (GitHub Pages - Static)

Just visit: **https://lntegrals.github.io/bash-terminal-tutor/**

No installation needed! The static version has simulated commands for learning.

## 🛠️ Full Interactive Version (With Real Command Execution)

### Prerequisites
- Python 3.8+
- Docker (for sandboxed command execution)

### Run Locally

```bash
# Clone the repo
git clone https://github.com/lntegrals/bash-terminal-tutor.git
cd bash-terminal-tutor

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

Then open http://localhost:5000

### Deploy to Render/Railway/Vercel

1. Connect your GitHub repo
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `gunicorn app:app`
4. Deploy!

## 📚 Lessons

| # | Lesson | Commands |
|---|--------|----------|
| 1 | 🚀 Welcome | pwd, ls, whoami |
| 2 | 📁 Moving Around | cd, cd .., cd ~ |
| 3 | 📝 Creating Things | mkdir, touch, rm |
| 4 | 🔍 Finding Things | grep, find |
| 5 | 🔐 Permissions | chmod, ls -l |

## 🏆 Achievements

- 🚀 **First Command** - Complete your first command
- 🔍 **Explorer** - Complete 3 lessons
- ✨ **Creator** - Earn 3 stars
- 🏆 **Master** - Complete all lessons

## 🔒 Security

The backend uses a **whitelist approach** - only safe commands are allowed:
- Navigation: `pwd`, `ls`, `cd`
- File ops: `mkdir`, `touch`, `rm`, `cp`, `mv`
- Reading: `cat`, `head`, `tail`
- Search: `grep`, `find`

Commands run in an **isolated sandbox** - students can't break anything!

## 🎓 Educational Goals

By the end of this course, students will be able to:
- [ ] Navigate the file system
- [ ] Create and manage files and folders
- [ ] Search for content in files
- [ ] Understand basic permissions
- [ ] Use pipes to chain commands

## 🤝 Contributing

Pull requests welcome! This is a learning project - let's make it better together.

## 📝 License

MIT License - Learn freely!

---

Made with ❤️ for aspiring terminal masters!
