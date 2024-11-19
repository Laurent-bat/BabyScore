from flask import request, jsonify
from config import app,db
from models import Player


base_ELO=1600


@app.route("/players", methods=["GET"])
def get_players():
    players = Player.query.all()
    json_players = list(map(lambda x: x.to_json(), players))
    
    return(jsonify({"players":json_players}))


@app.route("/create_player", methods=["POST"])
def create_player():
    name = request.json.get("name")
    
    if not name:
        return (jsonify({"message":"You must include a name"}),400)
    
    new_player= Player(name=name, atk_elo=base_ELO, def_elo= base_ELO)
    try:
        db.session.add(new_player)
        db.session.commit()
        
    except Exception as e:
        return jsonify({"message":str(e)}),400

    return jsonify({"message":"Player successfuly created"}),201


@app.route("/update_player/<int:user_id>", methods=["PATCH"])
def update_player(user_id):
    player=Player.query.get(user_id)
    
    if not player:
        return jsonify({"message":"Player not found"}),404
    
    data = request.json
    player.name= data.get("name", player.name)
    
    db.session.commit()
    
    return jsonify({"message":"Player updated"}),201

@app.route("/delete_player/<int:user_id>", methods=["DELETE"])
def delete_player(user_id):
    player=Player.query.get(user_id)
    
    if not player:
        return jsonify({"message":"Player not found"}),404
    
    db.session.delete(player)
    db.session.commit()
    
    return jsonify({"message":"Player deleted"})

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    
    
    app.run(debug=True)
