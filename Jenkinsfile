@Library('jenkins-shared-library@main') _

ciRepositoryPipeline(
    profile: 'homeassistant-integration',
    repository: [
        provider: 'forgejo',
        owner: 'siczb',
        name: 'homeassistant_zurichsee',
    ],
    scmStatus: [
        context: 'Continuous Integration / Jenkins',
        title: 'Zürichsee Quality Gates',
        credentialId: 'forgejo',
        transport: 'api',
    ],
    features: [
        documentationOnly: [enabled: true],
        repositoryDocumentation: [enabled: true],
    ],
    profileConfig: [
        mainBranch: 'main',
        weeklyMutationCron: 'H H * * 6',
        componentPath: 'custom_components/zurichsee_ha',
        manifestPath: 'custom_components/zurichsee_ha/manifest.json',
        pythonVersion: '3.14',
        virtualEnvironment: '.venv',
        pythonCommand: '.venv/bin/python',
        requirementsFile: 'requirements-dev.txt',
        constraintsFile: 'constraints.txt',
        testPaths: ['tests/unit', 'tests/ha'],
        coverageFloor: 97.1,
        reportRoot: 'reports',
        prepareCommand: 'chmod 700 tools/jenkins_prepare.sh && tools/jenkins_prepare.sh',
        commands: [
            pytest: '''
                chmod 700 tools/jenkins_python_tasks.sh &&
                  tools/jenkins_python_tasks.sh pytest
            ''',
            ruffLint: '''
                chmod 700 tools/jenkins_python_tasks.sh &&
                  tools/jenkins_python_tasks.sh ruff-lint
            ''',
            ruffFormat: '''
                chmod 700 tools/jenkins_python_tasks.sh &&
                  tools/jenkins_python_tasks.sh ruff-format
            ''',
            mypy: '''
                chmod 700 tools/jenkins_python_tasks.sh &&
                  tools/jenkins_python_tasks.sh mypy
            ''',
            translations: '''
                chmod 700 tools/jenkins_python_tasks.sh &&
                  tools/jenkins_python_tasks.sh translations
            ''',
            pipAudit: '''
                chmod 700 tools/jenkins_python_tasks.sh &&
                  tools/jenkins_python_tasks.sh pip-audit
            ''',
            mutation: '''
                chmod 700 tools/jenkins_python_tasks.sh &&
                  tools/jenkins_python_tasks.sh mutation
            ''',
            dependencyConsistency: '''
                chmod 700 tools/jenkins_python_tasks.sh &&
                  tools/jenkins_python_tasks.sh dependency-consistency
            ''',
            codeql: 'chmod 700 tools/jenkins_codeql.sh && tools/jenkins_codeql.sh',
            sonar: 'chmod 700 tools/jenkins_sonar.sh && tools/jenkins_sonar.sh',
            actionlint: '''
                workflow_files="$(
                  find .forgejo/workflows -type f -name '*.yml' -print
                  find .forgejo/workflows -type f -name '*.yaml' -print
                )"
                test -n "$workflow_files"
                echo "$workflow_files" | while IFS= read -r workflow; do
                  podman run --rm -v "$PWD:/repo:z" -w /repo \
                    docker.io/rhysd/actionlint:latest -ignore forgejo "$workflow"
                done
            ''',
        ],
        mutation: [
            artifacts: 'reports/mutation/**,mutants/.mutmut-cache/**,.mutmut-cache',
        ],
        hassfest: [enabled: true],
        sonar: [
            enabled: true,
            server: 'SonarQube',
            projectKey: 'zurichsee_ha',
            projectName: 'Zürichsee Home Assistant Integration',
            timeoutMinutes: 15,
        ],
        coveralls: [
            enabled: true,
            file: 'reports/pytest/coverage.xml',
            credentialId: 'Coveralls',
            runtime: 'host',
        ],
        repositoryChecks: [
            commitMessageScript: 'tools/check_commit_messages.py',
            releaseNoteScript: 'tools/check_release_notes.py',
            changelog: 'CHANGELOG.md',
        ],
        security: [
            gitleaks: [enabled: true],
            trivy: [enabled: true],
            codeql: [
                enabled: true,
                toolName: 'codeql',
                toolPath: 'codeql',
                languages: ['python'],
            ],
            osv: [enabled: true],
            actionlint: [enabled: true],
        ],
        homeAssistant: [enabled: true],
        release: [
            enabled: true,
            provider: 'forgejo',
            asset: 'reports/pytest/zurichsee_ha.zip',
            packageFile: 'package.json',
            versionSyncCommand: 'npm run version:sync',
            stashName: 'ha-ci-artifact-pytest-coverage',
            credentialId: 'forgejo',
            autoMergePatch: true,
        ],
    ],
)
