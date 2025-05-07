# Extension_Project_IA

Projeto de extensão de Inteligência Artificial aplicada na automação de processos industriais.

## 📁 Estrutura do Repositório

- `matriz.py`: Script principal responsável pelo processamento das matrizes de dados.
- `base_testI.txt` & `base_testII.txt`: Arquivos de entrada contendo dados brutos para análise.
- `matrizI.csv` & `matrizII.csv`: Resultados processados exportados em formato CSV.
- `venv/`: Ambiente virtual Python para gerenciamento de dependências (não incluído no repositório).

## 🧪 Requisitos

- Python 3.8 ou superior

## Entendimento:

O objetivo do programa é receber um arquivos com vários dados, transformá-lo em uma matriz numérica e o programa deve ser capaz de reverter para texto novamente.
Passo a Passo: 
1. Entender o problema, os dados e pensar na solução.
2. Verificar se tem observações ou excessões no processo, por exemplo, a questão cita caracteres especiais e pontuação.
3. Após entender, pesquisei como poderia ler uma arquivo com o  python e a partir disso apliquei os conceitos.
4. Pensei em uma estrutura de dados chamada Tabela Hash, não apliquei diretamente a estrutura, mas o conceito sim. Basicamente, criei uma lista de caracteres(letras maiúsculas, minúsculas, números e espaço em branco) e criei uma variável que armazenava em dicionário (chave e valor), a ordem foi direta não fiz a função em específica, praticamente a letra "a" recebia o valor "1", ou seja, chave = "a", valor = "1".
5. Mas se a função é capaz de gerar um número para o caracter, é possível tamnbém fazer o processo reverso e é isso que o matriz_convertida faz no script. Utiliza o mesmo conceito.
6. No final, peço para o script criar dois documentos comas as matrizes com n linhas e 20 colunas. (Só consegui fazer o arquivo .csv com 20 colunas)
7. Praticar as boas práticas de programação também foi essencial para deixar organizado e modularizado.

Dificuldades: Entender o problema no início e gerar a solução.
