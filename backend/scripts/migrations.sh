#!/usr/bin/env bash

set -e

echo "Run migrations.."
piccolo migrations forwards all
echo "Migrations applied!"

exec "$@"
