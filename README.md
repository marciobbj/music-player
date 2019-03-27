# Music Player

## Hack it locally

clone o repo e use vá até a pasta `front/` e use o comando `npm install`.

### Docker:
Para rodar localmente recomendo o uso de Docker,
em um virtualenv com python 3.6 instale o **docker-compose** com
o comando:
* `pip install docker-compose`

Depois de instalado use o comando:
* `docker-compose build`

E depois:
* `docker-compose up`

O aplicativo estará disponível em:
* http://localhost:8000

Tenha certeza que ao visitar o endereço os serviços estejam carregados.

### Local:
Entra na pasta api com o Virtualenv ativado, versão
Python 3.6.0. Utilize os comandos
* `pip install -r requirements.txt`

Depois de instalado:
* `python manage.py makemigrations`,
* `python manage.py migrate`
* `python manage.py runserver`

Use o comando `npm run serve` e o aplicativo será iniciado.Adaptações
terão que ser feitas nas chamadas axios do aplicativo, especificando
o full path. O frontend estará disponível em:
* http://localhost:8080

### Informações
* Os primeiros commits são referentes ao desafio frontend.
* Os testes unitários estão em `v1_track/tests.py`
para roda-los use `python manage.py test` na pasta `api/`.

* O endpoint é `api/v1/tracks` e `api/v1/tracks/<track_id>/`,
API baseada no principio RESTFul, comandos
de List/Create/Delete disponíveis.
