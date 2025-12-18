from src.ai.llms import get_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def generate_output(carrier, route, risk_prob, delay_days, suggestion=None):
    """
    Translates raw AI model outputs into a human-readable logistics recommendation.
    """
    llm = get_llm()
    
    prompt = ChatPromptTemplate.from_template("""
    You are a Senior Logistics Dispatch Advisor for NexGen. 
    Your task is to interpret model predictions for a shipment and provide a professional recommendation.

    INPUT DATA:
    - Carrier: {carrier}
    - Route: {route}
    - Model Risk Score: {risk}% probability of delay
    - Predicted Delay Magnitude: {days} days
    - Recommended Action: {suggestion}

    INSTRUCTIONS:
    1. Start by clearly stating if the package is predicted to be on time or delayed.
    2. If delayed, explain the magnitude (how many days).
    3. Provide a brief, professional justification or corrective action based on the recommendation.
    4. Keep the tone executive and concise (max 3 sentences).
    """)

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({
        "carrier": carrier,
        "route": route,
        "risk": f"{risk_prob * 100:.0f}",
        "days": f"{delay_days:.1f}",
        "suggestion": suggestion if suggestion else "Monitor shipment closely."
    })

    return response