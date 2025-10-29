from .models import GeneProfile
import pandas as pd

def get_reference_profile(db):
    data = db.query(GeneProfile).all()
    return pd.DataFrame([(d.gene, d.expression) for d in data], columns=["Gene", "Expression"])
