
set -x

#static type checking
mypy app
#code formatter
black app --check
#sort imports alphabetically
isort --check-only app
#flake linter
flake8 app
