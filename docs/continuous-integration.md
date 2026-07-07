# Continuous integration

The root `Jenkinsfile` uses the shared runtime
`registry.home.siczb.de/siczb/homeassistant-integration-ci:3.14`.

Initialization runs `tools/jenkins_prepare.sh` once. It creates `.venv` from
`requirements-dev.txt` and `constraints.txt`, then Jenkins stashes the environment for
parallel stages. The repository no longer uses `python-ci:latest`.

The runtime uses `pullPolicy: always`, so each build resolves the current validated
`3.14` image published by the protected Maintenance main pipeline.

Existing quality, security, SonarQube, Coveralls, repository, and mutation gates remain
active. Mutation testing runs for pull requests, `main`, and the weekly schedule.
Containers preserve Jenkins workspace ownership through `--userns=keep-id`.
