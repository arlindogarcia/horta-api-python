# API - Horta em Python

- Documentação das tabelas do banco de dados:
![alt text](https://saerp-geral.s3.sa-east-1.amazonaws.com/public/chamados/446491e37c0fd85781ad88121.jpeg)


# Modelo de requisições - FERTILIZANTES
- ```/fertilizante GET (LISTAR)```
- ```/fertilizante/:id GET (VISUALIZAR)```
- ```/fertilizante POST (CADASTRAR)```
     ```
      {
        "nome": "Fertilizante 1",
        "fabricante": "Fabrica 1",
        "categoria_id": "6"
      }
     ```
- ```/fertilizante/:id PUT (EDITAR)```
     ```
      {
        "nome": "Fertilizante 1",
        "fabricante": "Fabrica 1",
        "categoria_id": "6"
      }
     ```
- ```/fertilizante/:id DELETE (DELETAR)```

# Modelo de requisições - HORTA E HORTA ITEM
- ```/horta GET (LISTAR)```
- ```/horta/:id GET (VISUALIZAR)```
- ```/horta POST (CADASTRAR)```
     ```
     {
        "nome_horta": "Horta 1",
        "area_plantio": 10.5,
        "horta_items": [
          {
            "quantidade": 5,
            "hortalicas_id": 4
          }
        ]
    }
     ```
- ```/horta/:id PUT (EDITAR)```
     ```
     {
        "nome_horta": "Horta 1",
        "area_plantio": 10.5,
        "horta_items": [
          {
            "quantidade": 5,
            "hortalicas_id": 4
          }
        ]
    }
     ```
- ```/horta/:id DELETE (DELETAR)```

# Modelo de requisições - CATEGORIA
- ```/categoria GET (LISTAR)```
- ```/categoria/:id GET (VISUALIZAR)```
- ```/categoria POST (CADASTRAR)```
     ```
    {
      "nome": exemplo,
    }
     ```
- ```/categoria/:id PUT (EDITAR)```
     ```
    {
      "nome": exemplo,
    }
     ```
- ```/categoria/:id DELETE (DELETAR)```

# Modelo de requisições - MEDIÇÃO
- ```/medicao GET (LISTAR)```
- ```/medicao/:id GET (VISUALIZAR)```
- ```/medicao POST (CADASTRAR)```
     ```
    {
      "valor_humidade": 15,
      "data_leitura": "2022-11-13",
      "horta_id": "7"
    }
     ```
- ```/medicao/:id PUT (EDITAR)```
     ```
    {
      "valor_humidade": 15,
      "data_leitura": "2022-11-13",
      "horta_id": "7"
    }
     ```
- ```/medicao/:id DELETE (DELETAR)```

# Modelo de requisições - IRRIGAÇÃO
- ```/irrigacao GET (LISTAR)```
- ```/irrigacao/:id GET (VISUALIZAR)```
- ```/irrigacao POST (CADASTRAR)```
     ```
    {
      "data_irrigacao": "2022-11-13",
      "horta_id": "3"
    }
     ```
- ```/irrigacao/:id PUT (EDITAR)```
     ```
    {
      "data_irrigacao": "2022-11-13",
      "horta_id": "3"
    }
     ```
- ```/irrigacao/:id DELETE (DELETAR)```

# Modelo de requisições - HORTALICAS
- ```/hortalicas GET (LISTAR)```
- ```/hortalicas/:id GET (VISUALIZAR)```
- ```/hortalicas POST (CADASTRAR)```
     ```
    {
      "categoria_id": 1,
      "largura": 20.0,
      "comprimento": 30.0,
      "altura": 25.0,
      "fertilizantes_id": 3,
      "nome": "Tomate"
    }
     ```
- ```/hortalicas/:id PUT (EDITAR)```
     ```
    {
      "categoria_id": 1,
      "largura": 20.0,
      "comprimento": 30.0,
      "altura": 25.0,
      "fertilizantes_id": 3,
      "nome": "Tomate"
    }
     ```
- ```/hortalicas/:id DELETE (DELETAR)```

# Modelo de requisições - ESTOQUE
- ```/estoque GET (LISTAR)```
- ```/estoque/:id GET (VISUALIZAR)```
- ```/estoque POST (CADASTRAR)```
     ```
    {
      "codigo": "exemplo1",
      "origem_nome": "exemplo2",
      "origem_id": 1,
      "quantidade": 30,
      "tipo_movimento": 1,
      "cancelado": 0,
      "observacoes": "Teste"
    }
     ```
- ```/estoque/:id PUT (EDITAR)```
     ```
    {
      "codigo": "exemplo1",
      "origem_nome": "exemplo2",
      "origem_id": 1,
      "quantidade": 30,
      "tipo_movimento": 1,
      "cancelado": 0,
      "observacoes": "Teste"
    }
     ```
- ```/estoque/:id DELETE (DELETAR)```
