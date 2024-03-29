# Helsinki City Bike App

A pre-assignment for Solita Dev Academy, this app lets you view data about city bike stations and journeys in the Helsinki and Espoo area. The technologies used are Python/Flask for the app and PostgreSQL for the database.

### Building and running the app:

Download the journey datasets from 
- https://dev.hsl.fi/citybikes/od-trips-2021/2021-05.csv
- https://dev.hsl.fi/citybikes/od-trips-2021/2021-06.csv
- https://dev.hsl.fi/citybikes/od-trips-2021/2021-07.csv

and the station dataset from
- https://opendata.arcgis.com/datasets/726277c507ef4914b0aec3cbcfcbfafc_0.csv

Place them in the *data* directory at the root of the project.

(The dataset file names should be 2021-05.csv, 2021-06.csv, 2021-07.csv, Helsingin_ja_Espoon_kaupunkipyöräasemat_avoin.csv, respectively. Rename the files if needed.)

Build and run the app and start the database with Docker: ```docker-compose up```

### Importing the datasets

The app is now running at http://localhost:5000. The datasets are imported to the database automatically when the localhost address is visited for the first time. This will take a while as the datasets a quite large.

### Running tests

Run unit tests: ```poetry run invoke test```

E2E tests are written using RobotFramework. To run the tests, make sure you have Chrome and [chromedriver](https://ohjelmistotuotanto-hy.github.io/chromedriver_asennusohjeet/) installed. With the app running, run E2E tests in another terminal: ```poetry run invoke robot```

### Other useful commands

You can also run the database and Flask app individually.

database:
```docker-compose up -d db```

python app:
```docker-compose up --build flask-app```

Access database:
```docker exec -it city-bike-app-db-1 psql -U postgres```

Run pylint:
```poetry run invoke lint```

Stop and remove volumes
```docker-compose down -v```
