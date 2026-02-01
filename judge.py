import random
from google import genai


# Configuration
client = genai.Client(api_key="AIzaSyD-Dcu3xulvLr7aFP5lrI7L1w3XgDnJBhQ")

MODEL_NAME = "models/gemini-2.0-flash"

VALID_BOT_MOVES = ["rock", "paper", "scissors", "bomb"]


# Load system prompt
with open("prompts/system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()


# Game state
state = {
    "round": 1,
    "user_bomb_used": False
}



# Judge function
def judge_move(user_input: str):
    bot_move = random.choice(VALID_BOT_MOVES)

    prompt = f"""
{SYSTEM_PROMPT}

Context:
Round number: {state['round']}
User bomb already used: {state['user_bomb_used']}

Bot move for this round: {bot_move}

User input:
"{user_input}"
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    output = response.text

    # Minimal state update (NO game logic here)
    if "User Move (interpreted): bomb" in output and "VALID" in output:
        state["user_bomb_used"] = True

    state["round"] += 1
    return output


# CLI Loop
if __name__ == "__main__":
    print("AI Judge: Rock–Paper–Scissors Plus")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter your move: ")

        if user_input.lower() == "exit":
            print("Game ended.")
            break

        result = judge_move(user_input)
        print("\n" + result + "\n" + "-" * 50 + "\n")
