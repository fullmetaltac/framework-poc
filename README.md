### Usefull commands

1. Code formatting
```
black .
```

1. Remove unused imports
```
autoflake --in-place --remove-all-unused-imports -r framework tests
```

1. Git cleanup
```shell
git clean -ndx -e venv/ -e .env
git clean -fdx -e venv/ -e .env
```

1. Pre-commit
```
pre-commit install
pre-commit run --all-files
```

1. Add __init__.py recursively
```
find . -type d -exec touch {}/__init__.py \;
```

1. Skip cheks
```python
# pylint: disable=R1705
# type: ignore[attr-defined]
```

1. Squash history
```
git checkout --orphan latest
git add -A
git commit -m "Initial commit (history squashed)"
git branch -D main
git branch -m main
git push -f origin main
```
