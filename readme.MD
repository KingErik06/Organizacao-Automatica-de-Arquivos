![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-estável-brightgreen)
![Automation](https://img.shields.io/badge/focus-automation-orange)

# Automação de Organização de Arquivos

## 📌 Descrição
Automação desenvolvida em Python para organizar arquivos automaticamente, separando-os por tipo/extensão e eliminando a necessidade de organização manual.
Esse script é ideal para pastas como **Downloads**, **Documentos** ou diretórios com grande volume de arquivos misturados.

---

## 🎯 Problema Resolvido
A organização manual de arquivos:
- Consome tempo
- Gera desordem
- É repetitiva e sujeita a erros

Esta automação resolve o problema ao estruturar os arquivos de forma automática, padronizada e rápida.

---

## ⚙️ Como a Automação Funciona
1. Os arquivos são inseridos na pasta de entrada
2. O script identifica a extensão de cada arquivo
3. Os arquivos são movidos automaticamente para pastas organizadas por extensão

---

## 📥 Entrada
- Arquivos de diferentes tipos e extensões  
- Os arquivos devem ser colocados na pasta `data/input`

Exemplo:
```
📁 input
├── arquivo.pdf
├── imagem.png
├── musica.mp3
```

---

## 📤 Saída
- Arquivos organizados em pastas de acordo com suas extensões  
- Estrutura criada automaticamente dentro da pasta `data/input`

Exemplo:
```
📁 input
├── Documentos/
│ └── arquivo.pdf
├── Imagens/
│ └── imagem.png
├── Audio/
│ └── musica.mp3
```
---

## ▶️ Como Executar
```bash
python src/main.py
```

---

## 🛠️ Tecnologias Utilizadas
- Python
- Pathlib
- Shutil

---

## 📈 Benefícios
- Economia de tempo
- Organização automática e padronizada de arquivos
- Redução de trabalho manual
- Pode ser adaptado para diferentes regras de organização

---

## 👤 Indicado para
- Escritórios
- Pequenas empresas
- Freelancers
- Usuários com grande volume de arquivos digitais

---

> O script pode ser facilmente adaptado para regras específicas de organização conforme a necessidade do usuário.