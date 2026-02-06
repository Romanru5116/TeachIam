Решаем задачи:
1 на локальной машине равзернуть кластер kubernetes дефолтный
2 настроить мониторингprometheus 
3 развернуть в кластере nginx

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

здесь должна быть картинка

Step 2: Defining the Docker Compose Configuration
-- пока не понимаю как- куча парметров

краткое описанеи компонентов
This Docker Compose setup wires together all the key components for a solid monitoring stack:

Prometheus handles time-series data collection and storage. It pulls metrics from exporters and other endpoints based on your configuration. The --web.enable-lifecycle flag lets you trigger config reloads without restarting the container.
Node Exporter collects low-level system metrics from the host—like CPU usage, memory, and disk stats. We're mounting /proc and /sys read-only so Prometheus can scrape accurate host metrics without affecting the system.
cAdvisor focuses on container-level metrics, offering insights into resource usage per container—handy when you’re running multiple services on the same host.
Grafana sits on top of Prometheus and provides a user-friendly interface to visualize your data. The provisioning folders (datasources and dashboards) ensure everything is set up automatically on first run.
Alertmanager receives alerts from Prometheus and routes them to the right place—Slack, PagerDuty, email, etc. Mounting the config from your local folder keeps it easy to tweak as your alerting needs evolve.

что к чему
volumes: Постоянное хранение данных, которые сохраняются после удаления контейнера. 
networks в docker-compose.yml — это раздел конфигурации, определяющий виртуальные сети для взаимодействия между контейнерами. Он позволяет объединять сервисы, изолировать их, настраивать DNS-имена и управлять сетевым трафиком внутри проекта. По умолчанию Compose создает одну сеть, подключая к ней все сервисы. 


Step 3: Configuring Prometheus
Create a prometheus.yml file in the prometheus directory:

steStep 4: Setting Up Alert Rules
Create an alert rules file at prometheus/rules/node_alerts.yml:p4:

Step 5: Configuring Alertmanager
Create a basic Alertmanager configuration in alertmanager/config.yml:

Step 6: Setting Up Grafana Dashboards
Configure Grafana to connect to Prometheus automatically by creating grafana/provisioning/datasources/datasource.yml:

Step 7: Performance Optimization for Production
For production deployments, optimize Prometheus for better performance:

ПРОВЕРКА ЧТО РАБОТАЕТ
ccess the monitoring interfaces:

Prometheus: http://localhost:9090
Grafana: http://localhost:3000 (login with admin/admin)
cAdvisor: http://localhost:8080
Alertmanager: http://localhost:9093

Результат:

[картинка GRAFAN ЗАПУСТИЛАСЬ!


Step 9: Monitoring Docker Containers

ПРИМЕЧАНИЯ:
версии Docker Compose (v1) с новыми версиями Docker Engine (24+), обычно проявляясь как KeyError: 'ContainerConfig'. Решения включают обновление до Docker Compose v2, использование команды docker compose (без дефиса) или удаление строки version: '...' из docker-compose.yml. 
Основные причины и способы решения:
Конфликт версий: Старая версия docker-compose (Python-версия) несовместима с новым API Docker.
Решение 1 (Рекомендуемое): Используйте обновленный плагин Docker Compose (v2), заменив в командах дефис на пробел: docker compose up -d вместо docker-compose up -d.
Решение 2: Удалите строку version: 'x.x' (например, version: '3') в начале вашего файла docker-compose.yml.
Решение 3: Обновите Docker Compose до последней версии. 

Документация
как развернуть https://last9.io/blog/prometheus-with-docker-compose/

собственно мониторинг https://habr.com/ru/companies/slurm/articles/516748/

