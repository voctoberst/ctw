
### task1

execute as below

```
python3 ./aio.py
```

will create sqlite db and get data from AlphaVantage
and then insert data to db


### task2
Not finish all.


same as task1
will create sqlite db and get data from AlphaVantage
and then insert data to db
```
python3 ./get_raw_data.py
```

financial(Django host)
```
python3 manage.py runserver
curl -X GET http://localhost:8000/admin/api/financial_data/?end_date=%3C%3D2023-02-25&start_date=%3E%3D2023-02-19&symbol=%3DIBM
```

docker(Django only)
need copy financial/schema.sql into docker
but I had not finish it
```
docker compose up -d
```
