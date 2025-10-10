#!/bin/bash

# Load Testing Script for Feedback System
# Usage: ./load_test.sh [URL] [connections] [duration]

URL=${1:-"https://feedbacksystem-dcaq.onrender.com/"}
CONNECTIONS=${2:-5000}
DURATION=${3:-30}

echo "Load Testing Configuration:"
echo "URL: $URL"
echo "Concurrent Connections: $CONNECTIONS"
echo "Duration: $DURATION seconds"
echo "Press Ctrl+C to stop early..."
echo

# Function to cleanup background processes
cleanup() {
    echo "Stopping load test..."
    kill 0
    exit 0
}

# Trap SIGINT (Ctrl+C)
trap cleanup SIGINT

# Start time
start_time=$(date +%s)

# Function to make requests
make_request() {
    local end_time=$((start_time + DURATION))
    local request_count=0
    
    while [ $(date +%s) -lt $end_time ]; do
        curl -s -w "%{http_code},%{time_total}\n" "$URL" -o /dev/null &
        ((request_count++))
        
        # Small delay to prevent overwhelming the system
        sleep 0.001
    done
    
    echo "Process completed $request_count requests"
}

echo "Starting load test with $CONNECTIONS concurrent connections..."
echo "Test will run for $DURATION seconds"
echo

# Start concurrent processes
for i in $(seq 1 $CONNECTIONS); do
    make_request &
    
    # Progress indicator every 100 processes
    if (( i % 100 == 0 )); then
        echo "Started $i processes..."
    fi
    
    # Small delay between process starts to prevent system overload
    sleep 0.01
done

echo "All processes started. Waiting for completion..."

# Wait for all background processes to complete
wait

end_time=$(date +%s)
total_time=$((end_time - start_time))

echo
echo "Load test completed!"
echo "Total time: ${total_time}s"
echo "Target duration: ${DURATION}s"
echo "Concurrent connections: $CONNECTIONS"
