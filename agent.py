import os, datetime
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

swing_agent = Agent(
    model=Groq(id="llama3-8b-8192"),
    tools=[
        YFinanceTools(stock_price=True,
                      company_info=True,
                      analyst_recommendations=True),
        DuckDuckGoTools()
    ],
    description="Generate 3 daily momentum stock picks with risk scores"
)

def get_picks():
    prompt = (
        "Current date: {}. "
        "Find 3 U.S. stocks showing recent momentum (>5 % 5-day gain or breakout). "
        "Return: Ticker, Last Close, 1-Mo Avg Target, 0-100 Risk Score, 1-line rationale."
    ).format(datetime.date.today())
    return swing_agent.run(prompt).content