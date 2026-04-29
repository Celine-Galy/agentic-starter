from agents.llm_agent import ask_llm
from tools.crypto_api import get_bitcoin_price

def route(user_input):
    
    # règle simple (améliorable avec LLM plus tard)
    if "bitcoin" in user_input.lower():
        price = get_bitcoin_price()
        return f"Le prix du Bitcoin est : {price} USD"
    
    # sinon → LLM
    return ask_llm(user_input)