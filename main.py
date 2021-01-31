import os


source_branch = os.getenv('SOURCE_BRANCH')
latest_version = os.getenv('LATEST_VERSION')

elements = latest_version.split(sep='.')

if len(elements) < 3:
    exit(f'Unexpected version string "{latest_version}".')
else:
    try:
        major = int(elements[0])
        minor = int(elements[1])
        patch = int(elements[2])
    except ValueError as exception:
        exit(f'Unexpected element "{exception.args[1]}" in version string "{latest_version}".')

new_version = ''
if source_branch.lower().startswith(('major/', 'feature-major/')):
    new_version = f'{major + 1}.0.0'
elif source_branch.lower().startswith(('minor/', 'feature/', 'feature-minor/')):
    new_version = f'{major}.{minor + 1}.0'
elif source_branch.lower().startswith(('bugfix/', 'hotfix/')):
    new_version = f'{major}.{minor}.{patch + 1}'
else:
    exit(f'Unexpected source branch name "{source_branch}".')

print(new_version)
