from config import db

class Player(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(80), unique=True, nullable=False)
    atk_elo= db.Column(db.Integer)
    def_elo= db.Column(db.Integer)
    
    def to_json(self):
        return {
            "id": self.id,
            "name":self.name,
            "attackElo":self.atk_elo,
            "defenseElo":self.def_elo,
            }