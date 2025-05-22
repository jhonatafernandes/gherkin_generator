import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# Carrega as variáveis de ambiente
load_dotenv()

# Define o LLM primário (OpenAI GPT-4o)
try:
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY")
    )
except Exception as e:
    print(f"Erro ao conectar com OpenAI: {e}")
    llm = None

# Fallback para Groq (LLaMA 3)
if llm is None:
    try:
        llm = ChatGroq(
            model="llama3-70b-8192",  # Nome mais comum na Groq
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0.7
        )
        print("Usando Groq LLaMA 3 como fallback")
    except Exception as e:
        raise RuntimeError(f"Erro ao conectar com Groq: {e}")

@CrewBase
class CrewGherkin():
    """Gherkin crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def analista_requisitos(self) -> Agent:
        return Agent(config=self.agents_config['analista_requisitos'], llm=llm, verbose=True)

    @agent
    def estrategista_testes(self) -> Agent:
        return Agent(config=self.agents_config['estrategista_testes'], llm=llm, verbose=True)

    @agent
    def autor_gherkin(self) -> Agent:
        return Agent(config=self.agents_config['autor_gherkin'], llm=llm, verbose=True)

    @agent
    def especialista_dados_teste(self) -> Agent:
        return Agent(config=self.agents_config['especialista_dados_teste'], llm=llm, verbose=True)

    @agent
    def gerador_artefatos_automacao(self) -> Agent:
        return Agent(config=self.agents_config['gerador_artefatos_automacao'], llm=llm, verbose=True)

    @agent
    def revisor_qualidade_testes(self) -> Agent:
        return Agent(config=self.agents_config['revisor_qualidade_testes'], llm=llm, verbose=True)

    @task
    def analise_requisitos_task(self) -> Task:
        return Task(config=self.tasks_config['analise_requisitos_task'])

    @task
    def definicao_estrategia_testes_task(self) -> Task:
        return Task(config=self.tasks_config['definicao_estrategia_testes_task'])

    @task
    def criacao_cenarios_gherkin_task(self) -> Task:
        return Task(config=self.tasks_config['criacao_cenarios_gherkin_task'], output_file='report_gherkin.md')

    @task
    def geracao_dados_teste_task(self) -> Task:
        return Task(config=self.tasks_config['geracao_dados_teste_task'], output_file='report_geracao_dados_task.json')

    @task
    def geracao_artefatos_automacao_task(self) -> Task:
        return Task(config=self.tasks_config['geracao_artefatos_automacao_task'], output_file='report_geracao_artefatos_task.md')

    @task
    def revisao_qualidade_artefatos_task(self) -> Task:
        return Task(config=self.tasks_config['revisao_qualidade_artefatos_task'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
            process=Process.hierarchical,
            manager_llm=llm
        )
