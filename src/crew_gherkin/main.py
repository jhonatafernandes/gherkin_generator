#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew_gherkin.crew import CrewGherkin

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'descricao_funcionalidade': '''
        Título da Funcionalidade: Login Básico com Usuário Fixo

Descrição Geral:

Permitir que um usuário faça login no sistema usando credenciais fixas.

Requisitos Principais:

Campos de Login:
Deve haver um campo para "Usuário".
Deve haver um campo para "Senha".
Deve haver um botão "Entrar".
Login Válido:
Se o usuário digitar "admin" no campo "Usuário" E "senha123" no campo "Senha" e clicar em "Entrar":
O sistema deve exibir a mensagem "Login bem-sucedido!".
Login Inválido:
Se o usuário digitar qualquer outra combinação de usuário/senha e clicar em "Entrar":
O sistema deve exibir a mensagem "Usuário ou senha inválidos."
Considerações para Simplificar o Teste:

Não há necessidade de verificar se o usuário existe em um banco de dados. As credenciais são fixas ("admin" / "senha123").
Não se preocupe com redirecionamento para outra página após o login. Apenas a mensagem é suficiente.
Não se preocupe com tentativas de login, bloqueio de conta, "esqueci minha senha", etc.
        ''',
    }
    
    try:
        gherkin_crew_instance = CrewGherkin()
        resultado_final = gherkin_crew_instance.crew().kickoff(inputs=inputs)

        print("\n\n✅ Execução da CrewGherkin Concluída!")
        print("----------------------------------------")
        print("📋 RESULTADO FINAL DA CREW:")
        print("----------------------------------------")
        print(resultado_final)
        print("----------------------------------------")
    except Exception as e:
        raise Exception(f"Ocorreu um erro ao executar a crew: {e}")


