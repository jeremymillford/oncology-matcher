# oncology-matcher
mock example for starting mycmie testing

oncology-matcher/
gene-app/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── .env
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── database.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── genes.py
├── frontend/
│   ├── Dockerfile
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   ├── package.json
│   ├── public/
│   │   ├── index.html
├── docker-compose.yml

docker exec -it postgres_server psql -U user -d db_name