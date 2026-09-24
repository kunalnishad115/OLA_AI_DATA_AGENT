from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from config.settings import LOW_MODEL, MID_MODE, HIGH_MODEL
load_dotenv()

def llm_pick(level:str):
    """
    Picks the appropriate LLM based on the level of the question.

    Args:
        level (str): The level of the question, can be "low", "medium", or "high".

    Returns:
        ChatMistralAI: The LLM instance to be used.
    """

    if level == "low":
        return ChatMistralAI(model_name=LOW_MODEL, temperature=0)
    elif level=="medium":
        return ChatMistralAI(model_name=MID_MODE, temperature=0)
    elif level=="high":
        return ChatMistralAI(model_name=HIGH_MODEL, temperature=0)
    else:
        raise ValueError("Invalid level. Please choose from 'low', 'medium', or 'high'.")

    

llm_obj=llm_pick("low")
ans=llm_obj.invoke("capital of US?")
print(ans.content)