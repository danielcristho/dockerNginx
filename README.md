# simple Nginx reverse proxy  on Docker 

### NB: generate certificate&key
```yml
$ mkdir proxy/ssl && cd proxy/ssl
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout site1.key -out site1.crt
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout site2.key -out site2.crt
```
### create

```yml
$ docker-compose build
```
### run
```yml
$ docker-compose run -d
```