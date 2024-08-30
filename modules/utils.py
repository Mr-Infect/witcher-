import random

def get_user_agents():
    return [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
        # Add more user agents
    ]

def rotate_user_agent(user_agents):
    return random.choice(user_agents)
