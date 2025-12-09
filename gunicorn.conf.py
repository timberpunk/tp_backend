# Gunicorn configuration file for TimberPunk API

# Number of worker processes
workers = 4

# Worker class - uvicorn for async support
worker_class = "uvicorn.workers.UvicornWorker"

# Bind to this address
bind = "0.0.0.0:8000"

# Keep alive connections
keepalive = 120

# Timeout for workers
timeout = 120

# Logging
errorlog = "-"  # Log errors to stdout
accesslog = "-"  # Log access to stdout
loglevel = "info"

# Graceful timeout for workers
graceful_timeout = 30

# Maximum requests per worker before restart (prevents memory leaks)
max_requests = 1000
max_requests_jitter = 50
