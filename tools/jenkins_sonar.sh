#!/usr/bin/env bash
set -euo pipefail

report_root="${CI_REPORT_ROOT:-reports}"
scanner="$(command -v sonar-scanner || command -v pysonar || true)"

if [[ -z "$scanner" ]]; then
    echo "Neither sonar-scanner nor pysonar is available." >&2
    exit 1
fi

export SONAR_TOKEN="${SONAR_TOKEN:-${SONAR_AUTH_TOKEN:-}}"
if [[ -z "$SONAR_TOKEN" ]]; then
    echo "No SonarQube token was provided by Jenkins." >&2
    exit 1
fi

mkdir -p "$report_root/sonar"

"$scanner" \
    -Dsonar.projectKey=zurichsee_ha \
    -Dsonar.projectName="Zürichsee Home Assistant Integration" \
    -Dsonar.projectVersion="${VERSION:-0.0.0}-${COMMIT_HASH:-unknown}" \
    -Dsonar.python.version=3.14 \
    -Dsonar.sources=custom_components/zurichsee_ha \
    -Dsonar.tests=tests/unit,tests/ha \
    -Dsonar.python.coverage.reportPaths="$report_root/pytest/coverage.xml" \
    -Dsonar.python.xunit.reportPath="$report_root/pytest/pytest.xml"
