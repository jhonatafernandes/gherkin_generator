# CrewGherkin Crew

[![crewAI](https://img.shields.io/badge/powered%20by-crewAI-blue?style=for-the-badge)](https://crewai.com)

Bem-vindo ao projeto CrewGherkin Crew! Este projeto utiliza o framework [crewAI](https://crewai.com) para criar um sistema multiagente de IA focado na geração de artefatos para testes automatizados. O objetivo principal é auxiliar na criação de cenários Gherkin, estratégias de teste, dados de teste e outros elementos essenciais para um processo de automação de testes robusto e eficiente.

O CrewGherkin Crew é projetado para ajudar equipes de desenvolvimento e QA a:
*   Analisar descrições de funcionalidades e transformá-las em requisitos testáveis.
*   Definir estratégias de teste abrangentes.
*   Gerar cenários de teste claros e concisos no formato Gherkin.
*   Identificar e sugerir dados de teste relevantes.
*   Criar uma base inicial para a codificação de testes automatizados.

Este template é desenhado para facilitar a configuração de um sistema multiagente, permitindo que seus agentes colaborem efetivamente em tarefas complexas, maximizando sua inteligência e capacidades coletivas.

## Instalação

Certifique-se de que você tem Python >=3.10 <3.13 instalado em seu sistema. Este projeto utiliza [UV](https://docs.astral.sh/uv/) para gerenciamento de dependências e pacotes, oferecendo uma experiência de configuração e execução simplificada.

Primeiro, se ainda não o fez, instale o uv:

```bash
pip install uv
```

Em seguida, navegue até o diretório do seu projeto e instale as dependências:

(Opcional) Bloqueie as dependências e instale-as usando o comando da CLI:

```bash
crewai install
```

### Customizando

**Adicione sua `OPENAI_API_KEY` (ou outras chaves de LLM) no arquivo `.env`**

*   Modifique `src/crew_gherkin/config/agents.yaml` para definir seus agentes.
*   Modifique `src/crew_gherkin/config/tasks.yaml` para definir suas tarefas.
*   Modifique `src/crew_gherkin/crew.py` para adicionar sua própria lógica, ferramentas e argumentos específicos.
*   Modifique `src/crew_gherkin/main.py` para adicionar entradas personalizadas para seus agentes e tarefas.

## Executando o Projeto

Para iniciar sua equipe de agentes de IA e começar a execução das tarefas, execute este comando a partir da pasta raiz do seu projeto:

bash
crewai run

Este comando inicializa a CrewGherkin Crew, montando os agentes e atribuindo-lhes tarefas conforme definido em sua configuração.

## Entendendo Sua Crew

A CrewGherkin Crew é composta por múltiplos agentes de IA, cada um com papéis, objetivos e ferramentas únicos. Esses agentes colaboram em uma série de tarefas, definidas em `config/tasks.yaml`, utilizando suas habilidades coletivas para alcançar objetivos complexos. O arquivo `config/agents.yaml` descreve as capacidades e configurações de cada agente em sua equipe.

## Autor

Este projeto é mantido por:

*   **Jhonata Fernandes** - [Linkedin](https://www.linkedin.com/in/jhonata-fernandes-128292126/)

Sinta-se à vontade para entrar em contato ou contribuir!

## Suporte

Para suporte, perguntas ou feedback sobre a CrewGherkin Crew ou crewAI:
*   Visite nossa [documentação](https://docs.crewai.com)
*   Entre em contato conosco através do nosso [repositório GitHub](https://github.com/joaomdmoura/crewai)
*   [Junte-se ao nosso Discord](https://discord.com/invite/X4JWnZnxPb)
*   [Converse com nossos documentos](https://chatg.pt/DWjSBZn)

Vamos criar maravilhas juntos com o poder e a simplicidade do crewAI.
