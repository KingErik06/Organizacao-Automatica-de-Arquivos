# Automação de Organização de Arquivos

## 📌 Descrição
Script em Python desenvolvido para organizar arquivos automaticamente, agrupando-os por tipo e eliminando a necessidade de organização manual.

## 🎯 Problema Resolvido
A organização manual de muitos arquivos consome tempo, gera desordem e está sujeita a erros.  
Esta automação resolve esse problema ao estruturar os arquivos de forma automática e padronizada.

## ⚙️ Como a Automação Funciona
1. Os arquivos são inseridos na pasta de entrada
2. O script identifica o tipo de cada arquivo
3. Os arquivos são organizados automaticamente em pastas por extensão

## 📥 Entrada
- Arquivos de diferentes tipos e extensões  
- Os arquivos devem ser colocados na pasta `data/input`

## 📤 Saída
- Arquivos organizados em pastas de acordo com suas extensões  
- Estrutura criada automaticamente dentro da pasta `data/input`

## ▶️ Como Executar
```bash
python src/main.py
```

## 🛠️ Tecnologias Utilizadas
- Python
- Pathlib
- Shutil

## 📈 Benefícios
- Economia de tempo
- Organização automática e padronizada de arquivos
- Redução de trabalho manual

> Esta automação é ideal para quem lida com grandes volumes de arquivos e deseja manter a organização de forma simples e eficiente.