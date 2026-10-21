from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import config

llm = ChatGoogleGenerativeAI(
    model=config.MODEL_NAME,
    google_api_key=config.GEMINI_API_KEY
)

researcher_agent = Agent(
    role="Web News Analyst",
    goal="Find and analyze recent and trending news from the internet",
    backstory="An experienced information researcher who quickly gathers accurate data from various web sources.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

writer_agent = Agent(
    role="SEO Content Writer",
    goal="Write engaging and SEO-friendly blog posts based on gathered data",
    backstory="A professional content writer who creates compelling and readable blog articles.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

support_agent = Agent(
    role="Customer Experience Specialist",
    goal="Provide professional and helpful responses to website visitors and customers",
    backstory="A customer care expert skilled at resolving inquiries smoothly and efficiently.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)
