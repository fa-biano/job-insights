# 💡 Projeto Job Insights!

Delivery App é uma aplicação full stack desenvolvida para ser um site de compras de bebidas online.
O sistema possui 3 fluxos principais: Cliente, Vendedor e Admin.

Clientes realizam seus pedidos e conseguem acompanhar o tracking da preparação até a entrega. Além de poder consultar o histórico de pedidos anteriores.

Os vendedores visualizam todos os pedidos que estão pendentes de preparação e atualizam o status do tracking até serem enviados aos clientes.

Todo controle de acesso é feito pelo fluxo do Admin, onde são criados os logins para os vendedores/clientes/admins. (Clientes podem criar seu próprio login através de formulário de cadastro no site)

O desenvolvimento desse projeto foi realizado durante o curso de Desenvolvimento Web na [Trybe](https://www.betrybe.com/)!

## 🔥 Tecnologias utilizadas:

  * Pyhton
  * Pytest
  * Flask
  * Jinja  

## ✨ Inicializando:

  Clone o repositório: `git clone git@github.com:fa-biano/job-insights.git`

  Execute no terminal `python3 -m venv .venv && source .venv/bin/activate` para habilitar o amnbiente virtual

  Instale as depenência com `python3 -m pip install -r dev-requirements.txt`. *(Algumas depências do pytest precisam de pré-instalação de alguns pacotes, por isso, caso apresente algum erro no terminal, basta executar o comando de instalação novamente.)*

  Inicie a aplicação com `python3 -m flask run`. No navegador acesse `http://localhost:5000/`.