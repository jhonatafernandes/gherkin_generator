```gherkin
# Cenário de Login Válido
Funcionalidade: Login no sistema

Cenário: Login com credenciais válidas
  Dado que o usuário está na página de login
  E que o campo "Usuário" contém "admin"
  E que o campo "Senha" contém "senha123"
  Quando o usuário clica no botão "Entrar"
  Então o sistema deve exibir a mensagem "Login bem-sucedido!"

# Cenário de Login Inválido
Cenário: Login com credenciais inválidas
  Dado que o usuário está na página de login
  E que o campo "Usuário" contém "usuario_invalido"
  E que o campo "Senha" contém "senha_invalida"
  Quando o usuário clica no botão "Entrar"
  Então o sistema deve exibir a mensagem "Usuário ou senha inválidos."

# Cenário de Campos Vazios
Cenário: Tentativa de login com campos vazios
  Dado que o usuário está na página de login
  E que o campo "Usuário" está vazio
  E que o campo "Senha" está vazio
  Quando o usuário clica no botão "Entrar"
  Então o sistema deve exibir a mensagem "Usuário ou senha inválidos."

# Cenário de Comprimento Máximo
Cenário: Inserir dados com comprimento máximo permitido
  Dado que o usuário está na página de login
  E que o campo "Usuário" contém um texto com o comprimento máximo permitido
  E que o campo "Senha" contém um texto com o comprimento máximo permitido
  Quando o usuário clica no botão "Entrar"
  Então o sistema deve exibir a mensagem "Usuário ou senha inválidos."

# Cenário de Caracteres Especiais
Cenário: Inserção de caracteres especiais nos campos de entrada
  Dado que o usuário está na página de login
  E que o campo "Usuário" contém "!@#$%"
  E que o campo "Senha" contém "^&*()"
  Quando o usuário clica no botão "Entrar"
  Então o sistema deve exibir a mensagem "Usuário ou senha inválidos."
```

This answer provides the Gherkin scenarios in markdown format, addressing both valid and invalid login attempts, along with edge cases such as empty fields and special characters.