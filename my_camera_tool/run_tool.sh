#!/bin/bash

PORT=8080

echo "Starting PHP web server on port $PORT..."
echo "Your local server will be accessible at: http://localhost:$PORT"
echo "To stop the server, press Ctrl+C."
echo "=========================================="

php -S 0.0.0.0:$PORT
