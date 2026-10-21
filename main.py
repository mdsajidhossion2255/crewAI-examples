from crewai import Crew, Process
from tasks import research_task, write_task, support_task
from agents import researcher_agent, writer_agent, support_agent

def run_automation():
    crew = Crew(
        agents=[researcher_agent, writer_agent, support_agent],
        tasks=[research_task, write_task, support_task],
        process=Process.sequential,
        verbose=2
    )

    print("AI Agent automation process is starting...")
    result = crew.kickoff()
    print("\nExecution Result:\n")
    print(result)

if __name__ == "__main__":
    run_automation()
