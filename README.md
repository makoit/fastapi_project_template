# fastapi_project_template

Base template for fastapi projects. Templates includes example endpoints, schemas & unit tests.

## project structure

Optional folders can be deleted if not required.

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
