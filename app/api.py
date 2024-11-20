from flask import Flask, request, jsonify
from .AccountRegistry import AccountRegistry
from .PersonalAccount import PersonalAccount
app = Flask(__name__)
@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    konto = PersonalAccount(data["imie"], data["nazwisko"], data["pesel"])
    AccountRegistry.add_account(konto)
    return jsonify({"message": "Account created"}), 201


@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    account=AccountRegistry.search_by_pesel(pesel)
    if account is None:
        return jsonify({"message": "konta brak"}), 404
    return jsonify({"imie": account.imie, "nazwisko": account.nazwisko, "saldo": account.saldo}), 200

@app.route("/api/accounts/count", methods=['GET'])
def how_many_accounts():
    return f"Ilość kont w rejestrze {AccountRegistry.get_accounts_count()}", 200


@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    data = request.get_json()
    account = AccountRegistry.search_by_pesel(pesel)
    if account is None:
        return jsonify({"message": "konta brak"}), 404
    account.imie=data["imie"]
    account.nazwisko = data["nazwisko"]
    account.pesel = data["pesel"]
    account.saldo = data["saldo"]

    return jsonify({"message": "Account updated"}), 200


@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    account = AccountRegistry.search_by_pesel(pesel)
    if account is None:
        return jsonify({"message": "konta brak"}), 404
    AccountRegistry.delete_by_pesel(pesel)
    return jsonify("konto usuniete"), 200
