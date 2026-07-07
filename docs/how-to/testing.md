# Testing

Create the same project environment used by Jenkins:

```bash
bash tools/jenkins_prepare.sh
```

Run tests and static analysis through that environment:

```bash
.venv/bin/python -m pytest tests/unit tests/ha
.venv/bin/python -m ruff check .
.venv/bin/python -m ruff format --check .
.venv/bin/python -m mypy .
```

Jenkins runs these commands in the shared Python 3.14 Home Assistant integration CI
image. The image contains common CI tooling but no repository source or project
dependencies. `tools/jenkins_prepare.sh` installs `requirements-dev.txt` with
`constraints.txt` once, and the bootstrap stash restores `.venv` in parallel stages.
