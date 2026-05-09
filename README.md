# 🐍 Fundamentos Python - Curso Completo

Uma formação abrangente em **Python Fundamentals** cobrindo desde conceitos básicos até **Programação Orientada a Objetos (POO)** avançada. Este repositório contém **70+ conceitos práticos** organizados em módulos progressivos com exemplos, exercícios e desafios.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📚 Estrutura do Repositório

```
fundamentos-python/
├── introdução/                          # Conceitos Fundamentais
├── Estrturas de Dados Com Python/       # Estruturas de Dados & Funções
├── Programação Orientada a Objetos/     # POO Avançada
├── Hands-on/                            # Projetos Práticos
├── Desafios-de-Código/                  # Exercícios Desafiadores
└── README.md                            # Este arquivo
```

---

## 🎯 Mapa de Conceitos

### 1️⃣ **CONCEITOS FUNDAMENTAIS** (`introdução/`)

Dominando os alicerces da linguagem Python.

#### Tipos de Dados e Operadores
- **Tipos de Dados Básicos** → [aula-1-tipos-de-dados.py](introdução/aula-1-tipos-de-dados.py)
  - Inteiros, Floats, Booleanos
- **Conversão de Tipos** → [aula-4-convertendo tipos.py](introdução/aula-4-convertendo tipos.py)
- **Operadores Aritméticos** → [aula-6-operadores-aritmeticos.py](introdução/aula-6-operadores-aritmeticos.py)
  - `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Operadores de Comparação** → [aula-7-operadores-de-comparacao.py](introdução/aula-7-operadores-de-comparacao.py)
  - `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Operadores de Identidade** → [aula-8-operadores-de-identidade.py](introdução/aula-8-operadores-de-identidade.py)
  - `is`, `is not`
- **Operadores de Associação** → [aula-9-operadores-de-associacao.py](introdução/aula-9-operadores-de-associacao.py)
  - `in`, `not in`
- **Operadores Lógicos** → [aula-11-estruturas-condicionais.py](introdução/aula-11-estruturas-condicionais.py)
  - `and`, `or`, `not`

#### Variáveis e Entrada/Saída
- **Variáveis e Constantes** → [aula-3-variaveis-e-constantes.py](introdução/aula-3-variaveis-e-constantes.py)
- **Input e Output** → [aula-5-entrada-e-saida-de-dados.py](introdução/aula-5-entrada-e-saida-de-dados.py)
- **Modo Interativo** → [aula-2-modo-interativo.py](introdução/aula-2-modo-interativo.py)

#### Estruturas de Controle
- **Indentação e Blocos** → [aula-10-indentacao-e-blocos.py](introdução/aula-10-indentacao-e-blocos.py)
- **Estruturas Condicionais (if, elif, else)** → [aula-11-estruturas-condicionais.py](introdução/aula-11-estruturas-condicionais.py)
- **Estruturas de Repetição (for, while)** → [aula-12-estruturas-de-repeticao.py](introdução/aula-12-estruturas-de-repeticao.py)
- **Break e Continuação de Loops** → [aula-12-part2-break.py](introdução/aula-12-part2-break.py)

#### Manipulação de Strings
- **Métodos de String** → [aula-13-metodos-uteis-classe-string.py](introdução/aula-13-metodos-uteis-classe-string.py)
  - `.lower()`, `.upper()`, `.strip()`, `.replace()`, `.split()`, `.join()`, `.find()`, `.count()`
- **F-Strings e Interpolação** → [aula-14-interpolacao-de-variaveis.py](introdução/aula-14-interpolacao-de-variaveis.py)
- **Fatiamento de Strings (Slicing)** → [aula-15-fatiamento-de-strings.py](introdução/aula-15-fatiamento-de-strings.py)
  - `string[início:fim:passo]`
- **Strings Multilinhas** → [aula-16-strings-multilinhas.py](introdução/aula-16-strings-multilinhas.py)

