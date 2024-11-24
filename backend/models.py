from config import db

class Player(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(80), unique=True, nullable=False)
    atk_elo= db.Column(db.Integer)
    def_elo= db.Column(db.Integer)
    avg_elo= db.Column(db.Integer)
    
    def to_json(self):
        return {
            "id": self.id,
            "name":self.name,
            "attackElo":self.atk_elo,
            "defenseElo":self.def_elo,
            "averageElo": self.avg_elo
            }

class Matchs(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    black_atk= db.Column(db.Integer)
    black_def= db.Column(db.Integer)
    white_atk= db.Column(db.Integer)
    white_def= db.Column(db.Integer)
    white_score=db.Column(db.Integer)
    black_score=db.Column(db.Integer)
    E_white=db.Column(db.Integer)
    E_black=db.Column(db.Integer)
    
    def to_json(self):
        return{
            "id": self.id,
            "blackAttack": self.black_atk,
            "blackDefense": self.black_def,
            "whiteAttack": self.white_atk,
            "whiteDefense": self.white_def,
            "whiteScore": self.white_score,
            "blackScore": self.black_score
        }