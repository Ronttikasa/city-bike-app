# Helsinki City Bike App

### Building and running the app:

Download the journey datasets from 
- https://dev.hsl.fi/citybikes/od-trips-2021/2021-05.csv
- https://dev.hsl.fi/citybikes/od-trips-2021/2021-06.csv
- https://dev.hsl.fi/citybikes/od-trips-2021/2021-07.csv

and the station dataset from
- https://opendata.arcgis.com/datasets/726277c507ef4914b0aec3cbcfcbfafc_0.csv

Place them in the *data* directory at the root of the project.

(The dataset file names should be 2021-05.csv, 2021-06.csv, 2021-07.csv, Helsingin_ja_Espoon_kaupunkipyöräasemat_avoin.csv, respectively. Rename the files if needed.)

Build and run the app with Docker:
```docker-compose up```

### Importing the datasets

The app is now running at http://localhost:5000. Import the data by [voisko tehdä nappulat etusivulle jos kanta tyhjä?]


### Other useful commands

You can also run the database and Flask app individually.

database:
```docker-compose up -d db```
python app:
```docker-compose up --build flask-app```

Access database:
```docker exec -it city-bike-app-db-1 psql -U postgres```

Stop and remove volumes
```docker-compose down -v```