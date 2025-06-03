# Cryptocurrency Advisor Chatbot
# Name: CryptoBuddy
# Theme: AI-Powered Financial Sidekick

# Sample Cryptocurrency Database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    },
    "Solana": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7/10
    }
}

# Chatbot Introduction
def chatbot_intro():
    print("\n🌟 Welcome to CryptoBuddy! 🌟")
    print("Your AI-powered financial sidekick for smart crypto investments.")
    print("I analyze coins based on profitability (price trends) and sustainability (eco-friendliness).")
    print("Type 'help' for guidance or 'exit' to quit.\n")

# Help Menu
def show_help():
    print("\n💡 How to use CryptoBuddy:")
    print("- Ask me things like:")
    print("  * 'Which crypto is trending up?'")
    print("  * 'What’s the most sustainable coin?'")
    print("  * 'Recommend a profitable and green crypto.'")
    print("- You can also type 'list' to see all supported cryptos.\n")

# List All Cryptocurrencies
def list_cryptos():
    print("\n📊 Available Cryptocurrencies:")
    for crypto in crypto_db:
        print(f"- {crypto} (Trend: {crypto_db[crypto]['price_trend']}, Sustainability: {crypto_db[crypto]['sustainability_score']}/10)")
    print()

# Chatbot Logic
def crypto_advisor():
    chatbot_intro()
    
    while True:
        user_query = input("\nYou: ").lower()
        
        if user_query == 'exit':
            print("\n🚀 Happy investing! Remember: Crypto is risky—always do your own research!")
            break
        
        elif user_query == 'help':
            show_help()
        
        elif user_query == 'list':
            list_cryptos()
        
        # Profitability-Based Recommendation (Rising Price + High Market Cap)
        elif any(word in user_query for word in ["trend", "profit", "rising", "grow"]):
            profitable_coins = [
                crypto for crypto in crypto_db 
                if crypto_db[crypto]["price_trend"] == "rising" 
                and crypto_db[crypto]["market_cap"] == "high"
            ]
            if profitable_coins:
                print(f"\n📈 Invest in {', '.join(profitable_coins)}! They're trending up with strong market potential! 🚀")
            else:
                print("\n⚠️ No highly profitable coins found. Consider sustainable options instead.")
        
        # Sustainability-Based Recommendation (Low Energy + High Score)
        elif any(word in user_query for word in ["sustainable", "green", "eco", "environment"]):
            sustainable_coin = max(
                crypto_db.keys(), 
                key=lambda x: crypto_db[x]["sustainability_score"]
            )
            print(f"\n🌱 {sustainable_coin} is the most sustainable! (Score: {crypto_db[sustainable_coin]['sustainability_score']}/10)")
        
        # Balanced Recommendation (Profitable + Sustainable)
        elif any(word in user_query for word in ["best", "recommend", "advice", "long-term"]):
            balanced_choice = max()
            crypto_db.keys(),
            key=lambda x: (
                    crypto_db[x]["sustainability_score"] * 0.6 + 
                    (1 if crypto_db[x]["price_trend"] == "rising" else 0) * 0.4
                )
            print(f"\n💎 My top pick: {balanced_choice}! It balances growth + sustainability. 🌍📊")
        
        else:
            print("\n🤖 Sorry, I didn’t understand. Try asking about 'trending cryptos' or 'sustainable coins'!")

# Run the Chatbot
if __name__ == "__main__":
    crypto_advisor()