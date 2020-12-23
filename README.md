# fastapi_project_template

Base template for fastapi projects

## project structure

- scripts (includes useful shell scripts)
- src
  - app (includes python code)
    - api (This module includes the api endpoints)
      - api_v1 (includes the version 1 of the api)
    - core (This module includes core functionalities for the app)
    - db [optional] (This module includes database access)
    - models (This module includes the internal api data models e.g. database data models for sql or no-sql databases)
    - schemas (This module includes pydantic schemas to define the properties and types to validate some payload)
    - tests
      - api (includes the api endpoint tests)
      - db [optinal] (includes the database specific tests)
      - postman (includes postman collection)
      - utils (includes tests for utils)
    - utils (This module include util functionality.)
  - scripts (includes useful shell scripts)

## app config

- `.env.example` file shows example for `.env` file
- modify example file to your needs and change file name to .env
- `.env` file will not be commited to your repo

## run app local for dev

Deployment is actually based on docker-compose for local dev. Execute the commands on the same folder level where the docker-compose file is located.

### start app and mongo:

(run first time container are build, next time run this command container will not be build)

```sh
docker-compose up
```

### rebuild container:

```sh
docker-compose build --no-cache
```

### run after rebuild:

```sh
docker-compose down && docker-compose up
```

---

## api documentation

- swagger documentation find in local dev env at: http://localhost:8000/docs

---

## lint code

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

navigate to folder

```sh
cd /src/scripts
```

```sh
./format.sh
```

---

## testing code

```sh
cd /src/scripts
```

```sh
./test.sh
```
