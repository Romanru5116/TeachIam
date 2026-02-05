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
docker  compose развкрнут
структур под проект создать
Развернуть prometheus^
ep-by-Step Guide to Monitoring Prometheus with Docker
Step 1: Creating the Project Structure
Start by setting up a well-organized directory structure:

# Create project directory
mkdir prometheus-monitoring
cd prometheus-monitoring

# Create subdirectories for configurations
mkdir -p prometheus/rules alertmanager grafana/provisioning/{datasources,dashboards}
This directory structure helps keep things clean and manageable as your monitoring setup grows.

prometheus/rules/ is where you’ll store custom alerting and recording rules.
alertmanager/ will hold the Alertmanager config file, including routing and notification settings.
grafana/provisioning/ is split into datasources/ and dashboards/ to support automated Grafana setup—so your dashboards and data sources load automatically on startup.
Organizing your files this way makes it easier to version-control, update configs independently, and troubleshoot issues faster.


Документация
мониторинг https://habr.com/ru/companies/slurm/articles/516748/

