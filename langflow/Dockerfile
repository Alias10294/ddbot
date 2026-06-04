FROM langflowai/langflow:latest

WORKDIR /app

RUN mkdir -p /app/flows

COPY flows/ /app/flows/

ENV LANGFLOW_LOAD_FLOWS_PATH=/app/flows
ENV LANGFLOW_AUTO_LOGIN=True
ENV LANGFLOW_HOST=0.0.0.0
ENV LANGFLOW_PORT=7860

EXPOSE 7860