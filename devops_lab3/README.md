Автор: Крестьянова Елизавета
# CI/CD: Github Actions
## "Плохой" CI/CD файл
> Написать “плохой” CI/CD файл, который работает, но в нем есть не менее пяти “bad practices” по написанию CI/CD

[Написанный файл находится в этом репозитории](https://github.com/plida/itmo_devops-cloud/blob/ci-cd-test/.github/workflows/bad_example.yml).

```
name: CI-CD_devoops 

on: 
  push:
    branches: [ ci-cd-test ]

jobs:
  Test:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: ./devops_lab3
    steps:
      - uses: actions/checkout@v4
      - run: |
          sudo apt-get update
          sudo apt-get install -y python3
          pip install pytest
      - run: |
          pytest test_main.py
  Deploy:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: ./devops_lab3
    steps: 
      - uses: actions/checkout@v4
      - run: |
          sudo apt-get update
          sudo apt-get install -y python3
      - run: |
          echo "😈 BAD EXAMPLE"
          python helloworld.py
          
```

**Успешное выполнение:**

![alt text](<../images/cicdbad1.png>)

## "Хороший" CI/CD файл
> Написать “хороший” CI/CD, в котором эти плохие практики исправлены

[Написанный файл находится в этом репозитории](https://github.com/plida/itmo_devops-cloud/blob/ci-cd-test/.github/workflows/good_example.yml).

```
name: CI-CD_devOPs 

defaults:
      run:
        working-directory: ./devops_lab3

on: 
  push:
    branches: [ ci-cd-test ]

jobs:
  Test:
    runs-on: ubuntu-22.04
    steps:
      - name: Checkout
        uses: actions/checkout@v4
  
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
  
      - name: Install pytest
        run: |
          pip install pytest
          
      - name: Launch Test
        run: |
          pytest test_main.py
          
  Deploy:
    needs: Test
    runs-on: ubuntu-22.04
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Deployment
        run: |
              echo "😇 GOOD EXAMPLE"
              python helloworld.py
```

**Успешное выполнение:**

![alt text](<../images/cicdgood1.png>)

## Описание плохих практик и их исправление

> В Readme описать каждую из плохих практик в плохом файле, почему она плохая и как в хорошем она была исправлена, как исправление повлияло на результат
