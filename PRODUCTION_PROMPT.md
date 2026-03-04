# Bash Terminal Tutor - Production Ready

## Prompt for Self-Correction

You built a bash learning app but it's NOT interactive or useful. Here's how to fix it:

### Requirements for Production-Ready Kids Learning App:

1. **REAL Command Execution** - Kids need to actually run bash commands, not see simulated output
2. **Interactive Lessons** - Step-by-step with clear objectives
3. **Visual Feedback** - Immediate rewards (stars, confetti, progress bars)
4. **Kid-Friendly UI** - Bright colors, big buttons, fun animations
5. **Progressive Difficulty** - Start easy, get harder
6. **Hints System** - Help when stuck
7. **Achievements** - Badges for completing lessons
8. **Terminal That Works** - Use xterm.js for real terminal experience

### Architecture:

**Option A: Full-Stack (Recommended)**
- Frontend: React/Next.js with xterm.js
- Backend: Python/FastAPI with Docker sandbox for command execution
- Deploy: Vercel + Railway/Render

**Option B: Hybrid**
- Frontend: Static HTML/JS with xterm.js
- Backend: Simple Flask server (deployable anywhere)
- Commands execute in restricted container

### Key Features to Build:

1. **Lesson System**
   - Navigation → Files → Search → Permissions → Pipes
   - Each lesson: Concept → Examples → Challenge → Quiz

2. **Terminal Component**
   - Real command input with xterm.js
   - Output rendered with syntax highlighting
   - Command history support

3. **Progress Tracking**
   - LocalStorage for progress
   - Stars per lesson (1-3 based on attempts)
   - Total score display

4. **Gamification**
   - Achievement badges
   - Streak counter
   - Celebration animations

### Files to Create:

```
bash-terminal-tutor/
├── app.py                  # Flask backend for command execution
├── sandbox.py              # Restricted shell execution
├── static/
│   ├── index.html         # Main app
│   ├── styles.css        # Kid-friendly styling
│   └── app.js            # Frontend logic with xterm.js
├── lessons/
│   └── *.json            # Lesson content
├── requirements.txt
└── Dockerfile             # For sandboxed deployment
```

### Execution Safety:
NEVER allow direct shell access. Use:
- Docker containers with limited commands
- OR whitelist of allowed commands (ls, cd, pwd, mkdir, etc.)
- OR gvisor-based sandbox

---

Now BUILD this properly!
