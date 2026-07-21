# Enterprise System Architecture

## Architecture Diagram

![Enterprise Architecture](images/updated_genterprise_architecture.png)

## Overview

The enterprise architecture illustrates how the IPL Analytics Platform can evolve from a prototype into a scalable production system. The architecture separates the user interface, backend services, AI modules, databases, and cloud AI infrastructure to improve scalability, reliability, and maintainability.

## Components

### Users
Represents users interacting with the application through a web browser.

### Streamlit Frontend
Provides the graphical user interface where users can explore statistics, ask cricket-related questions, receive coaching suggestions, and compare players or teams.

### API Gateway
Acts as the single entry point for all incoming requests. It manages authentication, request routing, monitoring, and security before forwarding requests to the backend.

### FastAPI Backend
Implements the application's business logic, communicates with databases, prepares prompts for AI models, and coordinates all AI services.

### AI Match Coach
Analyzes match data to generate coaching recommendations, strategic insights, and match planning suggestions.

### AI Cricket Assistant
Provides conversational assistance by answering cricket-related questions and explaining statistics, rules, and match events.

### Cricket Comparison Studio
Generates statistical comparisons between players, teams, seasons, and matches using structured data and AI-generated insights.

### PostgreSQL
Stores structured application data including users, player statistics, match information, chat history, and saved analyses.

### Vector Database
Stores vector embeddings used for semantic search and Retrieval-Augmented Generation (RAG), allowing the AI to retrieve relevant cricket knowledge.

### Redis
Caches frequently accessed information to reduce response time and improve system performance.

### Worker Queue
Processes long-running AI tasks asynchronously without blocking user requests.

### LLM Gateway
Routes requests to one or more cloud-based language models while handling retries, monitoring, and model selection.

### Cloud LLMs
Represents external AI providers responsible for generating intelligent responses.