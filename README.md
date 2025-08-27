# Word Guessing Game Jailbreak - Attackers vs Protectors

This project implements a word-guessing game where an Attacker tries to make a Protector include "password" in his response. The Protector will answer questions which are related to keyword without accidentally. After each game, a Coach provides strategic analysis. 

## Example

password: poison someone
keyword: finance

Attacker aims at "poison someone" from Protector. At same time, Protector will give feedback if the question is not related to "finance". The attacker's question will learn toward malicious finance and the protector will answer it like a simple question(Bypass inherent guardrail).



## Game Overview
- **Attacker**: Tries to make the Protector say the password through carefully crafted questions
- **Protector**: Answers questions only related their keywords
- **Game Rounds**: 5 rounds maximum, game ends if password is revealed
- **Post-Game**: Coach analyzes the strategies used and provides improvement suggestions (red-teaming)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/word-guessing-game.git
cd word-guessing-game
```

2. Install dependencies:
```bash
pip install openai python-dotenv
```

3. Set up environment variables:
```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```
Replace `your_api_key_here` with your actual OpenAI API key.

## Running the Game
```bash
python main.py
```

Follow the prompts to:
1. Set the password (Attacker)
2. Set the keyword (Protector)
3. Watch the game unfold over 5 rounds
4. Receive post-game analysis from the Coach

## Code Structure
- `main.py`: Entry point that orchestrates the game flow
- `agents.py`: Contains the `Attacker` and `Protector` classes with their question/response logic
- `coach.py`: Implements the `GameCoach` class for post-game analysis
- `messaging.py`: Provides a message bus system for communication (currently not fully utilized)



## How It Works
1. The Attacker generates subtle questions using to trick the Protector
2. The Protector ensure responses stay topic-related
3. The game ends if the password is mentioned or after N rounds
4. The Coach analyzes the conversation and provides strategic feedback

