# fastapi_project_template

Base template for fastapi projects. Templates includes example endpoints, schemas & unit tests.

## project structure

- optional folders can be deleted if not required
- in the main folder can be found config example & docker-compose file for local dev deployment

```
├───scripts (includes useful shell scripts)
└───src
    ├───app (python code)
    │   ├───api (api endpoints)
    │   │   └───v1 (version 1 of the api)
    │   │       └───endpoints
    │   ├───core (core functionalities and configs)
    │   ├───db (optional: db access if required)
    │   │   ├───crud
    │   │   └───init
    │   ├───models (internal api data models if required)
    │   ├───schemas (pydantic schemas for api payload)
    │   ├───tests (unit tests)
    │   │   ├───api (api endpoint tests)
    │   │   │   └───v1
    │   │   ├───db (optional: database specific tests)
    │   │   ├───postman (postman test collection)
    │   │   └───utils (test utils)
    │   └───utils (util functionality for app)
    └───scripts (useful shell scripts)
```

## app config

- `.env.example` file shows example for `.env` file
- modify example file to your needs and change file name to .env
- `.env` file will not be commited to your repo

## run app local for dev

Deployment is actually based on docker-compose for local dev. Execute the commands on the same folder level where the docker-compose file is located.
App runs in docker container with [uvicorn](https://www.uvicorn.org/). Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

Note: This is only for local dev mode. In docker-compose file the source code folder is mounted to the docker container and the uvicorn folder is set on reload if file changes in the source code folder occur. So after code changes you don't have to rebuild the complete container which is really helpful for dev purpose.

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

## lint code - static analysis of source code

for code linting following deps are required:

- [mypy](https://mypy.readthedocs.io/en/stable/introduction.html) (static type checking)
- [flake8](https://pypi.org/project/flake8/) (verifies pep8)
- [black](https://pypi.org/project/black/) (code formatter - check mode)
- [isort](https://pypi.org/project/isort/) (sort imports - check mode)

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

- [autoflake](https://pypi.org/project/autoflake/) (removes unused imports and unused variables from Python code)
- [black](https://pypi.org/project/black/) (code formatter)
- [isort](https://pypi.org/project/isort/) (sort imports)

(install them globally or in a local python env)

navigate to folder

```sh
cd /src/scripts
```

```sh
./format.sh
```

---

## To-Do List:

- [x] add poetry for deps management (dev deps and prod deps)
- [x] add postman collection
- [ ] add branch with auth/api_key
- [ ] add branch for deploy/kubernetes
