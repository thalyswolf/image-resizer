# Image Resizer
Projeto com a finalidade de redimensionar uma imagem em segundo plano, este código conta com dois microservices onde um é responsável por receber uma request e encaminhar para uma fila e outro onde realmente redimensiona a imagem.

## Microservice API
Esse microserviço recebe uma request em 'form-data' com a imagem e com parâmetros opcionais  de width/height.
http://localhost:8081/docs

## Microservice Resizer
É o microserviço responsável por redimensionar uma imagem, ele funciona de forma passiva onde fica 'escutando' uma fila.

## Como rodar a aplicação
No diretório .docker executar o comando 
`` $ docker-compose up --b``

## Ferramentas utilizadas
1. Docker
2. Python 3
3. RabbitMq
4. FastAPI