yandex-conqueror
================

Swagger dostępny na https://yandex.henrietta.com.pl/apidocs

Lista [kontrybutorów](CONTRIBUTORS.md) dostępna w osobnym pliku.

Ways to run this repo?
======================

A a Docker container as a backend with a Cassandra runner.

To run the scraper:

```bash
python -m conqueror.scraper <apikey> <amountOfRequestsToDo>
```

To run the actual bot

```bash
python -m conqueror <yandex login> <yandex password>
```

The bot will choose 10 Russian cities and continue on to spread our propaganda.
