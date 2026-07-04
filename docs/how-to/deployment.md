# Deployment

1. Jenkins validates Python quality, Home Assistant compatibility, security, and packaging.
2. Changesets maintains the version pull request and release intent.
3. A tagged release publishes the integration archive for HACS.

Documentation-only changes must never execute deployment or publication stages.
