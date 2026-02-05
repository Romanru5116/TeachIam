на локальной машине равзернуть кластер
настроить мониторинг
задеплоить готовое ПО

на 02.02:
kube развернут в дефолтном конфиге
прометеус развернут
при сборке prometheus сыпет ошибками  docker compose

ставим docker compose
офф инуструкция отсюда
Docker Desktop (Recommended)
The easiest and recommended way to get Docker Compose is to install Docker Desktop.

Docker Desktop includes Docker Compose along with Docker Engine and Docker CLI which are Compose prerequisites.

Docker Desktop is available for:
Docker Compose is by installing Docker Desktop. It includes Docker Engine, Docker CLI, and Docker Compose as part of the package for Windows, macOS, and Linux. The modern command is docker compose (with a space), not the legacy docker-compose (with a hyphen). 
В итоге нашел инструкцию как постаивть  докер плагин
https://www.google.com/search?q=docker+compose+insstall&oq=docker+compose+insstall&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDY1MjlqMGo3qAIIsAIB&sourceid=chrome&ie=UTF-8

0502
продолжаем разворачивание docker compose Recommended Method: Docker Desktop


Документация
мониторинг https://habr.com/ru/companies/slurm/articles/516748/
