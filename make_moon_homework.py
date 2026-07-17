import webbrowser
import os

# Interactive Moon Homework structured beautifully as HTML
homework_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESL Homework: Mission to the Moon</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Nunito:wght@400;700;800;900&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <style>
        :root {
            --bg: #0b0f19;
            --panel: #111827;
            --panel-light: #1f2937;
            --primary: #c9a227;
            --primary-hover: #e5b934;
            --accent: #38bdf8;
            --text: #f3f4f6;
            --text-muted: #9ca3af;
            --correct: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --glow-green: rgba(16, 185, 129, 0.15);
            --glow-yellow: rgba(245, 158, 11, 0.15);
            --glow-red: rgba(239, 68, 68, 0.15);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Nunito', sans-serif;
            background: var(--bg);
            background-image: 
                radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
                radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
                radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 40px);
            background-size: 550px 550px, 350px 350px, 250px 250px;
            background-position: 0 0, 40px 60px, 130px 270px;
            color: var(--text);
            min-height: 100vh;
            padding: 24px 12px 48px;
            overflow-x: hidden;
        }

        header {
            width: min(1000px, 100%);
            margin: 0 auto 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
            border-bottom: 1px solid rgba(201, 162, 39, 0.15);
            padding-bottom: 14px;
        }

        .back-btn {
            border: 1.5px solid #2a4060;
            color: var(--primary);
            border-radius: 999px;
            padding: 8px 18px;
            font-weight: 900;
            background: var(--panel);
            text-decoration: none;
            font-size: 14px;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .back-btn:hover {
            background: rgba(201, 162, 39, 0.08);
            border-color: var(--primary);
            transform: translateY(-1px);
        }

        .antigravity-btn {
            background: linear-gradient(135deg, #4f46e5, #06b6d4);
            border: none;
            color: white;
            border-radius: 999px;
            padding: 8px 18px;
            font-weight: 900;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.4);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .antigravity-btn:hover {
            box-shadow: 0 6px 16px rgba(79, 70, 229, 0.6);
            transform: translateY(-2px);
        }

        .antigravity-btn.active {
            background: linear-gradient(135deg, #10b981, #06b6d4);
            box-shadow: 0 0 15px var(--correct);
            animation: pulse-glow 1.5s infinite;
        }

        @keyframes pulse-glow {
            0% { box-shadow: 0 0 5px rgba(16, 185, 129, 0.5); }
            50% { box-shadow: 0 0 18px rgba(16, 185, 129, 0.8); }
            100% { box-shadow: 0 0 5px rgba(16, 185, 129, 0.5); }
        }

        h1 {
            font-family: 'Fredoka One', cursive;
            font-size: 28px;
            color: var(--primary);
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .container {
            width: min(1000px, 100%);
            margin: 0 auto;
        }

        .hero-panel {
            background: linear-gradient(145deg, var(--panel), var(--panel-light));
            border: 1px solid rgba(201, 162, 39, 0.2);
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 12px 36px rgba(0,0,0,0.4);
            margin-bottom: 24px;
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: var(--accent);
            background: rgba(56, 189, 248, 0.1);
            border: 1px solid rgba(56, 189, 248, 0.2);
            border-radius: 999px;
            padding: 6px 12px;
            font-size: 11px;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 14px;
        }

        .hero-title-main {
            font-family: 'Fredoka One', cursive;
            font-size: clamp(24px, 4vw, 36px);
            color: var(--primary);
            margin-bottom: 12px;
        }

        .hero-desc {
            color: var(--text-muted);
            line-height: 1.6;
            font-size: 15px;
            margin-bottom: 16px;
        }

        .student-meta {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            background: rgba(0,0,0,0.2);
            padding: 16px;
            border-radius: 16px;
            border: 1px solid rgba(255,255,255,0.05);
        }

        .meta-field {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .meta-field label {
            font-size: 12px;
            font-weight: 800;
            text-transform: uppercase;
            color: var(--accent);
            letter-spacing: 0.05em;
        }

        .meta-field input {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            color: var(--text);
            padding: 8px 12px;
            border-radius: 8px;
            font-family: inherit;
            font-size: 14px;
            outline: none;
            transition: all 0.2s;
        }

        .meta-field input:focus {
            border-color: var(--primary);
            background: rgba(255,255,255,0.08);
        }

        .workspace-layout {
            display: grid;
            grid-template-columns: 1fr 1.2fr;
            gap: 24px;
            margin-bottom: 28px;
        }

        @media (max-width: 850px) {
            .workspace-layout {
                grid-template-columns: 1fr;
            }
        }

        .board-column {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .panel-heading {
            font-family: 'Fredoka One', cursive;
            font-size: 18px;
            color: var(--primary);
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .panel-sub {
            font-size: 13px;
            color: var(--text-muted);
            margin-bottom: 12px;
        }

        /* Items Salvage Bay */
        .salvage-bay {
            background: rgba(17, 24, 39, 0.6);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 20px;
            padding: 16px;
            min-height: 480px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            align-content: start;
        }

        @media (max-width: 480px) {
            .salvage-bay {
                grid-template-columns: 1fr;
            }
        }

        .item-card {
            background: var(--panel-light);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 12px;
            padding: 12px;
            cursor: pointer;
            user-select: none;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            font-size: 14px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .item-card:hover {
            border-color: var(--accent);
            transform: translateY(-2px);
            background: rgba(31, 41, 55, 0.9);
            box-shadow: 0 6px 12px rgba(56, 189, 248, 0.15);
        }

        .item-card.dragging {
            opacity: 0.4;
            transform: scale(0.95);
        }

        .item-icon {
            font-size: 18px;
            flex-shrink: 0;
        }

        /* The Board Slots */
        .board-zone {
            background: rgba(17, 24, 39, 0.6);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 20px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .tier-group {
            border-radius: 16px;
            padding: 14px;
            border: 1.5px solid transparent;
            transition: all 0.3s;
        }

        .tier-top {
            background: var(--glow-green);
            border-color: rgba(16, 185, 129, 0.2);
        }
        .tier-top .tier-title { color: var(--correct); }

        .tier-mid {
            background: var(--glow-yellow);
            border-color: rgba(245, 158, 11, 0.2);
        }
        .tier-mid .tier-title { color: var(--warning); }

        .tier-bottom {
            background: var(--glow-red);
            border-color: rgba(239, 68, 68, 0.2);
        }
        .tier-bottom .tier-title { color: var(--danger); }

        .tier-title {
            font-family: 'Fredoka One', cursive;
            font-size: 13px;
            letter-spacing: 0.05em;
            margin-bottom: 10px;
            text-transform: uppercase;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .tier-slots {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }

        @media (max-width: 550px) {
            .tier-slots {
                grid-template-columns: 1fr;
            }
        }

        .slot-container {
            background: rgba(0,0,0,0.3);
            border: 1px dashed rgba(255,255,255,0.15);
            border-radius: 10px;
            height: 44px;
            display: flex;
            align-items: center;
            padding: 0 10px;
            font-size: 13px;
            color: var(--text-muted);
            position: relative;
            transition: all 0.2s;
            cursor: pointer;
        }

        .slot-container.drag-over {
            border-color: var(--accent);
            background: rgba(56, 189, 248, 0.05);
        }

        .slot-num {
            font-weight: 800;
            margin-right: 8px;
            color: rgba(255,255,255,0.25);
            width: 20px;
            text-align: center;
        }

        .slot-desc {
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            width: 100%;
        }

        .slot-filled {
            position: absolute;
            top: 2px;
            left: 2px;
            right: 2px;
            bottom: 2px;
            background: var(--panel-light);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 8px;
            color: var(--text);
            font-weight: 700;
            cursor: grab;
            animation: pop-in 0.15s ease-out;
        }

        @keyframes pop-in {
            from { transform: scale(0.95); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }

        .slot-remove {
            color: var(--text-muted);
            border: none;
            background: transparent;
            cursor: pointer;
            font-size: 14px;
            padding: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            transition: all 0.15s;
        }

        .slot-remove:hover {
            color: var(--danger);
            background: rgba(239, 68, 68, 0.15);
        }

        /* Float Animation for Antigravity Mode */
        .antigravity-active .item-card:not(.dragging), 
        .antigravity-active .slot-filled {
            animation: drift 6s ease-in-out infinite;
        }

        .antigravity-active .item-card:nth-child(2n) { animation-delay: 1.5s; animation-duration: 5.5s; }
        .antigravity-active .item-card:nth-child(3n) { animation-delay: 0.7s; animation-duration: 7s; }
        .antigravity-active .slot-filled:nth-child(2n) { animation-delay: 2.2s; animation-duration: 6.5s; }

        @keyframes drift {
            0% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-6px) rotate(0.8deg); }
            100% { transform: translateY(0) rotate(0deg); }
        }

        /* Task 2: Strategy Justifications */
        .strategy-section {
            background: linear-gradient(145deg, var(--panel), var(--panel-light));
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            margin-bottom: 24px;
            display: grid;
            grid-template-columns: 1.3fr 0.7fr;
            gap: 24px;
        }

        @media (max-width: 800px) {
            .strategy-section {
                grid-template-columns: 1fr;
            }
        }

        .writing-area {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .prompt-card {
            background: rgba(0,0,0,0.2);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 16px;
            padding: 16px;
        }

        .prompt-card p {
            font-size: 14.5px;
            line-height: 1.6;
            margin-bottom: 10px;
            font-weight: 700;
        }

        .prompt-card p strong {
            color: var(--primary);
        }

        .prompt-card textarea {
            width: 100%;
            min-height: 80px;
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 10px;
            padding: 10px;
            color: var(--text);
            font-family: inherit;
            font-size: 14.5px;
            line-height: 1.5;
            resize: vertical;
            outline: none;
            transition: all 0.2s;
        }

        .prompt-card textarea:focus {
            border-color: var(--accent);
            background: rgba(255,255,255,0.06);
        }

        /* Grammar Helper Sidebar */
        .helper-sidebar {
            background: rgba(56, 189, 248, 0.03);
            border: 1px solid rgba(56, 189, 248, 0.1);
            border-radius: 18px;
            padding: 18px;
            align-self: start;
        }

        .sidebar-title {
            font-family: 'Fredoka One', cursive;
            font-size: 14px;
            text-transform: uppercase;
            color: var(--accent);
            margin-bottom: 12px;
            border-bottom: 1px dashed rgba(56, 189, 248, 0.2);
            padding-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .sidebar-section {
            margin-bottom: 14px;
        }

        .sidebar-section h5 {
            font-size: 12px;
            text-transform: uppercase;
            color: var(--primary);
            margin-bottom: 6px;
            font-weight: 800;
        }

        .sidebar-section ul {
            list-style: none;
            padding-left: 0;
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }

        .sidebar-section li {
            font-size: 11.5px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 6px;
            padding: 3px 8px;
            color: var(--text-muted);
            cursor: pointer;
            transition: all 0.15s;
        }

        .sidebar-section li:hover {
            color: var(--text);
            border-color: var(--accent);
            background: rgba(56, 189, 248, 0.08);
        }

        /* Action Buttons */
        .action-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 14px;
            margin-bottom: 24px;
        }

        .btn-group {
            display: flex;
            gap: 10px;
        }

        .action-btn {
            border: none;
            border-radius: 12px;
            padding: 12px 20px;
            font-family: inherit;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14px;
        }

        .action-btn:hover {
            transform: translateY(-2px);
        }

        .btn-primary-act {
            background: var(--primary);
            color: var(--bg);
        }

        .btn-primary-act:hover {
            background: var(--primary-hover);
        }

        .btn-secondary-act {
            background: rgba(255,255,255,0.04);
            color: var(--primary);
            border: 1.5px solid rgba(201, 162, 39, 0.3);
        }

        .btn-secondary-act:hover {
            background: rgba(201, 162, 39, 0.08);
            border-color: var(--primary);
        }

        .btn-accent {
            background: var(--accent);
            color: var(--bg);
        }

        .btn-accent:hover {
            background: #7dd3fc;
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
        }

        /* NASA evaluation results */
        .nasa-results-panel {
            background: linear-gradient(145deg, #1e1b4b, #111827);
            border: 1px solid rgba(56, 189, 248, 0.25);
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.5);
            margin-bottom: 24px;
            display: none;
            animation: slide-down 0.4s ease-out;
        }

        @keyframes slide-down {
            from { transform: translateY(-10px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        .score-headline {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
            border-bottom: 1.5px solid rgba(255,255,255,0.1);
            padding-bottom: 12px;
            flex-wrap: wrap;
            gap: 16px;
        }

        .score-box {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .score-circle {
            width: 64px;
            height: 64px;
            border-radius: 50%;
            background: var(--primary);
            color: var(--bg);
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Fredoka One', cursive;
            font-size: 26px;
            box-shadow: 0 0 15px rgba(201, 162, 39, 0.4);
        }

        .score-text h4 {
            font-family: 'Fredoka One', cursive;
            font-size: 20px;
            color: var(--primary);
        }

        .score-text p {
            font-size: 13px;
            color: var(--text-muted);
        }

        .rank-badge {
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            padding: 8px 16px;
            font-family: 'Fredoka One', cursive;
            font-size: 16px;
            color: var(--accent);
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }

        .score-analysis {
            font-size: 14px;
            line-height: 1.6;
            color: #d1d5db;
            background: rgba(0,0,0,0.2);
            padding: 16px;
            border-radius: 14px;
            margin-bottom: 20px;
            border-left: 4px solid var(--accent);
        }

        /* NASA vs Student Comparison Table */
        .comparison-table-wrapper {
            overflow-x: auto;
        }

        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 13.5px;
            text-align: left;
        }

        .comparison-table th {
            font-family: 'Fredoka One', cursive;
            color: var(--accent);
            border-bottom: 2px solid rgba(255,255,255,0.1);
            padding: 10px;
            font-size: 13px;
            text-transform: uppercase;
        }

        .comparison-table td {
            padding: 12px 10px;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            vertical-align: top;
            line-height: 1.5;
        }

        .comparison-table tr:hover {
            background: rgba(255,255,255,0.02);
        }

        .rank-num {
            display: inline-block;
            width: 24px;
            height: 24px;
            border-radius: 50%;
            text-align: center;
            line-height: 24px;
            font-weight: 800;
            font-size: 12px;
        }

        .rank-num.student {
            background: rgba(255,255,255,0.15);
            color: var(--text);
        }

        .rank-num.nasa {
            background: var(--primary);
            color: var(--bg);
            font-weight: 900;
        }

        .rank-diff {
            font-weight: 800;
        }
        .rank-diff.good { color: var(--correct); }
        .rank-diff.bad { color: var(--danger); }
    </style>
</head>
<body>

    <header>
        <h1>🚀 Mission to the Moon</h1>
        <div style="display: flex; gap: 10px; align-items: center;">
            <button class="antigravity-btn" id="antigravity-toggle" onclick="toggleAntigravity()">
                ✨ Float Mode: OFF
            </button>
            <a class="back-btn" href="./index.html">← Study Hub</a>
        </div>
    </header>

    <div class="container">
        
        <!-- Hero Scenario Section -->
        <section class="hero-panel">
            <span class="hero-badge">ESL Advanced Lesson 2 · Study Module</span>
            <h2 class="hero-title-main">🪐 The Scenario: Apollo 2026 Emergency</h2>
            <p class="hero-desc">
                Your lunar landing craft has just suffered a catastrophic technical malfunction. You were forced to land <strong>60 miles away</strong> from the main Moon Base. You are safe inside your pressure spacesuit, but you must hike across the lunar surface on foot to reach safety. Before your ship's airlocks seal forever, you manage to salvage 12 items.
            </p>
            <p class="hero-desc" style="color: var(--accent); font-weight: 700; margin-bottom: 20px;">
                🚨 <strong>The Rule:</strong> Because you are traveling on foot in lunar gravity, you need to decide what is worth carrying. You must rank all 12 items from most critical to totally useless.
            </p>

            <div class="student-meta">
                <div class="meta-field">
                    <label for="student-name">Student Name</label>
                    <input type="text" id="student-name" value="Paolo" placeholder="Enter name...">
                </div>
                <div class="meta-field">
                    <label for="due-date">Due Date</label>
                    <input type="text" id="due-date" value="Wednesday" placeholder="Enter due date...">
                </div>
            </div>
        </section>

        <!-- Task 1 Workspace -->
        <h3 class="panel-heading" style="margin-bottom: 4px;">📋 Task 1: The Lunar Ranking Board</h3>
        <p class="panel-sub" style="margin-bottom: 20px;">Drag items from the Salvage Bay to the Board, or click on items to automatically place them in order.</p>

        <section class="workspace-layout">
            <!-- Salvage Bay -->
            <div class="board-column">
                <h4 style="font-family: 'Fredoka One', cursive; font-size: 15px; color: var(--accent); text-transform: uppercase;">🧳 Lunar Salvage Bay</h4>
                <div class="salvage-bay" id="salvage-bay">
                    <!-- Items will be generated here -->
                </div>
            </div>

            <!-- Ranking Board -->
            <div class="board-column">
                <h4 style="font-family: 'Fredoka One', cursive; font-size: 15px; color: var(--primary); text-transform: uppercase;">🛸 The Lunar Ranking Board</h4>
                <div class="board-zone" id="ranking-board">
                    
                    <!-- TOP TIER -->
                    <div class="tier-group tier-top">
                        <div class="tier-title">🟢 Top Tier: Essential for Survival</div>
                        <div class="tier-slots">
                            <div class="slot-container" data-rank="1"><span class="slot-num">#1</span><span class="slot-desc">Drop here (Absolute Priority)</span></div>
                            <div class="slot-container" data-rank="2"><span class="slot-num">#2</span><span class="slot-desc">Drop here</span></div>
                            <div class="slot-container" data-rank="3"><span class="slot-num">#3</span><span class="slot-desc">Drop here</span></div>
                            <div class="slot-container" data-rank="4"><span class="slot-num">#4</span><span class="slot-desc">Drop here</span></div>
                        </div>
                    </div>

                    <!-- MID TIER -->
                    <div class="tier-group tier-mid">
                        <div class="tier-title">🟡 Mid Tier: Helpful, but Not Critical</div>
                        <div class="tier-slots">
                            <div class="slot-container" data-rank="5"><span class="slot-num">#5</span><span class="slot-desc">Drop here</span></div>
                            <div class="slot-container" data-rank="6"><span class="slot-num">#6</span><span class="slot-desc">Drop here</span></div>
                            <div class="slot-container" data-rank="7"><span class="slot-num">#7</span><span class="slot-desc">Drop here</span></div>
                            <div class="slot-container" data-rank="8"><span class="slot-num">#8</span><span class="slot-desc">Drop here</span></div>
                        </div>
                    </div>

                    <!-- BOTTOM TIER -->
                    <div class="tier-group tier-bottom">
                        <div class="tier-title">🔴 Bottom Tier: A Total Waste of Weight</div>
                        <div class="tier-slots">
                            <div class="slot-container" data-rank="9"><span class="slot-num">#9</span><span class="slot-desc">Drop here</span></div>
                            <div class="slot-container" data-rank="10"><span class="slot-num">#10</span><span class="slot-desc">Drop here</span></div>
                            <div class="slot-container" data-rank="11"><span class="slot-num">#11</span><span class="slot-desc">Drop here</span></div>
                            <div class="slot-container" data-rank="12"><span class="slot-num">#12</span><span class="slot-desc">Drop here (Useless)</span></div>
                        </div>
                    </div>

                </div>
            </div>
        </section>

        <!-- Task 2 Strategy Writing -->
        <h3 class="panel-heading" style="margin-bottom: 4px;">✍️ Task 2: Justify Your Strategy</h3>
        <p class="panel-sub" style="margin-bottom: 20px;">Practice your English grammar by writing 2–4 full sentences for each question.</p>

        <section class="strategy-section">
            <div class="writing-area">
                <div class="prompt-card">
                    <p><strong>1.</strong> Why did you choose your <strong>#1 item</strong>? Why is it the most critical thing to have on the Moon?</p>
                    <textarea id="justification-1" placeholder="Write 2-4 sentences explaining your #1 choice..."></textarea>
                </div>
                <div class="prompt-card">
                    <p><strong>2.</strong> Look at your <strong>#12 item</strong>. Explain why this item is completely useless in space.</p>
                    <textarea id="justification-2" placeholder="Write 2-4 sentences explaining your #12 choice..."></textarea>
                </div>
                <div class="prompt-card">
                    <p><strong>3.</strong> Compare two items: Why is item <strong>#4</strong> more useful to you than item <strong>#8</strong>?</p>
                    <textarea id="justification-3" placeholder="Compare items #4 and #8 using comparative structures..."></textarea>
                </div>
            </div>

            <!-- Grammar and Vocab Sidebar -->
            <div class="helper-sidebar">
                <div class="sidebar-title">💡 Vocabulary Helper</div>
                
                <div class="sidebar-section">
                    <h5>🌌 Space Terminology</h5>
                    <ul>
                        <li onclick="insertWord('vacuum')">vacuum</li>
                        <li onclick="insertWord('atmosphere')">atmosphere</li>
                        <li onclick="insertWord('combustion')">combustion</li>
                        <li onclick="insertWord('gravity')">gravity</li>
                        <li onclick="insertWord('navigation')">navigation</li>
                        <li onclick="insertWord('dehydration')">dehydration</li>
                        <li onclick="insertWord('propulsion')">propulsion</li>
                        <li onclick="insertWord('solar-powered')">solar-powered</li>
                    </ul>
                </div>

                <div class="sidebar-section">
                    <h5>🛡️ Utility Adjectives</h5>
                    <ul>
                        <li onclick="insertWord('crucial')">crucial</li>
                        <li onclick="insertWord('vital')">vital</li>
                        <li onclick="insertWord('useless')">useless</li>
                        <li onclick="insertWord('essential')">essential</li>
                        <li onclick="insertWord('ineffective')">ineffective</li>
                        <li onclick="insertWord('redundant')">redundant</li>
                        <li onclick="insertWord('combustible')">combustible</li>
                    </ul>
                </div>

                <div class="sidebar-section">
                    <h5>🔗 Connectors & Comparatives</h5>
                    <ul>
                        <li onclick="insertWord('consequently')">consequently</li>
                        <li onclick="insertWord('since')">since</li>
                        <li onclick="insertWord('whereas')">whereas</li>
                        <li onclick="insertWord('in contrast to')">in contrast to</li>
                        <li onclick="insertWord('on the other hand')">on the other hand</li>
                        <li onclick="insertWord('is more vital than')">is more vital than</li>
                    </ul>
                </div>

                <p style="font-size: 11px; color: var(--text-muted); line-height: 1.4; border-top: 1px dashed rgba(255,255,255,0.08); padding-top: 8px;">
                    💡 <em>Click any word to insert it at your cursor's last position!</em>
                </p>
            </div>
        </section>

        <!-- NASA Evaluation Results (Hidden by default) -->
        <section class="nasa-results-panel" id="nasa-results">
            <div class="score-headline">
                <div class="score-box">
                    <div class="score-circle" id="score-circle">52</div>
                    <div class="score-text">
                        <h4 id="score-status">Calculating...</h4>
                        <p>Total difference from NASA ranks (lower is better)</p>
                    </div>
                </div>
                <div class="rank-badge" id="rank-badge">Lunar Pioneer</div>
            </div>

            <div class="score-analysis" id="score-analysis">
                <!-- Custom evaluation text -->
            </div>

            <div class="panel-heading" style="color: var(--accent); margin-bottom: 12px; font-size: 16px;">
                🔍 Detailed Breakdown: Your Ranks vs. NASA Experts
            </div>
            
            <div class="comparison-table-wrapper">
                <table class="comparison-table">
                    <thead>
                        <tr>
                            <th>Item</th>
                            <th style="width: 80px; text-align: center;">Your Rank</th>
                            <th style="width: 80px; text-align: center;">NASA Rank</th>
                            <th style="width: 80px; text-align: center;">Diff</th>
                            <th>NASA Reasoning</th>
                        </tr>
                    </thead>
                    <tbody id="comparison-table-body">
                        <!-- Filled by JS -->
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Action Bar -->
        <div class="action-bar">
            <div class="btn-group">
                <button class="action-btn btn-primary-act" onclick="downloadPDF()">
                    💾 Download PDF for Preply
                </button>
                <button class="action-btn btn-secondary-act" onclick="resetHomework()">
                    🔄 Clear All
                </button>
            </div>
            <button class="action-btn btn-accent" id="compare-btn" onclick="toggleNasaComparison()">
                👁️ Compare with NASA Experts
            </button>
        </div>

    </div>

    <script>
        // Item database
        const items = [
            { id: "oxygen", name: "Two 100lb tanks of oxygen", icon: "💨", nasaRank: 1, reason: "The absolute first survival requirement. There is no air on the Moon." },
            { id: "water", name: "5 gallons of water", icon: "💧", nasaRank: 2, reason: "Vital for hydration to replace high liquid loss in the lunar environment." },
            { id: "map", name: "Stellar map", icon: "🌌", nasaRank: 3, reason: "Essential for navigation. The stars will guide you across the featureless Moon." },
            { id: "food", name: "15 packs of space food", icon: "🥩", nasaRank: 4, reason: "Efficient supply of energy requirements for the 60-mile trek." },
            { id: "radio", name: "Solar-powered radio", icon: "📻", nasaRank: 5, reason: "Crucial for FM line-of-sight communication with the main base." },
            { id: "rope", name: "50 feet of nylon rope", icon: "🪢", nasaRank: 6, reason: "Useful for scaling craters, crossing rough terrains, or tying crewmates together." },
            { id: "firstaid", name: "First-aid kit", icon: "🩹", nasaRank: 7, reason: "Essential for injuries, featuring injection needles that fit spacesuit ports." },
            { id: "silk", name: "Parachute silk", icon: "🪂", nasaRank: 8, reason: "Provides shelter and shields you from the direct, intense rays of the sun." },
            { id: "raft", name: "Self-inflating life raft", icon: "🛶", nasaRank: 9, reason: "The CO2 cylinder inside can be released for emergency jet propulsion." },
            { id: "heater", name: "Portable heating unit", icon: "🔥", nasaRank: 10, reason: "Only useful if you land on the dark side of the Moon. Otherwise redundant." },
            { id: "compass", name: "Magnetic compass", icon: "🧭", nasaRank: 11, reason: "Totally useless. The Moon does not have a polarized magnetic field." },
            { id: "matches", name: "Box of matches", icon: "🔥", nasaRank: 12, reason: "Completely worthless. There is no oxygen on the Moon to support combustion." }
        ];

        // Track state
        let boardState = Array(12).fill(null); // stores item IDs at index = rank-1
        let activeTextarea = null;

        // Initialize Bay
        function initSalvageBay() {
            const bay = document.getElementById("salvage-bay");
            bay.innerHTML = "";
            
            // Render items that are NOT currently on the board
            items.forEach(item => {
                const isOnBoard = boardState.includes(item.id);
                if (!isOnBoard) {
                    const card = document.createElement("div");
                    card.className = "item-card";
                    card.draggable = true;
                    card.id = `item-${item.id}`;
                    card.setAttribute("data-item-id", item.id);
                    card.innerHTML = `<span class="item-icon">${item.icon}</span> ${item.name}`;
                    
                    // Setup Drag and Drop Event Listeners
                    card.addEventListener("dragstart", dragStart);
                    card.addEventListener("dragend", dragEnd);
                    
                    // Click to auto-place
                    card.addEventListener("click", () => autoPlaceItem(item.id));
                    
                    bay.appendChild(card);
                }
            });
        }

        // Drag and Drop Logic
        let draggedItem = null;

        function dragStart(e) {
            draggedItem = this;
            this.classList.add("dragging");
            e.dataTransfer.setData("text/plain", this.getAttribute("data-item-id"));
        }

        function dragEnd() {
            this.classList.remove("dragging");
            draggedItem = null;
        }

        // Setup Board Slots Event Listeners
        const slots = document.querySelectorAll(".slot-container");
        slots.forEach(slot => {
            slot.addEventListener("dragover", dragOver);
            slot.addEventListener("dragenter", dragEnter);
            slot.addEventListener("dragleave", dragLeave);
            slot.addEventListener("drop", drop);
            slot.addEventListener("click", slotClick);
        });

        function dragOver(e) {
            e.preventDefault();
        }

        function dragEnter(e) {
            e.preventDefault();
            this.classList.add("drag-over");
        }

        function dragLeave() {
            this.classList.remove("drag-over");
        }

        function drop(e) {
            this.classList.remove("drag-over");
            const itemId = e.dataTransfer.getData("text/plain");
            const rank = parseInt(this.getAttribute("data-rank"));
            placeItemInSlot(itemId, rank);
        }

        function slotClick() {
            const rank = parseInt(this.getAttribute("data-rank"));
            const itemId = boardState[rank - 1];
            if (itemId) {
                removeItemFromSlot(rank);
            }
        }

        // Action: Place item
        function placeItemInSlot(itemId, rank) {
            const index = rank - 1;
            const currentItemAtSlot = boardState[index];
            
            // Check if the item is already somewhere else on the board
            const existingRankIndex = boardState.indexOf(itemId);
            if (existingRankIndex !== -1) {
                // Remove from that slot first
                boardState[existingRankIndex] = null;
                updateSlotUI(existingRankIndex + 1);
            }

            // If slot is occupied, send occupied item back to bay
            if (currentItemAtSlot) {
                boardState[index] = null;
            }

            // Put new item in slot
            boardState[index] = itemId;
            updateSlotUI(rank);
            initSalvageBay();
            
            // Recalculate score if comparison panel is visible
            if (document.getElementById("nasa-results").style.display === "block") {
                calculateNasaScore();
            }
        }

        // Action: Remove item from slot
        function removeItemFromSlot(rank) {
            const index = rank - 1;
            boardState[index] = null;
            updateSlotUI(rank);
            initSalvageBay();
            
            // Recalculate score if comparison panel is visible
            if (document.getElementById("nasa-results").style.display === "block") {
                calculateNasaScore();
            }
        }

        // Auto-place in first free slot
        function autoPlaceItem(itemId) {
            const freeSlotIndex = boardState.indexOf(null);
            if (freeSlotIndex !== -1) {
                placeItemInSlot(itemId, freeSlotIndex + 1);
            } else {
                alert("The board is full! Remove an item before adding a new one.");
            }
        }

        // Update UI of a specific slot
        function updateSlotUI(rank) {
            const index = rank - 1;
            const itemId = boardState[index];
            const slot = document.querySelector(`.slot-container[data-rank="${rank}"]`);
            const descSpan = slot.querySelector(".slot-desc");
            
            // Clear existing filled container if any
            const existingFilled = slot.querySelector(".slot-filled");
            if (existingFilled) {
                existingFilled.remove();
            }

            if (itemId) {
                const item = items.find(i => i.id === itemId);
                descSpan.style.opacity = "0"; // hide placeholder
                
                const filledDiv = document.createElement("div");
                filledDiv.className = "slot-filled";
                filledDiv.innerHTML = `
                    <span>${item.icon} ${item.name}</span>
                    <button class="slot-remove" onclick="event.stopPropagation(); removeItemFromSlot(${rank})">×</button>
                `;
                slot.appendChild(filledDiv);
            } else {
                descSpan.style.opacity = "1"; // show placeholder
            }
        }

        // Textarea cursor focus tracker
        const textareas = [
            document.getElementById("justification-1"),
            document.getElementById("justification-2"),
            document.getElementById("justification-3")
        ];

        textareas.forEach(ta => {
            ta.addEventListener("focus", () => {
                activeTextarea = ta;
            });
        });

        // Insert vocab from sidebar
        function insertWord(word) {
            if (!activeTextarea) {
                // If no active text area, default to the first one
                activeTextarea = textareas[0];
                activeTextarea.focus();
            }
            const txt = activeTextarea.value;
            const start = activeTextarea.selectionStart;
            const end = activeTextarea.selectionEnd;
            activeTextarea.value = txt.substring(0, start) + word + txt.substring(end);
            activeTextarea.selectionStart = activeTextarea.selectionEnd = start + word.length;
            activeTextarea.focus();
        }

        // Easter Egg: Antigravity Floating Mode Toggle
        let antigravityMode = false;
        function toggleAntigravity() {
            antigravityMode = !antigravityMode;
            const btn = document.getElementById("antigravity-toggle");
            if (antigravityMode) {
                document.body.classList.add("antigravity-active");
                btn.classList.add("active");
                btn.innerHTML = "✨ Float Mode: ON";
            } else {
                document.body.classList.remove("antigravity-active");
                btn.classList.remove("active");
                btn.innerHTML = "✨ Float Mode: OFF";
            }
        }

        // Clear All answers & rankings
        function resetHomework() {
            if (confirm("Are you sure you want to clear your current progress?")) {
                boardState = Array(12).fill(null);
                for (let r = 1; r <= 12; r++) {
                    updateSlotUI(r);
                }
                initSalvageBay();
                textareas.forEach(ta => ta.value = "");
                document.getElementById("nasa-results").style.display = "none";
                document.getElementById("compare-btn").innerText = "👁️ Compare with NASA Experts";
            }
        }

        // NASA comparison logic
        function toggleNasaComparison() {
            const resultsPanel = document.getElementById("nasa-results");
            const compareBtn = document.getElementById("compare-btn");
            
            if (resultsPanel.style.display === "block") {
                resultsPanel.style.display = "none";
                compareBtn.innerText = "👁️ Compare with NASA Experts";
            } else {
                // Ensure all items are placed
                const unplacedCount = boardState.filter(s => s === null).length;
                if (unplacedCount > 0) {
                    alert(`You must place all 12 items on the board before comparing with NASA. (${unplacedCount} item(s) remaining)`);
                    return;
                }
                
                calculateNasaScore();
                resultsPanel.style.display = "block";
                compareBtn.innerText = "🙈 Hide NASA Comparison";
                // Smooth scroll to results
                resultsPanel.scrollIntoView({ behavior: 'smooth' });
            }
        }

        function calculateNasaScore() {
            let totalDiff = 0;
            const tbody = document.getElementById("comparison-table-body");
            tbody.innerHTML = "";

            // Loop through slots
            for (let index = 0; index < 12; index++) {
                const itemId = boardState[index];
                const item = items.find(i => i.id === itemId);
                const studentRank = index + 1;
                const nasaRank = item.nasaRank;
                const diff = Math.abs(studentRank - nasaRank);
                totalDiff += diff;

                const tr = document.createElement("tr");
                let diffClass = "";
                if (diff === 0) diffClass = "good";
                else if (diff > 5) diffClass = "bad";

                tr.innerHTML = `
                    <td><strong>${item.icon} ${item.name}</strong></td>
                    <td style="text-align: center;"><span class="rank-num student">${studentRank}</span></td>
                    <td style="text-align: center;"><span class="rank-num nasa">${nasaRank}</span></td>
                    <td style="text-align: center; font-weight: 800;" class="${diffClass}">${diff === 0 ? "✓" : (studentRank > nasaRank ? "+" : "-") + diff}</td>
                    <td style="color: var(--text-muted); font-size: 13px;">${item.reason}</td>
                `;
                tbody.appendChild(tr);
            }

            // Update Score Display
            document.getElementById("score-circle").innerText = totalDiff;
            
            // Assign rank title and custom feedback paragraph
            let status = "";
            let badge = "";
            let analysis = "";

            if (totalDiff <= 16) {
                status = "Excellent Survival Strategy! 🌟";
                badge = "Space Commander (Elite)";
                analysis = `Outstanding! Your ranking aligns very closely with NASA's survival calculations. You demonstrated a deep understanding of lunar physics (recognizing matches and compasses are useless, while oxygen and water are absolute priorities). You are fully prepared to lead a trek across the Moon.`;
            } else if (totalDiff <= 32) {
                status = "Great Job! You Survived. 🧑‍🚀";
                badge = "Lunar Officer (Pioneer)";
                analysis = `Very good effort! You made strong, logical choices. Your rankings are quite close to NASA's. You prioritized the critical physiological survival elements (oxygen and water) and did not rely heavily on useless tools. A couple of items could be optimized, but you would make it to base safely.`;
            } else if (totalDiff <= 48) {
                status = "Risky Journey Ahead! 🛰️";
                badge = "Space Cadet";
                analysis = `You survived the journey, but it was highly dangerous. You placed some useless or less critical items in your high tiers, which means you would be carrying extra weight at the expense of vital life-support materials. Review NASA's reasons below to see how to optimize your packing.`;
            } else {
                status = "Lost in Orbit! ☄️";
                badge = "Space Cadet";
                analysis = `Oh no! You would likely run out of oxygen or become lost on your hike. You ranked items like the matchbox or magnetic compass too high, which are completely useless on the Moon due to the lack of air and magnetic field. Study NASA's explanations below to prepare for your next flight!`;
            }

            document.getElementById("score-status").innerText = status;
            document.getElementById("rank-badge").innerText = badge;
            document.getElementById("score-analysis").innerHTML = analysis;
        }

        // Generate PDF
        function downloadPDF() {
            // Check if name is filled
            const studentName = document.getElementById("student-name").value.trim() || "Paolo";
            const dueDate = document.getElementById("due-date").value.trim() || "Wednesday";

            const unplacedCount = boardState.filter(s => s === null).length;
            if (unplacedCount > 0) {
                alert(`Please place all 12 items on the board before downloading the PDF. (${unplacedCount} item(s) remaining)`);
                return;
            }

            // Calculate NASA score first to ensure comparison values are populated
            calculateNasaScore();
            const totalDiff = document.getElementById("score-circle").innerText;
            const badge = document.getElementById("rank-badge").innerText;

            const { jsPDF } = window.jspdf;
            const doc = new jsPDF({unit:'pt', format:'a4'});
            const margin = 50;
            const maxWidth = 595 - margin * 2;
            let y = margin;

            // Page 1: Header & Ranking Board
            doc.setFillColor(11, 15, 25);
            doc.rect(0, 0, 595, 842, "F");

            doc.setTextColor(201, 162, 39);
            doc.setFont('helvetica','bold');
            doc.setFontSize(22);
            doc.text("ESL HOMEWORK: MISSION TO THE MOON", margin, y); y += 30;

            doc.setTextColor(243, 244, 246);
            doc.setFontSize(11);
            doc.setFont('helvetica', 'normal');
            doc.text(`Student Name: ${studentName}`, margin, y);
            doc.text(`Due Date: ${dueDate}`, 350, y); y += 30;

            doc.setFillColor(17, 24, 39);
            doc.rect(margin - 10, y - 12, maxWidth + 20, 65, "F");
            doc.setDrawColor(201, 162, 39);
            doc.setLineWidth(1);
            doc.rect(margin - 10, y - 12, maxWidth + 20, 65, "D");

            doc.setTextColor(201, 162, 39);
            doc.setFont('helvetica','bold');
            doc.text("Apollo 2026 Emergency Scenario:", margin, y); y += 16;
            doc.setTextColor(209, 213, 219);
            doc.setFont('helvetica','normal');
            const scenarioIntro = doc.splitTextToSize("Your ship landed 60 miles from Moon Base. You must hike across the lunar surface and rank your 12 salvaged items from most critical to totally useless.", maxWidth);
            doc.text(scenarioIntro, margin, y); y += 45;

            // Ranks Table
            doc.setTextColor(201, 162, 39);
            doc.setFont('helvetica','bold');
            doc.setFontSize(14);
            doc.text("Task 1: Your Lunar Ranking Board", margin, y); y += 20;

            // Draw table columns
            doc.setFillColor(31, 41, 55);
            doc.rect(margin, y - 12, maxWidth, 20, "F");
            doc.setTextColor(56, 189, 248);
            doc.setFontSize(10);
            doc.text("RANK", margin + 10, y + 2);
            doc.text("ITEM NAME", margin + 70, y + 2);
            doc.text("NASA RANK", margin + 350, y + 2);
            doc.text("DIFF", margin + 440, y + 2);
            y += 20;

            doc.setTextColor(243, 244, 246);
            doc.setFontSize(10);
            for (let i = 0; i < 12; i++) {
                const itemId = boardState[i];
                const item = items.find(it => it.id === itemId);
                const sRank = i + 1;
                const nRank = item.nasaRank;
                const diff = Math.abs(sRank - nRank);

                // Alternating row background
                if (i % 2 === 0) {
                    doc.setFillColor(21, 27, 38);
                    doc.rect(margin, y - 10, maxWidth, 18, "F");
                }
                
                doc.setFont('helvetica','bold');
                doc.text(`#${sRank}`, margin + 10, y + 3);
                doc.setFont('helvetica','normal');
                doc.text(item.name, margin + 70, y + 3);
                doc.text(`#${nRank}`, margin + 360, y + 3);
                doc.text(diff === 0 ? "✓" : `${sRank > nRank ? "+" : "-"}${diff}`, margin + 445, y + 3);
                y += 18;
            }

            y += 20;
            // NASA Score
            doc.setFillColor(30, 27, 75);
            doc.rect(margin, y - 12, maxWidth, 40, "F");
            doc.setDrawColor(56, 189, 248);
            doc.rect(margin, y - 12, maxWidth, 40, "D");
            doc.setTextColor(201, 162, 39);
            doc.setFont('helvetica','bold');
            doc.text(`NASA Comparison Score: ${totalDiff}`, margin + 15, y + 13);
            doc.setTextColor(56, 189, 248);
            doc.text(`Rank: ${badge}`, margin + 280, y + 13);
            y += 60;

            // Page 2: Strategy Justifications
            doc.addPage();
            y = margin;

            doc.setFillColor(11, 15, 25);
            doc.rect(0, 0, 595, 842, "F");

            doc.setTextColor(201, 162, 39);
            doc.setFont('helvetica','bold');
            doc.setFontSize(16);
            doc.text("Task 2: Strategy Justifications", margin, y); y += 30;

            // Question 1
            doc.setTextColor(243, 244, 246);
            doc.setFontSize(11);
            doc.text("Q1. Why did you choose your #1 item? Why is it the most critical thing to have on the Moon?", margin, y); y += 16;
            
            doc.setFillColor(17, 24, 39);
            doc.rect(margin, y - 8, maxWidth, 80, "F");
            doc.setTextColor(209, 213, 219);
            const ans1Text = document.getElementById("justification-1").value || "(no answer written)";
            const ans1 = doc.splitTextToSize(ans1Text, maxWidth - 20);
            doc.text(ans1, margin + 10, y + 12);
            y += 100;

            // Question 2
            doc.setTextColor(243, 244, 246);
            doc.text("Q2. Look at your #12 item. Explain why this item is completely useless in space.", margin, y); y += 16;
            
            doc.setFillColor(17, 24, 39);
            doc.rect(margin, y - 8, maxWidth, 80, "F");
            doc.setTextColor(209, 213, 219);
            const ans2Text = document.getElementById("justification-2").value || "(no answer written)";
            const ans2 = doc.splitTextToSize(ans2Text, maxWidth - 20);
            doc.text(ans2, margin + 10, y + 12);
            y += 100;

            // Question 3
            doc.setTextColor(243, 244, 246);
            doc.text("Q3. Compare two items: Why is item #4 more useful to you than item #8?", margin, y); y += 16;
            
            doc.setFillColor(17, 24, 39);
            doc.rect(margin, y - 8, maxWidth, 80, "F");
            doc.setTextColor(209, 213, 219);
            const ans3Text = document.getElementById("justification-3").value || "(no answer written)";
            const ans3 = doc.splitTextToSize(ans3Text, maxWidth - 20);
            doc.text(ans3, margin + 10, y + 12);
            y += 110;

            // Footer / Sign off
            doc.setTextColor(156, 163, 175);
            doc.setFontSize(9);
            doc.text("Completed via Preply Conversation Lab • NASA Lunar Survival ESL Module", margin, y);

            doc.save(`paolo-moon-survival-homework-${new Date().toISOString().slice(0,10)}.pdf`);
        }

        // Initialize on load
        window.addEventListener("DOMContentLoaded", () => {
            initSalvageBay();
        });
    </script>
</body>
</html>
"""

# Write the HTML layout to a local file
file_name = "moon_survival_homework.html"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(homework_html)

# Tell the code to open the browser (simulating the antigravity style jump!)
print("Flying over to your browser to deliver the homework...")
webbrowser.open('file://' + os.path.realpath(file_name))
