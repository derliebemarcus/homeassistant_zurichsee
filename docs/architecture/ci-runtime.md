# CI runtime

The integration pipeline uses the shared Python 3.14 image. Project requirements and
constraints remain in this repository. Initialization creates `.venv` once and reuses
it in all validation stages.
