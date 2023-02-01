# city-bike-app

run the app:
```docker-compose up```

run the elements individually
database:
```docker-compose up -d db```
python app:
```docker-compose up --build flask-app```

access database:
```docker exec -it city-bike-app-db-1 psql -U postgres```

stop and remove with volumes
```docker-compose down -v```