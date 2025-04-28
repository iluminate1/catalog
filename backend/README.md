## Run Locally

Setup .env
```bash
  mv .env.template .env
```

Install dependencies
```bash
  uv sync
```

Migrations
```bash
  uv run piccolo migrations forwards all
```

Create super user
```bash
  uv run piccolo user create
```

Start the server
```bash
  uv run catalog/main.py
```

