# AI Judge – Rock–Paper–Scissors-Bomb

## Overview

This project implements a **prompt-driven AI Judge** that evaluates free-text user inputs against a fixed set of game rules and produces **structured, explainable decisions**.

The focus is on:
- Prompt quality
- Instruction design
- Ambiguity handling
- Explainability

The system intentionally avoids hardcoding logic and instead delegates reasoning and judgment to the language model via a carefully designed prompt.

---

## Core Idea

The language model acts as the **decision-making authority**.

The code:
- Passes user input and game state
- Stores minimal state (round number, bomb usage)
- Displays the model’s structured decision

All interpretation, validation, and explanation are driven by prompt design.

---

## Game Rules

- Valid moves: `rock`, `paper`, `scissors`, `bomb`
- `bomb` can be used only once
- `bomb` beats all other moves
- `bomb` vs `bomb` results in a draw
- Invalid or unclear moves waste the turn

---

## Architectural Separation

The solution conceptually separates:

1. **Intent Understanding**  
   Mapping free-text input to possible moves and detecting ambiguity

2. **Game Logic**  
   Rule enforcement and outcome determination

3. **Response Generation**  
   Clear, structured explanations for the user

This separation is enforced through **prompt structure**, not code complexity.

---

## Failure Cases Considered

- Ambiguous phrasing (e.g. “something strong”)
- Metaphors (e.g. “drop a nuke”)
- Multiple moves in one input
- Bomb reuse attempts
- Hesitant language (“probably scissors”)
- Emoji-only inputs

The AI Judge never guesses intent.

---

## How to Run the Agent

### 1. Clone the repository
git clone <https://github.com/Jagmohan-Prajapati/AI-judge-rps-plus.git>
cd ai-judge-rps-plus

### 2. Install dependencies
pip install -r requirements.txt
or 
pip install -U google-genai    

### 3. Set your Gemini API key
Edit `judge.py` and replace:
genai.configure(api_key = "YOUR_GEMINI_API_KEY")

### 4. Run the Agent
python judge.py

### 5. Play via CLI
Type `exit` to stop.

## What would i improve next
- Confidence scoring for intent clarity
- Multi-round summary output
- Adversarial fuzz testing
- Extension to other rule-based judging tasks