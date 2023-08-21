
# Running the application locally.

To run the application execute below command

`FLASK_APP=app.py flask run`

# Invoking resources

## Viewing all the available resevations

```
curl -X GET http://localhost:5000/reservations


[{"reservationCreator": "John Doe", "reservationId": "1234", "contact": "011-123-4567"}, {"reservationCreator": "Jane Doe", "reservationId": "5678", "contact": "011-123-4562"}, {"reservationCreator": "John Smith", "reservationId": "9012", "contact": "011-123-4523"}]
```

## Viewing a specific resevation

```
curl -X GET http://localhost:5000/reservation/1234

Your reservation details: {"reservationCreator": "John Doe", "reservationId": "1234", "contact": "011-123-4567"}

```

## Adding a resevation

```
curl -X POST -d '{"reservationCreator": "John Doe", "reservationId": "111", "contact": "011-123-1111"}' http://localhost:5000/reservation/1111


Your added reservation details: b'{"reservationCreator": "John Doe", "reservationId": "111", "contact": "011-123-1111"}'
```

## Updating a resevation

```
curl -X PUT http://localhost:5000/reservation/1234 -d '{"reservationCreator": "Lahiru C", "reservationId": "1234", "contact": "011-123-4588"}' 

Reservation updated: 1234
```

## Deleting a resevation

```
curl -X DELETE http://localhost:5000/reservation/1234

Reservation deleted: {"reservationCreator": "John Doe", "reservationId": "1234", "contact": "011-123-4567"}

```