#### Exercícios Práticos
- **Par ou Ímpar** → [ex01-par-ou-impar.py](introdução/ex01-par-ou-impar.py)
- **Ano Bissexto** → [ex2-ano-bissexto.py](introdução/ex2-ano-bissexto.py)
- **Contador de Vogais** → [ex03-contador-de-vogais.py](introdução/ex03-contador-de-vogais.py)

---

### 2️⃣ **ESTRUTURAS DE DADOS** (`Estrturas de Dados Com Python/`)

Explorando as principais estruturas para organizar dados em Python.

#### Listas
- **Criação e Acesso** → [aula-01-listas-criacao-e-acesso.py](Estrturas%20de%20Dados%20Com%20Python/aula-01-listas-criacao-e-acesso.py)
  - Criação de listas, indexação, slicing
- **Métodos de Listas** → [aula-01-listas-part3-metodos.py](Estrturas%20de%20Dados%20Com%20Python/aula-01-listas-part3-metodos.py)
  - `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, `.clear()`
  - `.index()`, `.count()`, `.sort()`, `.reverse()`
- **Listas Aninhadas (Matrizes)** → [aula-01-part2-listas-aninhadas-matrizes.py](Estrturas%20de%20Dados%20Com%20Python/aula-01-part2-listas-aninhadas-matrizes.py)
  - Trabalhar com listas multidimensionais

#### Tuplas
- **Criação, Acesso e Desempacotamento** → [aula-02-tuples.py](Estrturas%20de%20Dados%20Com%20Python/aula-02-tuples.py)
  - Tuplas imutáveis, tuple unpacking

#### Conjuntos (Sets)
- **Criação e Operações** → [aula-03-conjuntos-sets.py](Estrturas%20de%20Dados%20Com%20Python/aula-03-conjuntos-sets.py)
  - `add()`, `remove()`, `union()`, `intersection()`, `difference()`

#### Dicionários
- **Criação, Acesso e Métodos** → [aula-04.dicionario.py](Estrturas%20de%20Dados%20Com%20Python/aula-04.dicionario.py)
  - `.keys()`, `.values()`, `.items()`, `.get()`, `.pop()`, `.update()`
  - `.clear()`, `.copy()`, `.fromkeys()`, `.setdefault()`

#### Transformação e Filtragem de Dados
- **Filter com Loops** → [filtro-1.py](Estrturas%20de%20Dados%20Com%20Python/filtro-1.py)
- **Map e Transformação** → [filtro-2.py](Estrturas%20de%20Dados%20Com%20Python/filtro-2.py)
- **List Comprehensions** → [filtro-3.py](Estrturas%20de%20Dados%20Com%20Python/filtro-3.py)
  - Sintaxe concisa para criar e filtrar listas

---

### 3️⃣ **FUNÇÕES** (`Estrturas de Dados Com Python/`)

Dominando a reutilização de código com funções.

#### Conceitos Básicos
- **Definição e Uso de Funções** → [funcoes-pt1.py](Estrturas%20de%20Dados%20Com%20Python/funcoes-pt1.py)
- **Argumentos Nomeados** → [funcoes-pt1-argumentos-nomeados.py](Estrturas%20de%20Dados%20Com%20Python/funcoes-pt1-argumentos-nomeados.py)
- **\*args e \*\*kwargs** → [funcoes-pt1-args-e-kwargs.py](Estrturas%20de%20Dados%20Com%20Python/funcoes-pt1-args-e-kwargs.py)
  - Argumentos variáveis e nomeados variáveis

#### Conceitos Avançados
- **Escopo Local e Global** → [funcoes-pt2-escopo.py](Estrturas%20de%20Dados%20Com%20Python/funcoes-pt2-escopo.py)
  - `global`, `nonlocal`, escopo léxico
- **Closures** → [funcoes-pt2-closures.py](Estrturas%20de%20Dados%20Com%20Python/funcoes-pt2-closures.py)
  - Funções que retornam funções
- **Funções Adicionais** → [funcoes-pt2.py](Estrturas%20de%20Dados%20Com%20Python/funcoes-pt2.py)

---

### 4️⃣ **PROGRAMAÇÃO ORIENTADA A OBJETOS** (`Programação Orientada a Objetos/`)

Dominando o paradigma orientado a objetos.

#### Conceitos Fundamentais
- **Introdução a POO** → [explicacao-conceitos-poo.md](explicacao-conceitos-poo.md)
  - Classes como "moldes" para objetos
  - Instâncias e atributos
  
- **Classes e Instâncias** → [aula01-primeiro-programa.py](Programação%20Orientada%20a%20Objetos/aula01-primeiro-programa.py)
  - Definição de classes, criação de objetos
  - Sistema prático de Bicicletaria
  
- **Método Construtor (__init__)** → [aula01-primeiro-programa.py](Programação%20Orientada%20a%20Objetos/aula01-primeiro-programa.py)
  - Inicialização de atributos
  
- **Método Destrutor (__del__)** → [aula02-destrutor.py](Programação%20Orientada%20a%20Objetos/introducao/aula02-destrutor.py)
  - Limpeza de recursos

#### Atributos e Métodos
- **Atributos de Instância e de Classe** → [aula01-var-de-classe-e-de-instancia.py](Programação%20Orientada%20a%20Objetos/Interfaces%20e%20Classes%20Abstratas%20com%20Python/aula01-var-de-classe-e-de-instancia.py)
  - Diferenças e casos de uso
  
- **Métodos de Classe (@classmethod)** → [aula02-metodos-de-classe-e-metodos-estaticos.py](Programação%20Orientada%20a%20Objetos/Interfaces%20e%20Classes%20Abstratas%20com%20Python/aula02-metodos-de-classe-e-metodos-estaticos.py)
  - Métodos que acessam a classe inteira
  
- **Métodos Estáticos (@staticmethod)** → [aula02-metodos-de-classe-e-metodos-estaticos.py](Programação%20Orientada%20a%20Objetos/Interfaces%20e%20Classes%20Abstratas%20com%20Python/aula02-metodos-de-classe-e-metodos-estaticos.py)
  - Métodos independentes da instância
  
- **Properties (@property, @setter, @deleter)** → [aula03-propety.py](Programação%20Orientada%20a%20Objetos/Encapsulamento/aula03-propety.py)
  - Getters e setters em Python

#### Encapsulamento
- **Conceito de Encapsulamento** → [aula01-encapsulamento.py](Programação%20Orientada%20a%20Objetos/Encapsulamento/aula01-encapsulamento.py)
  - Controlar acesso aos dados
  
- **Recursos Public e Private** → [aula02-recursos-public-e-private.py](Programação%20Orientada%20a%20Objetos/Encapsulamento/aula02-recursos-public-e-private.py)
  - `public`, `_protected`, `__private`
  - Name mangling

#### Herança
- **Herança Simples** → [aula03-heranca.py](Programação%20Orientada%20a%20Objetos/introducao/aula03-heranca.py)
  - Estender funcionalidade de uma classe
  - `super()`
  
- **Herança Simples (Prático)** → [heranca-simples.py](Hands-on/heranca-simples.py)
  - Exemplos práticos de herança
  
- **Herança Múltipla e Mixins** → [heranca-multipla.py](Hands-on/heranca-multipla.py)
  - Herdar de múltiplas classes
  - MRO (Method Resolution Order)

#### Polimorfismo
- **Introdução ao Polimorfismo** → [aula01-intro.py](Programação%20Orientada%20a%20Objetos/Polimorfismo/aula01-intro.py)
  - Muitas formas, uma interface
  
- **Polimorfismo com Herança** → [aula02-polimorfismo-c-heranca.py](Programação%20Orientada%20a%20Objetos/Polimorfismo/aula02-polimorfismo-c-heranca.py)
  - Duck typing, method overriding

#### Interfaces e Classes Abstratas
- **Interfaces e ABC (Abstract Base Classes)** → [aula03-interfaces.py](Programação%20Orientada%20a%20Objetos/Interfaces%20e%20Classes%20Abstratas%20com%20Python/aula03-interfaces.py)
  - `abc.ABC`, `@abstractmethod`
  - Contrato de interface

#### Manipulação de Dados em POO
- **Serialização e JSON** → [aula01-primeiro-programa.py](Programação%20Orientada%20a%20Objetos/aula01-primeiro-programa.py)
  - `to_dict()`, `from_dict()`
  - Persistência com JSON

---

### 5️⃣ **DESAFIOS DE CÓDIGO** (`Desafios-de-Código/`)

Exercícios práticos para consolidar aprendizado.

- **Soma de Tupla** → [desafio1-soma-tupla.py](Desafios-de-Código/desafio1-soma-tupla.py)
  - Manipulação de tuplas, conversão de tipos, `map()`
  
- **Intersection** → [desafio2-intersection.py](Desafios-de-Código/desafio2-intersection.py)
  - Operações com conjuntos
  
- **Contador de Caracteres** → [desafio3-contador-caracteres.py](Desafios-de-Código/desafio3-contador-caracteres.py)
  - Contagem de elementos

---

## 📊 Estatísticas do Repositório

| Categoria | Conceitos | Arquivos | Pasta |
|-----------|-----------|----------|-------|
| Conceitos Fundamentais | 25+ | 16 | `introdução/` |
| Estruturas de Dados | 15+ | 8 | `Estrturas de Dados Com Python/` |
| Funções | 8 | 5 | `Estrturas de Dados Com Python/` |
| Programação Orientada a Objetos | 20+ | 15 | `Programação Orientada a Objetos/` |
| Desafios e Exercícios | 6+ | 6 | `Desafios-de-Código/`, `introdução/` |
| **TOTAL** | **70+** | **50+** | **5 categorias** |

---

## 🚀 Como Usar Este Repositório

### 1. **Para Iniciantes** 🌱
Comece pela pasta `introdução/`:
1. Estude tipos de dados e operadores
2. Pratique estruturas de controle
3. Trabalhe com strings
4. Complete os exercícios básicos

### 2. **Estruturas de Dados** 📦
Na sequência, explore `Estrturas de Dados Com Python/`:
1. Domine listas, tuplas e dicionários
2. Aprenda sobre sets
3. Pratique filtragem com list comprehensions
4. Estude funções avançadas

### 3. **Programação Orientada a Objetos** 🎯
Finalize com `Programação Orientada a Objetos/`:
1. Compreenda classes e instâncias
2. Explore herança e polimorfismo
3. Estude encapsulamento
4. Trabalhe com interfaces e classes abstratas

### 4. **Prática** 💪
Use `Desafios-de-Código/` e `Hands-on/` para consolidar

---

## 📖 Tópicos Transversais

#### Tratamento de Erros
- **Try-Except** → Proteção contra exceções
- Implementado em [aula01-primeiro-programa.py](Programação%20Orientada%20a%20Objetos/aula01-primeiro-programa.py)

#### Manipulação de Arquivos
- **Open, With, JSON** → Ler e escrever dados
- `.dump()`, `.load()`, `os.path.exists()`
- Implementado em [aula01-primeiro-programa.py](Programação%20Orientada%20a%20Objetos/aula01-primeiro-programa.py)

---

## 💡 Principais Aprendizados

✅ **Fundamentos Python** - Tipos, operadores, estruturas de controle  
✅ **Estruturas de Dados** - Listas, dicionários, tuplas, sets  
✅ **Funções Avançadas** - Args, kwargs, closures, escopo  
✅ **Paradigma OOP** - Classes, herança, polimorfismo, encapsulamento  
✅ **Interfaces e Abstrações** - Contratos de código, ABC  
✅ **Manipulação de Dados** - Arquivos, JSON, serialização  
✅ **Desafios Práticos** - Exercícios para consolidar conhecimento  

---

## 📝 Licença

Este repositório é licenciado sob a [MIT License](LICENSE).

---

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Sinta-se à vontade para fazer fork, abrir issues ou contribuir com pull requests.

---

## 📞 Sobre

Uma formação prática completa em Python, desde conceitos fundamentais até técnicas avançadas de Programação Orientada a Objetos. Ideal para quem está começando do zero ou quer consolidar seus conhecimentos.

**Versão:** 1.0  
**Última Atualização:** Maio 2026  
**Status:** Ativo
