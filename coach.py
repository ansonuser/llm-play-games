import openai
import os

class GameCoach:
    def __init__(self, attacker_history, protector_history, password, keyword):
        self.attacker_history = attacker_history
        self.protector_history = protector_history
        self.password = password
        self.keyword = keyword
    
    def analyze_game(self):
        # Format conversation history
        conversation = []
        for i in range(len(self.attacker_history)):
            conversation.append(f"Attacker: {self.attacker_history[i]}")
            if i < len(self.protector_history):
                conversation.append(f"Protector: {self.protector_history[i]}")
        
        full_conversation = "\n".join(conversation)
        
        # Generate analysis with GPT-4
        prompt = f"""
        As a game strategy coach, analyze this attacker-protector exchange:
        
        PROTECTOR KEYWORD: {self.keyword}
        ATTACKER PASSWORD: {self.password}
        
        CONVERSATION HISTORY:
        {full_conversation}
        
        Provide analysis and advice:
        1. Identify 3 effective attacker strategies
        2. Find 2 protector vulnerabilities
        3. Suggest 3 concrete question templates
        4. Rate attacker performance (1-5)
        5. Explain your reasoning step-by-step
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": prompt}
                ]
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            return "Coach analysis unavailable due to API error"