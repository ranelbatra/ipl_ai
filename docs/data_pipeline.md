# Production Data Ingestion Pipeline

## Architecture Diagram

![Data Pipeline](images/data_pipeline.png)

## Overview

The production data pipeline describes how a user request moves through the system before an AI-generated response is returned. Each stage ensures that data is validated, enriched, and processed efficiently.

## Pipeline Stages

### User Query
The user submits a request through the Streamlit interface.

### Input Validation
The backend verifies that the request is complete, valid, and safe to process.

### Data Cleaning
The input is standardized by removing unnecessary whitespace, correcting formatting, and normalizing player or team names.

### Intent Detection
The system determines whether the request should be handled by the AI Match Coach, AI Cricket Assistant, or Cricket Comparison Studio.

### Retrieve Match & Player Data
Relevant structured information is retrieved from PostgreSQL.

### Retrieve AI Context
Additional contextual information is retrieved from the Vector Database using semantic search.

### Prompt Builder
The user's request and retrieved data are combined into a structured prompt for the language model.

### LLM Gateway
The request is routed to the appropriate language model for inference.

### Generate AI Response
The selected language model generates the response using the provided context.

### Response Validation
The generated output is checked for formatting and consistency before being returned.

### Return Response
The validated response is displayed to the user through the Streamlit application.