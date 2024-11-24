from flask import request, jsonify
from config import app,db
from models import Player, Matchs


base_ELO=1600



def calculate_ELO(black_atk,black_def,white_atk,white_def,white_score,black_score,K=16):
    # Retrieving the ELO of each player
    player_black_atk=Player.query.get(black_atk)
    player_black_def=Player.query.get(black_def)
    player_white_atk=Player.query.get(white_atk)
    player_white_def=Player.query.get(white_def)
    
    # Calculate ELO of the match
    R_white=(player_white_atk.atk_elo+player_white_def.def_elo)/2 # Ranking of team white
    R_black=(player_black_atk.atk_elo+player_black_def.def_elo)/2 # Ranking of team black
    
    E_white=1/(1+10**((R_white-R_black)/400))
    E_black=1/(1+10**((R_black-R_white)/400))
    
    S_white=int(white_score>black_score)
    S_black=1-S_white
    
    
    # Update Elo of each player
    player_white_atk.atk_elo=player_white_atk.atk_elo+K*(S_white-E_white)
    player_white_atk.avg_elo=(player_white_atk.atk_elo+player_white_atk.def_elo)/2
    
    player_white_def.def_elo=player_white_def.def_elo+K*(S_white-E_white)
    player_white_def.avg_elo=(player_white_def.def_elo+player_white_def.atk_elo)/2
    
    player_black_atk.atk_elo=player_black_atk.atk_elo+K*(S_black-E_black)
    player_black_atk.avg_elo=(player_black_atk.atk_elo+player_black_atk.def_elo)/2
    
    player_black_def.def_elo=player_black_def.def_elo+K*(S_black-E_black)
    player_black_def.avg_elo=(player_black_def.def_elo+player_black_def.atk_elo)/2

    return(E_white,E_black)


# Player Handeling

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
    
    new_player= Player(name=name, atk_elo=base_ELO, def_elo= base_ELO, avg_elo=base_ELO)
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


# Matchs Handeling
@app.route("/matchs", methods=["GET"])
def get_matchs():
    matchs = Matchs.query.all()
    json_matchs = list(map(lambda x: x.to_json(), matchs))
    
    return(jsonify({"matchs":json_matchs}))


@app.route("/create_match", methods=["POST"])
def create_match():
    black_atk=request.json.get("blackAttack")
    black_def=request.json.get("blackDefense")
    white_atk=request.json.get("whiteAttack")
    white_def=request.json.get("whiteDefense")
    white_score=request.json.get("whiteScore")
    black_score=request.json.get("blackScore")
    
    
    if not black_atk or not black_def or not white_atk or not white_def or not white_score or not black_score :
        return (jsonify({"message":"You must include existing players and a score."}),400)
    
    E_white,E_black=calculate_ELO(black_atk=black_atk,black_def=black_def,white_atk=white_atk,white_def=white_def,white_score=white_score,black_score=black_score)
    new_match= Matchs(black_atk=black_atk,black_def=black_def,white_atk=white_atk,white_def=white_def,white_score=white_score,black_score=black_score,E_white=E_white,E_black=E_black)
    try:
        db.session.add(new_match)
        db.session.commit()
        
    except Exception as e:
        return jsonify({"message":str(e)}),400
    
    return jsonify({"message":"Match successfuly created"}),201


# @app.route("/update_match/<int:user_id>", methods=["PATCH"])
# def update_match(user_id):
# TODO revert ranking after match update
#     match=Matchs.query.get(user_id)
    
#     if not match:
#         return jsonify({"message":"match not found"}),404
    
#     data = request.json
#     match.name= data.get("name", match.name)
#     match.
    
#     db.session.commit()
    
#     return jsonify({"message":"Match updated"}),201

# @app.route("/delete_match/<int:user_id>", methods=["DELETE"])
# def delete_match(user_id):
#     # TODO revert ranking after match deletion
#     match=Matchs.query.get(user_id)
    
#     if not match:
#         return jsonify({"message":"Match not found"}),404
    
#     db.session.delete(match)
#     db.session.commit()
    
#     return jsonify({"message":"Match deleted"})



if __name__=="__main__":
    with app.app_context():
        db.create_all()
    
    
    app.run(debug=True)
