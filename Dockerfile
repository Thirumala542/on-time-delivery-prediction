# Step 1: Use a base Python image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements.txt (if you want to use it to install dependencies)
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code
COPY app/ app/
COPY tests/ tests/

# Step 6: Expose the FastAPI port (default: 8000)
EXPOSE 8000

# Step 7: Command to run the FastAPI app using uvicorn
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
