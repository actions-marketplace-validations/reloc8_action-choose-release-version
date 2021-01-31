# Choose New Release Version

A Github Action to decide the new release version based on the merged branch name.

May be used on a merged pull request event to decide the next release version based on the merged branch name:
- Next version is a new Major if source branch starts with `major/` or `feature-major/`.
- It's a new Minor if source branch starts with `minor/`, `feature-minor/`, or `feature/`.
- It's a new Patch if source branch starts with `bugfix/` or `hotfix/`.

### Examples

1. Latest version is `4.8.15` and source branch is `major/new-backend-api`:
    
    New release version is `5.0.0`.
    
2. Latest version is `4.8.15` and source branch is `minor/add-request-field`:

    New release version is `4.9.15`.
    
3. Latest version is `4.8.15` and source branch is `bugfix/blue-screen`:

    New release version is `4.8.16`.

## Usage

```
# On a closed pull request:
on:
  pull_request:
    types: [closed]
    branches: 
      - master

jobs:
  job-name:
    
    # Avoid pull requests that are closed but not merged:
    if: github.event.pull_request.merged
    
    runs-on: ubuntu-latest
    steps:

      # This step is required:
      - uses: actions/setup-python@v2
        with:
          python-version: 3.7

      - name: Choose new release version
        id: choose-release-version
        uses: reloc8/action-choose-release-version@1.0.0
        with:
          source-branch: 'major/new-backend-api'
          latest-version: '4.8.15'

      - name: Test
        run: echo ${{ steps.choose-release-version.outputs.new-version }}
``` 
