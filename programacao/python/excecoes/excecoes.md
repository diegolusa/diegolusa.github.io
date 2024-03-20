---
title: "Python - Strings"
tags:
 - Programação
 - Linguagens de Programação
 - Python
 - Try-Catch
date: 2024-02-26 08:00:00
---


O `try`, `except`, `finally` é uma estrutura em Python que permite lidar com exceções de forma controlada e garantir que determinadas ações sejam executadas independentemente de ocorrer uma exceção ou não.

### Sintaxe:

A estrutura básica é composta por três blocos:

```python
try:
    # Código que pode gerar exceções
    # Se ocorrer uma exceção, o controle será transferido para o bloco except correspondente
except Excecao_Tipo_1:
    # Bloco executado se ocorrer uma exceção do tipo ExcecaoTipo1
except Excecao_Tipo_2:
    # Bloco executado se ocorrer uma exceção do tipo ExcecaoTipo2
else:
    # Bloco opcional executado se nenhuma exceção ocorrer no bloco try
finally:
    # Bloco opcional executado sempre, independentemente de ocorrer uma exceção ou não
```

- `try`: Este bloco contém o código que pode gerar exceções.
  
- `except`: Este bloco captura exceções específicas que podem ocorrer dentro do bloco `try`. É possível ter vários blocos `except` para diferentes tipos de exceções.

- `else`: É opcional e executado apenas se nenhuma exceção ocorrer dentro do bloco `try`. É útil para código que deve ser executado apenas se não houver exceções.

- `finally`: O bloco `finally` é sempre executado, independentemente de ocorrer uma exceção ou não dentro do bloco `try`. É usado para garantir que determinadas ações, como a liberação de recursos, sejam executadas, mesmo em caso de exceção.

### Exemplo de Uso:

```python
try:
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
else:
    print("O arquivo foi lido com sucesso.")
finally:
    arquivo.close()  # Garante que o arquivo seja fechado, mesmo se ocorrer uma exceção
```

Neste exemplo:

- O bloco `try` tenta abrir e ler um arquivo.
  
- Se o arquivo não for encontrado, uma exceção `FileNotFoundError` será levantada e o bloco `except` correspondente será executado, exibindo uma mensagem apropriada.

- Se o arquivo for lido com sucesso, o bloco `else` será executado, indicando que o arquivo foi lido sem problemas.

- O bloco `finally` garante que o arquivo seja fechado, independentemente de ter sido lido com sucesso ou não.

### Utilizações Comuns:

- **Manipulação de Arquivos:** Usado para abrir, ler e fechar arquivos de forma segura, garantindo que os recursos sejam liberados adequadamente.

- **Conexões de Rede e Banco de Dados:** É comum usar `try`, `except`, `finally` ao lidar com operações de rede ou banco de dados para garantir a limpeza adequada de recursos, como fechar conexões.

- **Validação de Entrada de Usuário:** Pode ser usado para validar entrada de usuário e lidar com erros de entrada de forma elegante.


A lista de exceções nativas do Python pode ser encontrada na [documentação oficial](https://docs.python.org/3/library/exceptions.html).