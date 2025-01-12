# MicroPython experiments

Micropython experiments with Arduino Nano 33 ble sense.

1. Install micropython on Arduino using
   the https://labs.arduino.cc/en/labs/micropython-installer
2. Compact the files in [libs/](libs/) using mpr
   
   
## Contributing

Please, see [CONTRIBUTING.md](CONTRIBUTING.md) for more details on:

- using [pre-commit](CONTRIBUTING.md#pre-commit);
- following the git flow and making good [pull requests](CONTRIBUTING.md#making-a-pr).

## Using this repository

You can create new projects starting from this repository,
so you can use a consistent CI and checks for different projects.

Besides all the explanations in the [CONTRIBUTING.md](CONTRIBUTING.md) file, you can use the docker-compose file
(e.g. if you prefer to use docker instead of installing the tools locally)

```bash
docker-compose run pre-commit
```

## Testing github actions

Tune the Github pipelines in [.github/workflows](.github/workflows/).

To speed up the development, you can test the pipeline with [act](https://github.com/nektos/act).
Installing `act` is beyond the scope of this document.

To test the pipeline locally and ensure that secrets (e.g., service accounts and other credentials)
are correctly configured, use:

 ```bash
 # Run a specific job in the pipeline
 act -j test -s CI_API_TOKEN="$(cat gh-ci.json)" \
      -s CI_ACCOUNT=my-secret-account
 ```
