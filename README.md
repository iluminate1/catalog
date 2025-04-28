# Каталог оборудования

Каталог содержит иерархический перечень оборудования, имеющийся на 
предприятии. Оборудование делится на различные типы и распределено по цехам и
площадкам. Разные типы оборудования имеют различных набор характеристик. Для
некоторых единиц оборудования имеются скан-копии их паспортов. Пользователь
должен иметь возможности поиска необходимого оборудования по различным
характеристикам. Должна быть возможность добавления, изменения и удаления
оборудования в каталоге.



## Stack
Backend -> [README](https://github.com/iluminate1/catalog/blob/main/backend/README.md):
- litestar
- piccolo orm
- piccolo admin
Frontend -> [README](https://github.com/iluminate1/catalog/blob/main/frontend/README.md): 
- Vue3
- PrimeVue
- Vue Router
- Pinia
## Run Locally

Clone the project

```bash
  git clone git@github.com:iluminate1/catalog.git
```

Go to the project directory

```bash
  cd catalog
```

Run project

```bash
  docker compose up -d 
```

