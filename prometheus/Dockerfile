# Use an official Prometheus base image
FROM prom/prometheus

# Copy your configuration file into the container
COPY ccloud.yml /etc/prometheus/

# Specify the command to run when the container starts
CMD ["prometheus", "--config.file=/etc/prometheus/ccloud.yml"]
