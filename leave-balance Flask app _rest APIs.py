from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['leave_balance_db']
leave_balance_collection = db['leave_balance']

class LeaveBalanceResource(Resource):
    def get(self):
        leave_balance = leave_balance_collection.find_one({})
        if leave_balance:
            return jsonify({"leave_balance": leave_balance["balance"]})
        else:
            return {"message": "Leave balance not found"}, 404

    def post(self):
        leave_balance_data = request.json
        leave_balance_collection.update_one({}, {"$set": {"balance": leave_balance_data["balance"]}}, upsert=True)
        return {"message": "Leave balance updated successfully"}

class LeaveDeductResource(Resource):
    def post(self):
        try:
            leave_to_deduct = float(request.json['leave_to_deduct'])
            leave_balance = leave_balance_collection.find_one({})["balance"]

            if leave_to_deduct <= leave_balance:
                new_balance = leave_balance - leave_to_deduct
                leave_balance_collection.update_one({}, {"$set": {"balance": new_balance}})
                return {"message": f"Leave deducted successfully! New balance: {new_balance}"}
            else:
                return {"message": "Not enough leave balance to deduct."}, 400
        except ValueError:
            return {"message": "Invalid input. Please enter a valid number for leave deduction."}, 400

# Add the LeaveBalanceResource and LeaveDeductResource to the Flask API
api.add_resource(LeaveBalanceResource, '/api/leave-balance')
api.add_resource(LeaveDeductResource, '/api/deduct-leave')

if __name__ == '__main__':
    app.run(debug=True)

