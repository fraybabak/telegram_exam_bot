

class BinaryCampaign:
    def __init__(self,  is_active, created_at, updated_at, user_id, context_id,  id=None, end_date=None):
        self.id = id
        self.end_date = end_date
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at
        self.user_id = user_id
        self.context_id = context_id
    
    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self)