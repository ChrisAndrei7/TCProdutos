Feature: Gerenciamento de produtos

  Scenario: Adicionar um novo produto
    Given que eu tenho os detalhes do produto
    When eu faço o cadastro de um produto
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um produto
    When eu faço a consulta dos produtos cadastros
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Editar um produto existente
    Given que eu tenho os detalhes atualizados do produto
    When eu faço uma atualização de um produto
    Then eu devo receber uma resposta com o código de status 200
