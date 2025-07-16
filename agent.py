import os, datetime
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

swing_agent = Agent(
    model=Groq(id="llama3-8b-8192"),
    tools=[
        YFinanceTools(
            stock_price=True,
            company_info=True,
            analyst_recommendations=True
        ),
        DuckDuckGoTools()
    ],
    description="Daily momentum-stock picker"
)

def get_picks():
    today = datetime.date.today()
    prompt = (
        f"Today is {today}.  "
        "Use the provided tools to:\n"
        "1.  Find three Indian tickers that have gained >5 % in the last 5 trading days.\n"
        "2.  For each ticker obtain:\n"
        "   - last closing price\n"
        "   - average 1-month analyst target\n"
        "   - a 0–100 risk score (based on volatility and news sentiment)\n"
        "3.  Return a clean markdown table: Ticker | Last Close | 1-Mo Target | Risk | One-line rationale"
    )
    return swing_agent.run(prompt, stream=False).content