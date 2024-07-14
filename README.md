<h1 align="center"> TCFoodSystem - Sistema de pedidos para lanches </h1>
Bem-vindo ao Sistema de Pedidos para Lanchonete! Este projeto está em desenvolvimento como atividade do Tech Challenge para a FIAP, curso Software Architecture.	
<br/>
<b>Neste repositório, temos o microsserviço de produtos</b>
<br/>
:construction: Projeto em construção :construction:
<br/>

# :computer: Endpoint base da aplicação
http://localhost:8003/
<br/>
<br/>

# :hammer: Subida da aplicação
### Subida completa da aplicação via docker:

#### - Subida no docker:
1. Entre no diretório do projeto: `cd appProdutos`
2. Efetue a criação/subida do banco de dados: `docker compose up -d dbProdutos`
3. Efetue a criação da aplicação: `docker compose build`                                                                                                                                                                                                                                                     
      <b>Nota Importante:
      Ao realizar a primeira inicialização, ocasionalmente pode ocorrer o erro "No installed app with label 'pagamentos'". Como solução temporária, sugerimos a seguinte abordagem: caso o erro mencionado ocorra na primeira subida, modifique o arquivo "django.sh" na linha       3, substituindo "produtos" por "application" e efetue novamente o passo 3 antes de seguir para o passo 4.</b>
4. Efetue a subida da aplicação: `docker compose up`
<br/>
  
# :arrow_forward: Uso 
Abaixo, fluxos principais com processo e endpoint desse microsserviço. Para maior detalhe dos campos, temos no projeto(Na pasta appProdutos/Documentos) o arquivo do Postman com a collection estruturando todos as APIs com descrição e valores a serem informados no json.

1 - Criar o pagamento: http://localhost:8003/produtos/create

2 - Consultar pagamentos: http://localhost:8003/produtos/

3 - Atualizar pagamento: http://localhost:8003/produtos/update/{id_do_produto}

4 - Deletar pagamento: http://localhost:8003/produtos/delete/{id_do_produto}

# :page_with_curl: Collection
Disponibilizamos uma collection do postman para ajudar na utilização, contendo todas as APIs deste microserviço e com os campos necessários para preenchimento. 

# :test_tube: Execução dos Testes
Para executar os testes, localizados dentro da pasta "feature", deve ser processado o comando behave abaixo após aplicação estar no ar.
OBS: BDD está dentro do arquivo "produtos.feature"

#### behave appProdutos/project/features/produtos.feature

# Evidência dos testes:

![image](https://github.com/user-attachments/assets/58f34190-b64b-416e-9caf-dc9416151d04)


