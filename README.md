# school-api
Simples API REST desenvolvida em python com o uso do framework Django, usando um exemplo fictício de uma escola. Alguns dos itens utilizados no projeto:
- Python
- Django/Django Rest
- PostgreSQL
- Docker

### Instalação
Primeiramente, você deve ter instalado o [python(3>=)](https://www.python.org/downloads/) no seu computador, além do gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/installing/). Com os dois devidamente instalados, ainda é necessário instalar libs relacionadas ao Docker, caso ainda não as possua:

Featurings do projeto:
- [Python v3.6.9](https://www.python.org/downloads/)
- [Docker v19.03.12](https://docs.docker.com/engine/install/)
- [Docker Compose v1.26.2](https://docs.docker.com/compose/install/)
- [Docker Machine v0.16.0](https://docs.docker.com/machine/install-machine/)



### Rodando Projeto

Com todas as features instaladas e o repositório clonado, basta ir até a raiz do projeto e executar os comandos:

- Iniciar nova máquina docker dev `docker-machine create -d virtualbox dev`
- Configurar shell para usar nova máquina dcoker `eval $(docker-machine env dev)`
- Build imagens `docker-compose build`
- Capturar IP de dev para visualização `docker-machine ip dev`
- Iniciar services `docker-compose up`

Se tudo ocorrer bem, basta apenas usar o IP de dev capturado no passo anterior e poderá ter acesso a API com:

```sh
  http://<IP_dev>:8000
```

### API

Para ter acesso a toda informação necessária sobre a API, basta apenas ver a documentação gerada pelo swagger, pelas seguintes rotas:

```sh
  http://<IP_dev>:8000/swagger
  ou
  http://<IP_dev>:8000/redoc
```
