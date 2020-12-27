# fastapi_project_template

Base template for fastapi projects. Templates includes example endpoints, schemas & unit tests.

## project structure

Optional folders can be deleted if not required.

- scripts (includes useful shell scripts)
- src
  - app (includes python code)
    - api (This module includes the api endpoints)
      - api_v1 (includes the version 1 of the api)
    - core (This module includes core functionalities for the app)
    - db [optional] (This module includes database access)
    - models [optional] (This module includes the internal api data models e.g. database data models for sql or no-sql databases)
    - schemas (This module includes pydantic schemas to define the properties and types to validate some payload)
    - tests
      - api (includes the api endpoint tests)
      - db [optional] (includes the database specific tests)
      - postman (includes postman collection)
      - utils (includes tests for utils)
    - utils (This module include util functionality.)
  - scripts (includes useful shell scripts)

├───scripts
└───src
├───app
│ ├───api
│ │ └───v1
│ │ └───endpoints
│ ├───core
│ ├───db
│ │ ├───crud
│ │ └───init
│ ├───models
│ ├───schemas
│ ├───tests
│ │ ├───.pytest_cache
│ │ │ └───v
│ │ │ └───cache
│ │ ├───api
│ │ │ └───v1
│ │ ├───db
│ │ ├───postman
│ │ └───utils
│ └───utils
├───htmlcov
└───scripts

## app config

- `.env.example` file shows example for `.env` file
- modify example file to your needs and change file name to .env
- `.env` file will not be commited to your repo

## run app local for dev

Deployment is actually based on docker-compose for local dev. Execute the commands on the same folder level where the docker-compose file is located.

### build docker image:

```sh
scripts/build.sh
```

### run app in container

```sh
scripts/run.sh
```

### build, run app in container & run unit tests

```sh
scripts/test.sh
```

info: html based test coverage report will be saved after run in `src/app/htmlcov`

---

## api documentation

- swagger documentation find in local dev env at: http://localhost:8000/docs

---

## lint code

for code linting following deps are required:

- [mypy](https://mypy.readthedocs.io/en/stable/introduction.html)
- [black](https://pypi.org/project/black/)
- [isort](https://pypi.org/project/isort/)
- [flake8](https://pypi.org/project/flake8/)

(install them globally or in a local python env)

navigate to folder

```sh
cd /src/scripts
```

lint your code

```sh
./lint.sh
```

---

## format code

for code formatting following deps are required:

- [autoflake](https://pypi.org/project/autoflake/)
- [black](https://pypi.org/project/black/)
- [isort](https://pypi.org/project/isort/)

(install them globally or in a local python env)

navigate to folder

```sh
cd /src/scripts
```

```sh
./format.sh
```

---

To-Do List:

- [ ] add poetry for deps management (dev deps and prod deps)
- [ ] add postman collection
- [ ] refactor linting and formatting
- [ ] add branch with auth/api_key
