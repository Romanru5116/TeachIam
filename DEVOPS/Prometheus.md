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

литература
