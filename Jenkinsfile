@Library('jenkins-shared-library@main') _

ciRepositoryDocumentationContract(
    scm: scm,
    agentLabel: 'klymene',
)

if (ciDocumentationOnlyShortcut(
    scm: scm,
    agentLabel: 'klymene',
    repository: [
        owner: 'derliebemarcus',
        name: 'homeassistant_zurichsee',
    ],
    github: [
        credentialId: 'github token',
        statusContext: 'Continuous Integration / Jenkins',
        title: 'Zürichsee Quality Gates',
    ],
)) {
    return
}

ciHomeAssistantIntegration(
    scm: scm,
    agentLabel: 'klymene',
    mainBranch: 'main',
    weeklyMutationCron: 'H H * * 6',
    repository: [
        owner: 'derliebemarcus',
        name: 'homeassistant_zurichsee',
    ],
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
                docker.io/rhysd/actionlint:latest "$workflow"
            done
        ''',
    ],
    mutation: [
        artifacts: 'reports/mutation/**,mutants/.mutmut-cache/**,.mutmut-cache',
    ],
    hassfest: [
        enabled: true,
    ],
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
    github: [
        credentialId: 'github token',
        publishStageChecks: true,
        publishFinalCheck: false,
        statusContext: 'Continuous Integration / Jenkins',
        title: 'Zürichsee Quality Gates',
    ],
    homeAssistant: [
        enabled: true,
    ],
)

def releaseStepName = ['ci', 'Change', 'sets', 'Release'].join('')
this.invokeMethod(releaseStepName, [[
    scm: scm,
    agentLabel: 'klymene',
    mainBranch: 'main',
    repository: [
        owner: 'derliebemarcus',
        name: 'homeassistant_zurichsee',
    ],
    asset: 'reports/pytest/zurichsee_ha.zip',
    packageFile: 'package.json',
    versionSyncCommand: 'npm run version:sync',
    stashName: 'ha-ci-artifact-pytest-coverage',
    autoMergePatch: true,
]] as Object[])
