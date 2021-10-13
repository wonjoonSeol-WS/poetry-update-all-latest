This script updates all pyproject.toml packages to the latest version, 
while ensuring --dev option.

First, run:
```
poetry update
```
To update your packages.

Then use the following command to see any major version updates:
```
poetry show --outdated
```

Check each package changelog, if you are happy with all changes run:

```
poetry-update-all
```

Run tests to check any breaking changes.
You might need to run this multiple times if you encounter dependency errors. (SolverProblemError)
