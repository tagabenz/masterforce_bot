#!/bin/bash
set -e

if [ "$ENV" = 'UNIT' ]; then
  echo "Running Unit Tests" # Запуск юнит-тестов
  exec python "test.py"
elif [ "$ENV" = 'DEV' ]; then
  echo "Running Development Server" # Запуск сервера для разработки
  exec python "start.py"
else
  echo "Running Production Server" # Запуск сервера для эксплуатации
  exec uwsgi --http 0.0.0.0:9090 --wsgi-file start.py --callable app --stats 0.0.0.0:9191
fi
