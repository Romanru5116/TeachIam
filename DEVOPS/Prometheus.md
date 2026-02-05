Prometheus Prometheus – это проект с открытым кодом, отвечающий за мониторинг и оповещение. Проект был выпущен в 2015 году.

У Прометея есть ряд особенностей:

Поддерживает гибкие языки запросов;
Имеет несколько режимов отображения и админ панели;
Данные хранятся и передаются по протоколу HTTP.

компоненты
картинка

Установка
Option 2: Production Setup with Docker Compose and Persistent Data 
For any long-term use, it is highly recommended to use a configuration file and persistent storage. 
1. Create a Prometheus configuration file 
Create a directory for your Prometheus setup and, inside it, a file named prometheus.yml. This basic configuration tells Prometheus to scrape its own metrics. 
mkdir prometheus-config
cd prometheus-config
nano prometheus.yml

Create a Docker Compose file 
In the same prometheus-config directory, create a file named docker-compose.yml. 
bash
nano docker-compose.yml
Add the following content:
yaml
version: '3.8'

services:
КОНФИГИ:
Файл конфигурации Prometheus (обычно с именем prometheus.yml) чаще всего находится в директории /etc/prometheus/ на Linux-системах. 
При установке из архива файл лежит в корне распакованной папки.
Если используется Docker, файл монтируется в контейнер, например, по пути /etc/prometheus/prometheus.yml. 
Основные пути и особенности:
Стандартная установка (Linux): /etc/prometheus/prometheus.yml.
 Конфиги обычно хранятся:
 Основные места хранения:
Конфигурация (prometheus.yml): /etc/prometheus/prometheus.yml.
Данные (TSDB): /var/lib/prometheus/ или /data. 
Для проверки точного пути, используемого запущенным экземпляром, можно выполнить команду:
ps aux | grep prometheus | grep config.file. 

Add the following content to prometheus.yml:

yaml
global:
  scrape_interval: 15s # How often to scrape targets
scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
   
. Run Prometheus
From within the prometheus-config directory, start the container in detached mode (in the background): 
bash
docker-compose up -d


he provided command line arguments are used to configure and run the Prometheus monitoring system. They define various system parameters and file locations: 
--config.file=/etc/prometheus/prometheus.yml: Specifies the path to the main configuration file that Prometheus uses to define scraping jobs, rules, and other settings.
--storage.tsdb.path=/prometheus: Sets the base directory where Prometheus stores its time-series database (TSDB) data on disk.
--web.console.libraries=/usr/share/prometheus/console_libraries and --web.console.templates=/usr/share/prometheus/consoles: These flags specify the locations for console libraries and templates, which are used for the experimental and historical web console functionality within Prometheus.
--web.enable-lifecycle: This flag enables the HTTP lifecycle endpoints (like /-/reload and /-/quit), allowing the configuration to be reloaded (by sending a SIGHUP or a POST request to the /reload endpoint) or the server to be shut down gracefully at runtime via HTTP requests, without needing to restart the process manually. 

литература
