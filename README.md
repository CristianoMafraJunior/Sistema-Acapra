# Sistema-ACAPRA
O projeto "Sistema para Adoção Animal - ACAPRA" visa criar uma aplicação web  que permita a comunidade visualizar os animais disponíveis para adoção, com opções administrativas para a ACAPRA gerir (cadastrar, editar, remover) os cadastros dos animais. O objetivo é facilitar e promover a adoção de animais por meio de plataforma tecnológica

## Funções da comunidade:

- Catálogo de animais para adoção: Adicionar página para exibição dos animais cadastrados pelos gestores e voluntários. Devem ser aplicados filtros para uma listagem mais assertiva pelo usuário, como, por exemplo, tipo do animal, se ainda não foi adotado, tamanho, idade e entre outros.

- Detalhes dos Animais: Ao selecionar um animal devem existir uma página para exibir todos os detalhes dele e todas as suas fotos. Acrescentar a opção de adoção em que o usuário será direcionado para um formulário de adoção.

- Formulário de Adoção: Criar o formulário de adoção conforme fornecido pela ACAPRA. O formulário deve ser persistido e visualizado nas funções administrativas e encaminhado para o e-mail da ACAPRA.

## Funções administrativas:

- Login e senha: Permitir que gestores e voluntários acessem as informações dos animais com privilégios adicionais.

- Cadastro de novos animais: Permitir que gestores e voluntários adicionem novos animais à plataforma. O cadastro deve conter informações do animal, fotos, e detalhes adicionais como saúde e necessidades especiais.

- Atualização de informações: Permitir que gestores e voluntários atualizem as informações dos animais existentes. Em caso de doação o sistema deve armazenar essa informação, a data de doação e tutor responsável pela adoção.

- Formulário de Adoção: Criar a listagem e visualização dos formulários de adoção respondidos pelos usuários.

## Clonar o Projeto e Configurar o Projeto

1. Clonar o Repositório
```bash
git clone https://github.com/CristianoMafraJunior/Sistema-Acapra
```

2. Criar e Ativar o Ambiente Virtual
```bash
python -m venv venv
```

3. Instalar Dependências do Projeto
```bash
pip install -r requirements.txt
```

4. Instalar o Tailwind:
```bash
npm install -D tailwindcss
```
5. Gerar o arquivo de configuração:
```bash
npx tailwindcss init
```

## ALUNOS

- [Leonardo Antunes Gonçalves](https://github.com/LeskeLense)
- [Cauã Nascimento Machado De Paula](https://github.com/CauaDePaula)
- [Cristiano Mafra Junior](https://github.com/CristianoMafraJunior)
- [Eryck Michalski](https://github.com/EryckScript)
- [Rafael de Araujo da Silva](https://github.com/Cascaum)
