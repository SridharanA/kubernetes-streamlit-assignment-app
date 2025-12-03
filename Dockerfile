FROM python:3.9-slim

WORKDIR /app

COPY . /app/

RUN pip install streamlit pandas matplotlib ucimlrepo

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]