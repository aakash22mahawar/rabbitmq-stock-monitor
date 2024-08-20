## Real-Time Stock Price Monitoring with FastAPI and RabbitMQ
In this project, I developed a real-time stock price monitoring system using Python, FastAPI, and RabbitMQ. The goal was to create a dynamic web application that continuously updates stock prices without manual page refreshes.

## Project Agenda
- Real-Time Data Retrieval: Fetch stock prices for Apple Inc. from an hidden API using network tab.
- Asynchronous Data Processing: Use RabbitMQ to manage and process stock data in real-time.
- Dynamic Web Display: Build a web interface that automatically refreshes to display the latest stock prices.

## Solution
FastAPI: Implemented a FastAPI application to serve the web interface and API endpoints. It provides:

- An endpoint (/get-stock-price) to fetch real-time stock data.
- An endpoint (/send-stock-price) to trigger data fetching and processing through RabbitMQ.
- RabbitMQ: Utilized RabbitMQ for asynchronous message handling, ensuring smooth background processing of stock price data.
- Created a index.html page that fetches and displays stock data every 30 seconds using JavaScript. This approach eliminates the need for manual page refreshes, offering a seamless user experience.
- This setup demonstrates the effective use of modern web technologies and message queuing systems to build a responsive and efficient real-time data monitoring application.

## Run the App
   ```bash
   uvicorn app:app --reload
