import json
from flask import Flask, request
from types import SimpleNamespace
app = Flask(__name__)

# defines initial reservations
reservations = [ 
	{
		"reservationCreator" : "John Doe",
		"reservationId" : "1234",
		"contact" : "011-123-4567",
	},
	{
		"reservationCreator" : "Jane Doe",
		"reservationId" : "5678",
		"contact" : "011-123-4562",
	},
	{
		"reservationCreator" : "John Smith",
		"reservationId" : "9012",
		"contact" : "011-123-4523",
	}
]

# route relevant to the reservation management
@app.route('/rs/reservation/<reservationId>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def reservation_management(reservationId):
    if request.method == "GET":
        return str("Your reservation details: " + getReservation(reservationId))
    elif request.method == "POST":
        return str("Your added reservation details: " + addReservation(request))
    elif request.method == "PUT":
        return "Reservation updated: " + updateReservation(reservationId, request) ;
    elif request.method == "DELETE":
        return "Reservation deleted: " + deleteReservation(reservationId)

# route relevant to the hello world
@app.route('/rs/healthCheck', methods=['GET'])
def health_check():
    return "Hello, Welcome to the simple reservation management app!"

# route relevant to get all reservations
@app.route('/rs/reservations', methods=['GET'])
def get_reservations():
    return str(json.dumps(reservations))

# gives a reservation created by the user considering the reservationId
def getReservation(reservationId):
    print("getReservation")
    for reservation in reservations:
        if reservation["reservationId"] == reservationId:
            print(type(json.dumps(reservation)))
            return str(json.dumps(reservation))
    return None

# adds a reservation to the list of reservations
def addReservation(request):
    x = json.loads(request.get_data(), object_hook=lambda d: SimpleNamespace(**d))
    reservations.append({
        "reservationCreator" : x.reservationCreator,
		"reservationId" : x.reservationId,
		"contact" : x.contact,})
    print(reservations)
    return str(request.get_data())

# deletes a reservation from the list of reservations considering the reservationId
def deleteReservation(reservationId):
    for reservation in reservations:
        if reservation["reservationId"] == reservationId:
            reservations.remove(reservation)
            return str(json.dumps(reservation))
    return reservationId

# updates a reservation from the list of reservations considering the reservationId
def updateReservation(reservationId, request):
    for reservation in reservations:
        if reservation["reservationId"] == reservationId:
            reservations.remove(reservation)
            x = json.loads(request.get_data(), object_hook=lambda d: SimpleNamespace(**d))
            reservations.append({
                "reservationCreator" : x.reservationCreator,
		        "reservationId" : x.reservationId,
		        "contact" : x.contact,})
    print(reservations)
    return reservationId

if __name__ == "__main__":
    app.run()