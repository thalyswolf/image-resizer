
# Image Resizer
Projeto com a finalidade de redimensionar uma imagem em segundo plano, este código conta com dois microservices onde um é responsável por receber uma request e encaminhar para uma fila e outro onde realmente redimensiona a imagem.

## Microservice API
Esse microserviço recebe uma request em 'form-data' com a imagem e com parâmetros opcionais de width/height.
http://localhost:8081/docs

  
## Microservice Resizer
É o microserviço responsável por redimensionar uma imagem, ele funciona de forma passiva onde fica 'escutando' uma fila.

## Como rodar a aplicação
No diretório .docker executar o comando
```console
$ docker-compose up --b
```
## Ferramentas utilizadas
1. Docker
2. Python 3
3. RabbitMQ
4. FastAPI

## Executando testes unitários
Os testes unitários podem ser executados dentro ou fora do container docker. 
#### Exemplo de teste de dentro do container
```console
$ python -m pytest src/
```

## Como executar um teste
Após o docker inicializar ele subirá uma API na porta 8081 com o endpoint /resize-image, enviando um POST com a imagem. Se a API retornar 202 - Accepted significa que funcionou.

![Imagem do Postman](https://i.imgur.com/NuE9OHU.png)

## Executando um teste usando cURL
```console
$ curl --location --request POST 'http://localhost:8081/resize-image' --form 'file=@"/DIRETORIO/DA/IMAGEM.png"'
```