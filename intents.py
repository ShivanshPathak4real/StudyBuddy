"""
intents.py — StudyBuddy AI
===========================
Defines the complete intent database:
  - Keyword triggers for each intent
  - Multiple randomised responses per intent
  - Resource recommendations for CS topics
"""

import random

# ─────────────────────────────────────────────
# INTENT DEFINITIONS
# Each intent:  { "keywords": [...], "responses": [...] }
# ─────────────────────────────────────────────

INTENTS = {

    # ── GREETINGS ──────────────────────────────────────────────────────────
    "greeting": {
        "keywords": ["hello", "hi", "hey", "howdy", "hiya", "sup", "greetings", "good morning",
                     "good afternoon", "good evening", "what's up", "whatsup"],
        "responses": [
            "Hello, future engineer! 🚀 I'm StudyBuddy AI — your 24/7 learning companion. Ask me about any CS topic, get study tips, or just say what's on your mind!",
            "Hey there, learner! 👋 Great to see you! Whether it's Python, DSA, AI, or just needing a motivational boost — I've got you covered. What are we exploring today?",
            "Hi! Ready to build something amazing today? 💡 Type a topic like *Python*, *DSA*, or *Web Dev*, or ask for *study tips* and *motivation*.",
            "Welcome back, scholar! 🎓 I'm here to guide, encourage, and occasionally drop a programming joke. What's the plan for today?",
            "Greetings, coder-in-training! ⚡ Ask me anything — CS topics, roadmaps, resources, or even a fun fact. Let's get started!"
        ]
    },

    # ── FAREWELL ───────────────────────────────────────────────────────────
    "farewell": {
        "keywords": ["bye", "goodbye", "exit", "quit", "see you", "later", "cya", "farewell",
                     "take care", "signing off", "good night"],
        "responses": [
            "Goodbye, champion! 👋 Every line of code you write today brings you closer to your goals. Keep building! 🚀",
            "See you soon! 🌟 Remember: consistency beats perfection. Come back anytime — I'll be here!",
            "Bye! 💪 The best time to start was yesterday; the second best time is NOW. Go get 'em!",
            "Take care! ✨ You're one study session away from a breakthrough. See you next time!",
            "Farewell, learner! 🎯 Don't forget — great developers are made, not born. Keep going!"
        ]
    },

    # ── ABOUT / IDENTITY ───────────────────────────────────────────────────
    "about": {
        "keywords": ["who are you", "what are you", "about you", "tell me about yourself",
                     "your name", "introduce yourself", "what is studybuddy", "about studybuddy"],
        "responses": [
            "I'm **StudyBuddy AI** 🤖 — a smart, rule-based student mentor designed to help you conquer computer science!\n\n📚 I can help you with:\n• CS topics & roadmaps (Python, DSA, AI, Web Dev, and 15+ more)\n• Study tips & productivity hacks\n• Motivation when you're feeling stuck\n• Resources, YouTube channels & practice platforms\n\nI'm not powered by an LLM — I'm 100% rule-based Python, which means I'm fast, predictable, and built with love! 💙",
            "**StudyBuddy AI** here! 🎓 Think of me as your senior peer who actually answers your messages at 2 AM.\n\nI know about: Python, Java, C++, DSA, DBMS, OS, Networks, AI/ML, Web Development, Git, and much more.\n\nBuilt with Python + Flask + Vanilla JS. Ask me anything!"
        ]
    },

    # ── HELP ───────────────────────────────────────────────────────────────
    "help": {
        "keywords": ["help", "commands", "what can you do", "options", "menu", "guide", "how to use"],
        "responses": [
            "Here's what I can do for you! 🗺️\n\n**📖 CS Topics:**\nPython • Java • C++ • C • JavaScript • HTML • CSS • SQL\nDSA • Algorithms • OOP • DBMS • OS • Networks\nAI • Machine Learning • Deep Learning • Web Dev • Git\n\n**💡 Study & Life:**\nStudy Tips • Productivity • Motivation • Stress Relief\nConcentration • Procrastination • Exam Tips\n\n**🎲 Fun:**\nProgramming Jokes • Fun Facts\n\nJust type any keyword or topic name!",
            "I'm your all-in-one CS study companion! Try asking:\n\n🐍 *\"Learn Python\"* — roadmap + resources\n📊 *\"Data Structures\"* — full DSA guide\n🤖 *\"Artificial Intelligence\"* — AI learning path\n💪 *\"I'm stressed\"* — motivation boost\n😄 *\"Tell me a joke\"* — you deserve a laugh!\n\nOr click any Quick Action button below! 👇"
        ]
    },

    # ── STUDENT SUPPORT: STRESS ────────────────────────────────────────────
    "stressed": {
        "keywords": ["stressed", "stress", "overwhelmed", "anxious", "anxiety", "pressure",
                     "too much", "can't handle", "breaking down", "burnout"],
        "responses": [
            "Hey, I hear you. 💙 Stress is real, and it's okay to feel overwhelmed sometimes.\n\n**Quick stress-busters:**\n• Take a 5-minute walk — seriously, it works 🚶\n• Use the **Pomodoro Technique**: 25 min study, 5 min break ⏱️\n• Drink water and breathe deeply 💧\n• Write down your top 3 tasks — clarity kills chaos ✍️\n\nYou've survived 100% of your hard days so far. This one is no different. 💪",
            "Breathe. 🌬️ You've got this.\n\nWhen everything feels like too much, zoom out. You're building skills that most people never will. That's worth the struggle.\n\n**Try this:** Close everything, set a 25-minute timer, and focus on just ONE thing. One task. One step. That's all it takes to break the cycle. You're stronger than you think! 🌟"
        ]
    },

    # ── STUDENT SUPPORT: TIRED ─────────────────────────────────────────────
    "tired": {
        "keywords": ["tired", "exhausted", "sleepy", "no energy", "fatigue", "drained",
                     "worn out", "need rest", "so tired"],
        "responses": [
            "Rest is not laziness — it's part of the process. 😴\n\n**Your body is signalling something important.** Here's what top developers do:\n• Sleep 7-8 hours — your brain consolidates memory during sleep 🧠\n• Take short power naps (15-20 min) when needed 💤\n• Don't study while exhausted — you retain almost nothing\n\nThe most productive thing you can do right now might be to rest. Come back refreshed and you'll learn 2x faster. 🚀",
            "Even machines need to recharge! 🔋 Don't feel guilty about needing rest.\n\nTip: Try the **20-20-20 rule** for screen fatigue — every 20 minutes, look at something 20 feet away for 20 seconds. 👀\n\nYou're playing a long game. Take care of yourself, and the code will still be there tomorrow. 💙"
        ]
    },

    # ── STUDENT SUPPORT: DEMOTIVATED ───────────────────────────────────────
    "demotivated": {
        "keywords": ["demotivated", "unmotivated", "no motivation", "give up", "want to quit",
                     "what's the point", "useless", "can't do this", "not good enough"],
        "responses": [
            "Let me be real with you for a second. 🔥\n\nEvery developer you admire — every Google engineer, every open-source hero — had a day where they felt exactly like you do right now. They didn't quit.\n\n**Remember why you started.** Is it freedom? Money? Building things? Impact?\n\nYou don't need motivation every day. You need *discipline* — and you're building it right now, just by being here. That's not nothing. That's everything. 💪",
            "You know what? Feeling demotivated is normal. It means you care enough to notice the gap between where you are and where you want to be. That gap is called *growth*. 🌱\n\n**Quick motivation hack:** Find one tiny win. Run one program. Solve one LeetCode easy. Read one page. Small wins compound into big results.\n\nYou're closer than you think. Don't stop now! 🚀"
        ]
    },

    # ── STUDENT SUPPORT: FAILED EXAM ───────────────────────────────────────
    "failed_exam": {
        "keywords": ["failed", "fail", "bad marks", "bad grades", "low score", "flunked",
                     "didn't pass", "poor result", "scored badly", "exam went bad"],
        "responses": [
            "That stings, I know. 💙 But here's the truth: a bad exam is data, not a destiny.\n\n**What to do now:**\n1. 📋 Review *what* went wrong — concept gaps? Time management? Anxiety?\n2. 🎯 Target those specific weak areas, not everything\n3. ⏱️ Use spaced repetition for better retention\n4. 🤝 Form a study group or find a mentor\n\nJK Rowling was rejected 12 times. Michael Jordan was cut from his high school team. Your setback is setting up your comeback. 💪",
            "One exam doesn't define your intelligence, your career, or your worth. 🌟\n\nSome of the best developers I know graduated with average marks. What set them apart? They kept building, kept learning, kept going.\n\n**Your action plan:** Identify the weak topic, spend 3 focused days on it, and watch how quickly things click. You've got this! 🎯"
        ]
    },

    # ── STUDENT SUPPORT: PROCRASTINATION ───────────────────────────────────
    "procrastination": {
        "keywords": ["procrastinating", "procrastination", "lazy", "not studying", "keep delaying",
                     "distracted", "can't focus", "wasting time", "social media", "phone addiction"],
        "responses": [
            "Ah, procrastination — the final boss of productivity! 😅\n\n**Beat it with science:**\n• **2-Minute Rule:** If it takes less than 2 minutes, do it NOW ⚡\n• **Pomodoro:** 25 min work, 5 min break — gamify your study\n• **Environment design:** Phone in another room, website blockers on\n• **Start ugly:** Open the file. Write one line. Momentum does the rest.\n\nYour future self is begging your present self to start. Listen to them! 🚀",
            "The secret to starting: **don't wait to feel ready**. Feelings follow action, not the other way around.\n\n**Try this right now:**\n1. Open your study material\n2. Set a timer for just 5 minutes\n3. Work for those 5 minutes\n\nI guarantee you'll keep going. The hardest part is always starting. Go! ⚡"
        ]
    },

    # ── STUDY TIPS ─────────────────────────────────────────────────────────
    "study_tips": {
        "keywords": ["study tips", "how to study", "study better", "study smart", "learning tips",
                     "study technique", "study method", "best way to study", "effective studying"],
        "responses": [
            "Here are battle-tested study strategies for CS students! 📚\n\n**🧠 Active Learning:**\n• Don't just read — *code along* with every tutorial\n• Teach concepts to yourself out loud (Feynman Technique)\n• Build mini-projects for every new concept\n\n**⏱️ Time Management:**\n• Pomodoro: 25 min focus + 5 min break\n• Study in the morning when your brain is fresh\n• Review notes within 24 hours to lock them in\n\n**📊 Retention:**\n• Use Anki for spaced repetition flashcards\n• Summarise topics in your own words\n• Solve problems *without* looking at solutions first\n\nConsistency > intensity, always! 🎯",
            "The #1 study secret in CS? **Build things.** 🔨\n\nReading about sorting algorithms is good. Coding them from scratch is 10x better. Applying them to a real project? That's mastery.\n\n**Top 5 CS Study Tips:**\n1. Code every day, even if just 30 minutes 💻\n2. Use official documentation, not just tutorials\n3. Practice on LeetCode/HackerRank regularly\n4. Collaborate — code reviews teach you *fast*\n5. Sleep well — your brain learns while you sleep! 😴"
        ]
    },

    # ── PRODUCTIVITY ───────────────────────────────────────────────────────
    "productivity": {
        "keywords": ["productivity", "productive", "time management", "efficient", "efficiency",
                     "get more done", "work smarter", "habits", "routine", "schedule"],
        "responses": [
            "Productivity isn't about doing more — it's about doing the *right things* well. ⚡\n\n**Developer Productivity Stack:**\n• 🌅 Morning routine: review yesterday, plan today\n• 📝 Daily MIT (Most Important Task): one critical thing per day\n• 🚫 Deep work blocks: 90-minute sessions, no interruptions\n• 📱 Phone-free study: put it in another room\n• 📊 Weekly review: what worked, what didn't\n\n**Tools that help:**\n• Notion or Obsidian for notes\n• Forest app to stay off your phone\n• GitHub for tracking your coding streak 📈",
            "The most productive developers I know all share one habit: **they protect their deep work time** like gold. 🏆\n\n**Anti-productivity traps to avoid:**\n• Multitasking (it's a myth — it reduces quality by 40%)\n• Checking notifications while studying\n• Passive watching without coding along\n• Perfectionism before shipping\n\n**Replace with:**\nTime-blocking + single-tasking + deliberate practice. Simple but transformative! 🎯"
        ]
    },

    # ── CONCENTRATION ──────────────────────────────────────────────────────
    "concentration": {
        "keywords": ["concentration", "focus", "can't concentrate", "mind wandering", "distraction",
                     "attention", "deep work", "flow state"],
        "responses": [
            "Getting into *flow state* is the holy grail of studying. Here's how to get there: 🎯\n\n**Environment Setup:**\n• Dedicated study space (not your bed!)\n• Noise-cancelling headphones + lofi music or white noise\n• Everything you need within reach before starting\n• Phone in a different room (not silent, *gone*)\n\n**Mental Warm-Up:**\n• 2-minute breathing exercise before starting\n• Write down 3 specific goals for the session\n• Start with an easy task to build momentum\n\nFlow usually kicks in after 15-20 minutes. Push through the first resistance! 💪"
        ]
    },

    # ── JOKES ─────────────────────────────────────────────────────────────
    "joke": {
        "keywords": ["joke", "funny", "laugh", "humor", "make me laugh", "tell me a joke",
                     "programming joke", "developer joke"],
        "responses": [
            "Why do programmers prefer dark mode? 🌑\n\n*Because light attracts bugs!* 🐛😂",
            "A QA engineer walks into a bar. Orders 0 beers. Orders 99999999 beers. Orders -1 beers. Orders a lizard. Orders NULL beers. Orders asdfghjkl beers.\n\n*The first real customer walks in and asks: 'Where's the bathroom?'*\n*The bar bursts into flames.* 🔥😂",
            "Why did the developer go broke? 💸\n\n*Because he used up all his cache!* 😂",
            "There are 10 types of people in the world: 🖥️\n\n*Those who understand binary and those who don't.* 😄",
            "A programmer's partner says: *'Go to the store, get a gallon of milk, and if they have eggs, get a dozen.'*\n\nThe programmer comes back with 12 gallons of milk. 🥛😂\n\n*They had eggs.*",
            "Why do Java developers wear glasses? 👓\n\n*Because they don't C#!* 😂"
        ]
    },

    # ── FUN FACTS ──────────────────────────────────────────────────────────
    "fun_fact": {
        "keywords": ["fun fact", "interesting fact", "did you know", "trivia", "cool fact",
                     "teach me something", "random fact"],
        "responses": [
            "🤯 **Fun Fact:** The first computer bug was a literal bug — a moth found stuck in a relay of the Harvard Mark II computer in 1947! Grace Hopper's team taped it into their logbook with the note 'First actual case of bug being found.' 🦗",
            "🤯 **Fun Fact:** Python is named after *Monty Python's Flying Circus*, not the snake. Guido van Rossum was reading Monty Python scripts when he named it! 🐍🎭",
            "🤯 **Fun Fact:** The inventor of the World Wide Web, Tim Berners-Lee, never patented his invention. He gave it to the world for free. Imagine if he had charged $0.01 per visit... 🌐💰",
            "🤯 **Fun Fact:** There are more possible iterations of a chess game than there are atoms in the observable universe. That's why AI chess engines still can't 'solve' chess completely! ♟️🌌",
            "🤯 **Fun Fact:** The Apollo 11 guidance computer that landed humans on the Moon had less processing power than a modern USB-C charger. 🚀💻",
            "🤯 **Fun Fact:** The first programmer in history was Ada Lovelace, in 1843 — over 100 years before modern computers existed! She wrote an algorithm for Charles Babbage's Analytical Engine. 👩‍💻"
        ]
    },

    # ── MOTIVATION ─────────────────────────────────────────────────────────
    "motivation": {
        "keywords": ["motivate me", "motivation", "inspire me", "inspiration", "need motivation",
                     "encourage me", "keep going", "push me", "i can do this"],
        "responses": [
            "🔥 **You are exactly where you need to be.**\n\nEvery line of code you write, every algorithm you study, every bug you fix — it's all compounding. Silently. Powerfully.\n\nThe developers who 'made it' aren't smarter than you. They just refused to stop when it got hard. *Will you?* 💪",
            "⚡ Here's the truth nobody tells you:\n\nYour first 100 programs will be ugly. Your first 50 algorithms will feel impossible. Your first projects will have bugs everywhere.\n\n**And that's completely normal and necessary.**\n\nEvery expert was once a beginner who kept going. Keep going. 🚀",
            "🌟 *'The expert in anything was once a beginner.'*\n\nYou're building skills that will last decades. The discomfort you feel right now is called growth. Lean into it.\n\nFive years from now, you'll look back at this moment and be grateful you didn't quit. 🎯",
            "💡 **Daily reminder:**\n\n• You don't need to be perfect, just persistent\n• Progress > perfection, always\n• One hour of focused study beats six hours of distracted scrolling\n• You chose a path most people won't even attempt\n\nThat already makes you exceptional. Now go prove it. 🔥"
        ]
    },

    # ── EXAM TIPS ──────────────────────────────────────────────────────────
    "exam_tips": {
        "keywords": ["exam tips", "how to prepare exam", "exam preparation", "exam strategy",
                     "before exam", "exam time", "revision", "revise"],
        "responses": [
            "Exam season survival guide! 📝\n\n**1 Week Before:**\n• Make a topic list and check off what you know\n• Focus 80% time on weak areas\n• Solve previous year papers\n• Summarise each topic in bullet points\n\n**Night Before:**\n• Light review only — no new topics\n• Sleep 7-8 hours (your brain needs it!)\n• Prepare everything the night before\n\n**Day Of:**\n• Eat a proper breakfast 🍳\n• Arrive early, read all questions first\n• Easy questions first, hard ones later\n• If stuck, move on and come back\n\nYou've got this! 🎯"
        ]
    },

    # ═══════════════════════════════════════════════════════════════════════
    # CS TOPICS
    # ═══════════════════════════════════════════════════════════════════════

    "python": {
        "keywords": ["python", "learn python", "python programming", "python language"],
        "responses": [
            "🐍 **Python — The Language of the Future**\n\nPython is loved for its clean syntax and massive ecosystem — from web apps to AI/ML, it does it all!\n\n**🗺️ Beginner Roadmap:**\n1. Syntax, Variables, Data Types\n2. Control Flow (if/else, loops)\n3. Functions & Scope\n4. Lists, Tuples, Dicts, Sets\n5. File I/O & Error Handling\n6. OOP in Python\n7. Modules & Packages\n8. Projects: Calculator → CRUD App → Web Scraper\n\n**📚 Resources:**\n• python.org/docs — Official docs\n• freeCodeCamp Python Course (YouTube)\n• Corey Schafer's Python series (YouTube)\n• W3Schools Python\n• CS50P by Harvard (free!)\n\n**💪 Practice:**\n• HackerRank Python domain\n• LeetCode (Easy problems)\n• Exercism Python track\n\n**⏱️ Time to basics:** 4-6 weeks with daily practice"
        ]
    },

    "java": {
        "keywords": ["java", "learn java", "java programming", "java language"],
        "responses": [
            "☕ **Java — Write Once, Run Anywhere**\n\nJava is the backbone of enterprise software, Android development, and competitive programming!\n\n**🗺️ Beginner Roadmap:**\n1. JDK Setup & Hello World\n2. Data Types, Variables, Operators\n3. Control Statements\n4. Methods & Recursion\n5. OOP: Classes, Objects, Inheritance, Polymorphism\n6. Exception Handling\n7. Collections Framework\n8. Threads & Concurrency basics\n\n**📚 Resources:**\n• docs.oracle.com/javase — Official docs\n• MOOC Java by University of Helsinki (free!)\n• Telusko Java Full Course (YouTube)\n• Head First Java (book)\n\n**💪 Practice:**\n• HackerRank Java domain\n• LeetCode with Java\n• CodingBat\n\n**⏱️ Time to basics:** 6-8 weeks"
        ]
    },

    "cpp": {
        "keywords": ["c++", "cpp", "learn c++", "cplusplus"],
        "responses": [
            "⚙️ **C++ — Power and Performance**\n\nC++ is king for competitive programming, game development, and systems programming!\n\n**🗺️ Beginner Roadmap:**\n1. Setup (g++, VSCode/CLion)\n2. I/O, Variables, Data Types\n3. Control Flow, Loops\n4. Functions & Recursion\n5. Arrays, Strings, Pointers\n6. OOP: Classes, Inheritance, Virtual Functions\n7. STL: vector, map, set, queue, stack\n8. Templates & Exception Handling\n\n**📚 Resources:**\n• cppreference.com — Best reference\n• learncpp.com — Excellent free course\n• The Cherno C++ Series (YouTube)\n• Competitive Programmer's Handbook (free PDF)\n\n**💪 Practice:**\n• Codeforces (CP gold standard)\n• LeetCode with C++\n• USACO Guide\n\n**⏱️ Time to basics:** 6-8 weeks"
        ]
    },

    "c_language": {
        "keywords": ["c language", "learn c", "c programming", "c lang"],
        "responses": [
            "🔧 **C — The Foundation of Computing**\n\nUnderstanding C makes you understand computers. OS kernels, embedded systems, and drivers are built in C!\n\n**🗺️ Beginner Roadmap:**\n1. Compilation & Hello World\n2. Variables, Data Types, Operators\n3. Control Flow\n4. Functions\n5. Arrays & Strings\n6. Pointers & Memory Management\n7. Structs & Unions\n8. File I/O\n\n**📚 Resources:**\n• The C Programming Language (K&R book) — timeless classic\n• CS50x by Harvard (free, uses C!)\n• Caleb Curry C Series (YouTube)\n• GeeksforGeeks C tutorials\n\n**💪 Practice:**\n• HackerRank C domain\n• LeetCode\n• CodeChef\n\n**⏱️ Time to basics:** 4-6 weeks"
        ]
    },

    "javascript": {
        "keywords": ["javascript", "js", "learn javascript", "java script"],
        "responses": [
            "🌐 **JavaScript — Language of the Web**\n\nJS runs in every browser and on servers (Node.js). It's essential for web development!\n\n**🗺️ Beginner Roadmap:**\n1. Variables, Data Types, Operators\n2. Functions & Scope\n3. DOM Manipulation\n4. Events & Event Listeners\n5. Arrays, Objects, JSON\n6. ES6+: Arrow functions, Destructuring, Spread\n7. Promises & Async/Await\n8. Fetch API & REST APIs\n9. Intro to a framework (React/Vue)\n\n**📚 Resources:**\n• javascript.info — Best JS resource online\n• MDN Web Docs\n• freeCodeCamp JS Curriculum\n• Traversy Media (YouTube)\n• Fireship (YouTube) — amazing short tutorials\n\n**💪 Practice:**\n• js30.com (30 JS projects)\n• Frontend Mentor\n• LeetCode\n\n**⏱️ Time to basics:** 4-6 weeks"
        ]
    },

    "html": {
        "keywords": ["html", "learn html", "html5", "html basics"],
        "responses": [
            "🏗️ **HTML — Structure of the Web**\n\nHTML is where every web developer starts. It's the skeleton of every webpage!\n\n**🗺️ Beginner Roadmap:**\n1. Document structure (html, head, body)\n2. Headings, Paragraphs, Links\n3. Images, Lists, Tables\n4. Forms & Input elements\n5. Semantic HTML5 elements\n6. Meta tags & SEO basics\n7. Accessibility attributes\n\n**📚 Resources:**\n• MDN HTML Reference — gold standard\n• W3Schools HTML\n• freeCodeCamp Responsive Web Design\n• Kevin Powell (YouTube) — CSS + HTML king\n\n**⏱️ Time to basics:** 1-2 weeks (it's fast!)\n\n**Pair with:** CSS and JavaScript for real projects 🎨"
        ]
    },

    "css": {
        "keywords": ["css", "learn css", "css3", "styling", "css basics"],
        "responses": [
            "🎨 **CSS — Make the Web Beautiful**\n\nCSS is the styling language that makes websites look amazing!\n\n**🗺️ Beginner Roadmap:**\n1. Selectors, Properties, Values\n2. Box Model (margin, padding, border)\n3. Display: block, inline, flex, grid\n4. Flexbox — master this first!\n5. CSS Grid\n6. Responsive Design & Media Queries\n7. Animations & Transitions\n8. CSS Variables & Custom Properties\n9. Frameworks: Bootstrap or Tailwind CSS\n\n**📚 Resources:**\n• MDN CSS Reference\n• css-tricks.com — amazing guides\n• Kevin Powell (YouTube) — literally the CSS king 👑\n• Flexbox Froggy (interactive game)\n• Grid Garden (interactive game)\n\n**⏱️ Time to basics:** 2-3 weeks"
        ]
    },

    "sql": {
        "keywords": ["sql", "learn sql", "database query", "mysql", "postgresql", "sqlite"],
        "responses": [
            "🗄️ **SQL — Talk to Databases**\n\nSQL is the universal language for databases — every developer needs to know it!\n\n**🗺️ Beginner Roadmap:**\n1. SELECT, FROM, WHERE\n2. INSERT, UPDATE, DELETE\n3. ORDER BY, GROUP BY, HAVING\n4. JOINs (INNER, LEFT, RIGHT, FULL)\n5. Subqueries\n6. Indexes & Performance\n7. Transactions & ACID\n8. Stored Procedures & Views\n\n**📚 Resources:**\n• SQLZoo — interactive SQL learning\n• Mode Analytics SQL Tutorial\n• CS50 SQL course (free!)\n• W3Schools SQL\n• PostgreSQL official docs\n\n**💪 Practice:**\n• HackerRank SQL domain\n• LeetCode Database problems\n• SQLFiddle for testing\n\n**⏱️ Time to basics:** 2-3 weeks"
        ]
    },

    "dsa": {
        "keywords": ["dsa", "data structures", "algorithms", "data structure", "algorithm",
                     "learn dsa", "arrays", "linked list", "trees", "graphs", "sorting", "searching"],
        "responses": [
            "📊 **Data Structures & Algorithms — The Heart of CS**\n\nDSA is what separates good developers from great ones. Every top tech interview tests this!\n\n**🗺️ Learning Roadmap:**\n\n**Phase 1 — Data Structures:**\n• Arrays & Strings\n• Linked Lists (Singly, Doubly)\n• Stacks & Queues\n• Hash Tables\n• Trees (Binary, BST, AVL)\n• Heaps & Priority Queues\n• Graphs\n\n**Phase 2 — Algorithms:**\n• Sorting (Bubble, Selection, Merge, Quick)\n• Binary Search\n• Recursion & Backtracking\n• BFS & DFS\n• Dynamic Programming\n• Greedy Algorithms\n• Divide & Conquer\n\n**📚 Resources:**\n• NeetCode.io — best structured DSA site\n• GeeksforGeeks\n• Abdul Bari Algorithms (YouTube) ⭐\n• Striver's DSA Sheet\n• CLRS Book (Introduction to Algorithms)\n\n**💪 Practice:**\n• LeetCode (start with Easy, then Medium)\n• Codeforces\n• HackerRank\n\n**⏱️ Timeline:** 3-6 months for solid mastery"
        ]
    },

    "dbms": {
        "keywords": ["dbms", "database management", "database systems", "normalization",
                     "er diagram", "rdbms", "transactions"],
        "responses": [
            "🗃️ **DBMS — Database Management Systems**\n\nDBMS is core CS theory that every developer and data engineer should know!\n\n**🗺️ Key Topics:**\n1. ER Diagrams & Relational Model\n2. SQL (DDL, DML, DCL, TCL)\n3. Normalization (1NF, 2NF, 3NF, BCNF)\n4. Transactions & ACID Properties\n5. Concurrency Control\n6. Indexing & B-Trees\n7. Query Optimization\n8. NoSQL Databases (MongoDB, Redis)\n\n**📚 Resources:**\n• Database System Concepts (Silberschatz) — the textbook\n• Gate Smashers DBMS (YouTube) — great for exams\n• CMU Database Group (YouTube) — advanced\n• GeeksforGeeks DBMS\n\n**⏱️ Time to cover:** 4-6 weeks for exam prep"
        ]
    },

    "os": {
        "keywords": ["operating systems", "os", "operating system", "kernel", "process",
                     "thread", "scheduling", "memory management", "deadlock"],
        "responses": [
            "💻 **Operating Systems — The Brain of a Computer**\n\nOS knowledge is essential for system design, interviews, and understanding how software really works!\n\n**🗺️ Key Topics:**\n1. Process Management (PCB, States, Scheduling)\n2. Threads & Concurrency\n3. CPU Scheduling Algorithms (FCFS, SJF, Round Robin)\n4. Deadlocks (Detection, Prevention, Avoidance)\n5. Memory Management (Paging, Segmentation)\n6. Virtual Memory & Page Replacement\n7. File Systems (FAT, NTFS, ext4)\n8. I/O Management\n\n**📚 Resources:**\n• Operating System Concepts (Silberschatz — Dinosaur Book)\n• Gate Smashers OS (YouTube)\n• Neso Academy OS (YouTube)\n• OSTEP (OS: Three Easy Pieces) — free online!\n\n**⏱️ Time to cover:** 4-6 weeks"
        ]
    },

    "networks": {
        "keywords": ["computer networks", "networking", "network", "tcp", "ip", "http",
                     "dns", "osi model", "protocols"],
        "responses": [
            "🌐 **Computer Networks — How Data Travels the World**\n\nNetworking knowledge is critical for web dev, cloud, DevOps, and cybersecurity!\n\n**🗺️ Key Topics:**\n1. OSI Model (7 layers) & TCP/IP Model\n2. Protocols: HTTP/S, FTP, SMTP, DNS, DHCP\n3. IP Addressing & Subnetting\n4. TCP vs UDP\n5. Routing Algorithms\n6. Application Layer Protocols\n7. Network Security basics\n8. Socket Programming\n\n**📚 Resources:**\n• Computer Networking: A Top-Down Approach (Kurose & Ross)\n• Gate Smashers Networks (YouTube)\n• PowerCert Animated Videos (YouTube)\n• Neso Academy Computer Networks\n• Cisco Networking Academy (free!)\n\n**⏱️ Time to cover:** 4-5 weeks"
        ]
    },

    "oop": {
        "keywords": ["oop", "object oriented", "object-oriented", "classes", "inheritance",
                     "polymorphism", "encapsulation", "abstraction"],
        "responses": [
            "🧩 **Object-Oriented Programming — Think in Objects**\n\nOOP is a fundamental programming paradigm used in Python, Java, C++, and most modern languages!\n\n**🗺️ Core Concepts:**\n1. **Classes & Objects** — Blueprint and instances\n2. **Encapsulation** — Hiding internal details\n3. **Inheritance** — Reusing and extending classes\n4. **Polymorphism** — Same interface, different behavior\n5. **Abstraction** — Showing only what's necessary\n\n**Advanced OOP:**\n• Design Patterns (Singleton, Factory, Observer)\n• SOLID Principles\n• UML Class Diagrams\n• Abstract Classes & Interfaces\n\n**📚 Resources:**\n• Head First Object-Oriented Analysis and Design\n• Refactoring.Guru — excellent design patterns resource\n• Tech With Tim OOP series (YouTube)\n\n**🐍 Best language to learn OOP:** Python (clean syntax!) or Java"
        ]
    },

    "webdev": {
        "keywords": ["web development", "web dev", "webdev", "full stack", "frontend",
                     "backend", "full-stack", "web application"],
        "responses": [
            "🌐 **Web Development — Build the Internet**\n\nWeb dev is one of the most in-demand skills in tech!\n\n**🗺️ Full-Stack Roadmap:**\n\n**Frontend:**\n• HTML → CSS → JavaScript\n• Responsive Design (Flexbox, Grid)\n• React.js (most popular framework)\n• TypeScript\n\n**Backend:**\n• Choose: Node.js / Python (Django/Flask) / Java (Spring)\n• REST API Design\n• Authentication (JWT, OAuth)\n• SQL + NoSQL databases\n\n**DevOps Basics:**\n• Git & GitHub\n• Deployment (Vercel, Netlify, Railway)\n• Docker basics\n\n**📚 Resources:**\n• The Odin Project — free, project-based curriculum ⭐\n• freeCodeCamp\n• roadmap.sh — visual roadmaps for everything\n• Traversy Media (YouTube)\n• Kevin Powell for CSS (YouTube)\n\n**⏱️ Junior dev ready in:** 6-12 months of dedicated study"
        ]
    },

    "git": {
        "keywords": ["git", "github", "version control", "git commands", "branching",
                     "pull request", "merge", "repository", "clone"],
        "responses": [
            "🔀 **Git & GitHub — Essential Developer Tools**\n\nEvery developer needs Git. Period. Start using it from day 1!\n\n**🗺️ Must-Know Commands:**\n```\ngit init          # Start a repo\ngit clone <url>   # Copy a repo\ngit add .         # Stage changes\ngit commit -m \"message\"  # Save snapshot\ngit push          # Upload to GitHub\ngit pull          # Download updates\ngit branch        # List branches\ngit checkout -b feature  # New branch\ngit merge feature  # Merge branch\ngit status        # Check state\ngit log --oneline  # View history\n```\n\n**📚 Resources:**\n• git-scm.com — Official docs\n• Learn Git Branching (learngitbranching.js.org) — interactive! ⭐\n• Fireship Git in 100 Seconds (YouTube)\n• The Coding Train Git & GitHub\n\n**🚀 Pro tip:** Make your GitHub profile look active — green squares matter for jobs!"
        ]
    },

    "ai": {
        "keywords": ["artificial intelligence", "ai", "learn ai", "ai basics", "ai roadmap"],
        "responses": [
            "🤖 **Artificial Intelligence — Building Intelligent Systems**\n\nAI is the most exciting field in tech right now. Here's how to get started!\n\n**🗺️ AI Learning Roadmap:**\n\n**Prerequisites:**\n• Python (intermediate level)\n• Mathematics: Linear Algebra, Calculus, Probability & Statistics\n\n**Core AI Concepts:**\n1. Search Algorithms (BFS, DFS, A*)\n2. Knowledge Representation\n3. Machine Learning fundamentals\n4. Neural Networks & Deep Learning\n5. NLP, Computer Vision\n6. Reinforcement Learning\n\n**📚 Resources:**\n• CS50 AI by Harvard — free & excellent ⭐\n• fast.ai — practical deep learning\n• 3Blue1Brown Neural Networks (YouTube) — beautiful explanations\n• Andrej Karpathy's videos (YouTube)\n• Stanford CS229 (free online)\n\n**💪 Practice:**\n• Kaggle competitions\n• Build projects: image classifier, chatbot, recommendation system\n\n**⏱️ Entry level:** 6-12 months"
        ]
    },

    "ml": {
        "keywords": ["machine learning", "ml", "learn ml", "supervised learning",
                     "classification", "regression", "clustering"],
        "responses": [
            "🧠 **Machine Learning — Teaching Machines to Learn**\n\nML is the engine powering modern AI — from Netflix recommendations to fraud detection!\n\n**🗺️ ML Roadmap:**\n\n**Math Prerequisites:**\n• Linear Algebra (matrices, vectors)\n• Statistics (distributions, hypothesis testing)\n• Calculus (derivatives, gradient descent)\n\n**Core ML:**\n1. Supervised Learning: Linear/Logistic Regression, Decision Trees, SVM, KNN\n2. Unsupervised Learning: K-Means, PCA, Hierarchical Clustering\n3. Ensemble Methods: Random Forest, Gradient Boosting, XGBoost\n4. Model Evaluation: Cross-validation, Precision/Recall, ROC-AUC\n5. Feature Engineering & Preprocessing\n\n**Libraries to Learn:**\n• NumPy → Pandas → Matplotlib → Scikit-learn\n• Then: TensorFlow or PyTorch\n\n**📚 Resources:**\n• Andrew Ng's ML Specialization (Coursera) ⭐ — the gold standard\n• fast.ai\n• StatQuest with Josh Starmer (YouTube)\n• Kaggle Learn (free!)\n\n**⏱️ Timeline:** 4-6 months to ML practitioner level"
        ]
    },

    "dl": {
        "keywords": ["deep learning", "dl", "neural network", "neural networks", "cnn",
                     "rnn", "lstm", "transformer", "pytorch", "tensorflow"],
        "responses": [
            "⚡ **Deep Learning — The Cutting Edge of AI**\n\nDeep Learning powers image recognition, language models, self-driving cars, and more!\n\n**🗺️ Deep Learning Roadmap:**\n\n**Prerequisites:**\n• Solid Python\n• Linear Algebra & Calculus\n• Basic Machine Learning\n\n**Core DL Concepts:**\n1. Neural Networks & Backpropagation\n2. CNNs — image recognition\n3. RNNs & LSTMs — sequence data\n4. Transformers & Attention Mechanism\n5. GANs — generative AI\n6. Transfer Learning\n7. Deployment (ONNX, TorchServe)\n\n**📚 Resources:**\n• Deep Learning Specialization — Andrew Ng (Coursera) ⭐\n• fast.ai — practical approach first\n• 3Blue1Brown Neural Networks series (YouTube) — must watch!\n• PyTorch official tutorials\n• Papers With Code (research + code)\n\n**💪 Project Ideas:**\n• Image Classifier, Style Transfer, Sentiment Analysis, Chatbot\n\n**⏱️ Timeline:** 6-12 months"
        ]
    },

    "thank_you": {
        "keywords": ["thank you", "thanks", "thank you so much", "thx", "ty", "cheers",
                     "appreciate it", "helpful"],
        "responses": [
            "You're welcome! 😊 That's what I'm here for. Keep up the great work and don't hesitate to ask anything else!",
            "Happy to help! 🌟 Remember, every question you ask is a step forward in your learning journey. Keep going!",
            "Anytime! 💙 You're doing great by actively seeking knowledge. That's the first quality of a great developer!",
            "It's my pleasure! 🚀 Now go apply what you've learned — that's where the real magic happens!"
        ]
    },

    "default": {
        "keywords": [],
        "responses": [
            "Hmm, I'm not quite sure I understand that! 🤔 I'm specialised in CS topics and student support.\n\nTry asking about: **Python, DSA, AI, Web Dev, Java, OOP, OS, DBMS, Git**, or type **help** to see everything I can do!",
            "I didn't catch that! 😅 I'm a rule-based bot, so I work best with specific keywords.\n\nTry: *Python roadmap*, *study tips*, *motivate me*, *tell me a joke*, or *fun fact*. Type **help** for the full menu!",
            "I'm still learning to understand that one! 🧠 I'm best at: CS topics, roadmaps, study advice, and motivation.\n\nType **help** to see all my capabilities!"
        ]
    }
}


def get_response(intent_name: str) -> str:
    """Return a random response string for the given intent name."""
    intent = INTENTS.get(intent_name, INTENTS["default"])
    return random.choice(intent["responses"])
