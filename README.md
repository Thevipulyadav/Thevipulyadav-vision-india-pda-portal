# Vision India : PDA (Plan, Develop & Ascent) Portal
### Inspired by Shri Akhilesh Yadav's *Vision India* & Samajwadi Party Website

An interactive, responsive full-stack Python web platform built around the **PDA (Plan, Develop & Ascent | Pichhde, Dalit, Alpasankhyak)** philosophy for **Neo India**.

---

## 🌟 Key Features

1. **Brand Identity & Philosophy**:
   - Modern Samajwadi Red & Emerald Green visual identity (`#d32f2f` & `#15803d`).
   - The **PDA Triad**:
     - **Plan (योजना)**: Progressive policies, tech incubators, youth entrepreneurship & democratic safeguards.
     - **Develop (विकास)**: World-class expressways, high-speed metro transit, universal healthcare, and agro-logistics.
     - **Ascent (उत्थान)**: Social justice, equal representation, women autonomy, and caste census.

2. **Flagship Highlights & Milestones**:
   - Spotlight on **Vision India Startup Summit (Taj Bangalore)**.
   - Proven track record showcase: Agra-Lucknow Expressway (fighter jet runway), 18+ Lakh Free Laptops, 1090 Women Powerline, Lucknow Metro, Super-Specialty Healthcare.

3. **Bilingual Support (English & हिन्दी)**:
   - Dynamic real-time language switcher (`English` $\leftrightarrow$ `हिन्दी`) for accessibility across India.

4. **Interactive Portals**:
   - **RSVP System**: Interactive modal registration for summits and conclaves.
   - **PDA Volunteer Portal**: Categorized registration for tech, legal, student, and rural organizers.
   - **Direct Feedback & Inquiries**: Real-time form submissions.
   - **Admin Dashboard**: Live metrics, tables for volunteers, RSVPs, and contact messages.

---

## 🚀 How to Run in VS Code

### Method 1: Play Button (Easiest)
1. Open the project in VS Code:
   ```powershell
   code .
   ```
2. Open [main.py](file:///c:/Users/vipul/OneDrive/Desktop/PDA/main.py).
3. Click the **▷ (Run Python File)** button in the top-right corner, or press **`F5`**.

### Method 2: Integrated Terminal
1. Open the terminal in VS Code (`Ctrl + ` `).
2. Run:
   ```powershell
   .\.venv\Scripts\python.exe main.py
   ```
3. Open your browser at: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**.

---

## 📁 Project Architecture

```
PDA/
├── app.py                   # Main Flask application with routes and API handlers
├── main.py                  # Entrypoint runner for VS Code & CLI
├── database.py              # SQLite storage for volunteers, RSVPs, messages
├── requirements.txt         # Dependencies (Flask >= 3.1.0)
├── pda.db                   # SQLite database
├── .vscode/
│   ├── settings.json        # Auto-configures .venv Python interpreter
│   └── launch.json          # F5 debug/run configuration
├── static/
│   ├── css/
│   │   └── custom.css       # Custom animations, Samajwadi themes & gradients
│   └── js/
│       ├── main.js          # Client AJAX submissions, RSVP modal, toast notifications
│       └── translations.js  # Bilingual (EN/HI) dictionary
└── templates/
    ├── base.html            # Core layout with navigation, bilingual switcher, footer
    ├── index.html           # Landing page with Hero, PDA Triad, Summit banner & Milestones
    ├── blueprint.html       # Comprehensive policy roadmap
    ├── achievements.html    # Landmark milestone achievements showcase
    ├── events.html          # Summits, Conclaves, and RSVP system
    ├── volunteer.html       # Volunteer registration portal
    └── admin.html           # Management dashboard & data tables
```
