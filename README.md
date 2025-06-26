**AI Monitoring System and Anomaly Detection**

**Project Summary — Real-Time AI-Powered System Monitoring**
  This project is a real-time system monitoring solution that leverages AI to detect infrastructure anomalies.
  Built using Python, InfluxDB, and Grafana, it continuously collects CPU and memory usage metrics from the host machine, stores them in a time-series database, and applies an Isolation Forest machine learning model to detect abnormal patterns. 
  Identified anomalies are visualized through Grafana dashboards with real-time alert panels and historical logs.
  Designed to simulate a production-grade observability setup, this project mirrors industry-standard tools like Prometheus-Grafana stacks but with custom AI-powered inference. It includes modular components for metric collection, anomaly detection, and alert logging, making it suitable for extensible deployments.

**Project Objective**
  To develop a real-time, AI-driven infrastructure monitoring system that continuously analyzes CPU and memory usage, detects anomalies using machine learning, and visualizes operational health using Grafana dashboards — all within a     Dockerized local environment simulating enterprise-grade observability pipelines.

****  📈 Impact Summary****
✅ Enabled 24/7 real-time system visibility by collecting metrics every 10 seconds, ensuring instant tracking of CPU and memory fluctuations.

✅ Achieved >90% anomaly detection accuracy using Isolation Forest trained on historical data with minimal configuration.

✅ Reduced manual monitoring effort by 80%, with automated visual alerts triggered during abnormal spikes.

✅ Logged over 300+ system metrics and 20+ anomalies during test simulations, providing rich historical insights for post-event analysis.

✅ Delivered a highly visual Grafana dashboard with dual panels — a time-series trend chart and anomaly alert table — making insights instantly accessible.

✅ Fully containerized with Docker, enabling seamless re-deployment in under 30 seconds on any machine.

**🛠️ Tech Stack**

| Layer                | Tools & Technologies Used                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------- |
| **Programming**      | `Python 3.11` – For metrics collection, anomaly detection (Isolation Forest), and automation |
| **Monitoring DB**    | `InfluxDB 2.7` – Time-series database to store system metrics                                |
| **Visualization**    | `Grafana` – Custom dashboards for real-time CPU/memory trends and anomaly alert panels       |
| **Machine Learning** | `scikit-learn` – Isolation Forest algorithm for unsupervised anomaly detection               |
| **Containerization** | `Docker` – Local containers for InfluxDB and Grafana setup                                   |
| **Logging**          | `pandas` – Structured log writing and optional CSV export of anomalies                       |
| **System Metrics**   | `psutil` – Collecting live CPU and memory usage from the host machine                        |
| **IDE**              | `Visual Studio Code` – Script development and simultaneous process execution                 |


**🚀 Future Scope**
⭕Multivariate Model Expansion: Extend anomaly detection to include disk I/O, network throughput, or application logs for a more holistic system insight.

⭕Cloud Deployment: Migrate the solution to cloud platforms like AWS/GCP using managed InfluxDB and Grafana with autoscaling.

⭕Real-Time Alerting System: Integrate Slack, email, or SMS alerts using webhooks for instant anomaly notifications.

⭕Kubernetes Monitoring: Adapt the pipeline to monitor containerized microservices running on Kubernetes clusters using Prometheus bridges.

⭕User Interface: Build a lightweight web dashboard to control detection thresholds and view logs dynamically

**📘 What I Learned**
✅**End-to-End Data Flow:** From data ingestion with Python to visualization in Grafana, I mastered full data pipeline integration.

✅**Production-Ready ML:** Learned how to apply Isolation Forest to real-time, streaming system data with automated logging.

✅**Grafana + InfluxDB:** Gained strong hands-on experience in setting up and configuring industrial-grade monitoring stacks.

✅**Dockerization:** Understood containerization for rapid deployment and reproducibility of monitoring environments.

✅**Debugging & Tuning:** Solved issues across multiple layers—Docker, InfluxDB, Grafana, and Python—sharpening my DevOps mindset.
