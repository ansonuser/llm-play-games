from agents import Attacker, Protector
from coach import GameCoach
import os

def main():
    print("Word Guessing Game - Attackers vs Protectors")
    password = input("Attacker, set your password: ").strip()
    keyword = input("Protector, set your keyword: ").strip()
    
    attacker = Attacker(password)
    protector = Protector(keyword)
    attacker_history = []
    protector_history = []
    
    for round in range(1, 6):
        print(f"\n--- ROUND {round} ---")
        question = attacker.generate_response()
        attacker_history.append(question)
        print(f"Attacker asks: {question}")
        
        response = protector.generate_response(question)
        protector_history.append(response)
        print(f"Protector responds: {response}")
        
        if password.lower() in response.lower():
            print(f"\nGame over! Protector revealed the password in round {round}")
            break
    else:
        print("\nGame ended after 5 rounds. Protector wins!")
    
    # Post-game coach analysis
    coach = GameCoach(attacker_history, protector_history, password, keyword)
    analysis = coach.analyze_game()
    print("\n--- COACH ANALYSIS ---")
    print(analysis)

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set")
    else:
        main()