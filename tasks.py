from crewai import Task
from agents import researcher_agent, writer_agent, support_agent

research_task = Task(
    description="Find and summarize today's important and recent technology or relevant news topics.",
    expected_output="A bulleted list of today's top news summaries.",
    agent=researcher_agent
)

write_task = Task(
    description="Write an engaging blog post based on the news provided by the researcher.",
    expected_output="A complete, well-structured blog post with a catchy title.",
    agent=writer_agent
)

support_task = Task(
    description="Prepare appropriate responses for incoming customer queries and comments on the website.",
    expected_output="A structured list of helpful responses for customers.",
    agent=support_agent
)
