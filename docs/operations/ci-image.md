# CI image operations

The pipeline consumes `homeassistant-integration-ci:3.14`. Dependency resolution uses
`requirements-dev.txt` and `constraints.txt`. Problems in those files are corrected in
this repository; missing shared tools are corrected in the maintenance image.
