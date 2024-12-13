Автор: Крестьянова Елизавета
# CI/CD: Github Actions
## "Плохой" CI/CD файл
> Написать “плохой” CI/CD файл, который работает, но в нем есть не менее пяти “bad practices” по написанию CI/CD

[Написанный файл находится в этом репозитории](https://github.com/plida/itmo_devops-cloud/blob/master/.github/workflows/bad_example.yml).

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

[Написанный файл находится в этом репозитории](https://github.com/plida/itmo_devops-cloud/blob/master/.github/workflows/good_example.yml).

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

### 1. Указание :latest версии

Как и в работе с докерфайлами, указание последней версии того же Ubuntu приводит к нестабильности конфигурации. Лучше указать определённую версию, например, ubuntu-22.04, и тогда мы точно будем знать, что выход новой версии Убунту нам случайно зависимости пайплайна не поломает.

### 2. Имена шагов

В плохой версии файла имена шагам работ никак не прописывались, отчего в активностях можно найти шаг с именем "Run sudo apt-get update". В котором на самом деле ещё заложены установка пайтона и пайтеста. В целом по первым линиям блока не всегда легко понять, о чём шаг, и это некрасиво, поэтому мы им имена в хорошем файле дали. Теперь понятно: есть Checkout, есть установка пайтона, пайтеста и само проведение теста.

### 3. Использование defaults

Что деплой, что тест, работают в одной рабочей папке. Вместо того чтобы прописывать её каждый раз, можно просто отдельно вывести. И красиво выглядит, и легче будет менять общую папку при смене проекта. В целом реюз конфигов в CI/CD поощряется - сюда же можно отнести [использование extend и ярлыков](https://about.gitlab.com/blog/2020/10/01/three-yaml-tips-better-pipelines/).

### 4. Использование actions

В плохом файле мы устанавливали пайтон через `sudo apt-get install -y python3`, но в "Github actions" есть слово "actions", можно использовать и нужно: это рекомендует [документация гитхаба](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python#specifying-a-python-version). setup-python помогает обеспечить одинаковый процесс установки пайтона среди нескольких раннеров, к тому же через него его можно установить не только на линукс, но и на мак, и на виндоус.

### 5. Зависимость деплоя от выполнения теста

В созданном примере деплой и тест не очень то и связаны, но мы попробуем закрыть на это глаза и сказать, что нет, что бы там не было, нам нужна чёткая последовательность. Если в плохом пайплайне деплой и тест работали параллельно, то прописав у деплоя "needs: Test", мы эту зависимость создаём. Визуально заметно на скриншоте пайплайна, что работы шли поочерёдно. 

## Результаты

У нас получился приличный файл CI/CD, в котором благодаря оптимизации работы стали совершаться быстрее, чем в плохом пайплайне (хотя, конечно, отсутствие паралелльности приводит к большему ожиданию). Это была очень интересная работа для очень неизвестной темы.
