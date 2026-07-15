# Continuous integration

The root `Jenkinsfile` is a declarative entry point for the central
`homeassistant-integration` profile from `jenkins-shared-library@main`.

The profile uses the validated runtime
`registry.home.siczb.de/siczb/homeassistant-integration-ci:3.14`. Initialization runs
`tools/jenkins_prepare.sh`, creates `.venv` from `requirements-dev.txt` and
`constraints.txt`, and makes the prepared environment available to subsequent stages.

Quality, security, SonarQube, Coveralls, repository, Home Assistant, mutation, and
release gates are implemented by the shared library. Stage groups run sequentially by
default; parallel execution requires an explicit profile opt-in. Mutation testing runs
for pull requests, `main`, and the weekly schedule.

Forgejo is the authoritative SCM provider. Jenkins publishes commit states through the
Forgejo API, validates workflows under `.forgejo/workflows/`, and delegates release
creation to Forgejo. CodeQL analyzes Python; Forgejo workflows are checked separately by
Actionlint in Forgejo compatibility mode.

Repository Rules require single-line commit messages to start with one of `add:`,
`change:`, `deprecate:`, `remove:`, `fix:`, `build:`, or `chore:`.

Documentation-only changes are classified before the full profile starts. Repository
documentation is validated through the central documentation contract.

The pull-request build validates the migration without publishing a release. The first
protected `main` build after merge is the final acceptance check for the release path.
