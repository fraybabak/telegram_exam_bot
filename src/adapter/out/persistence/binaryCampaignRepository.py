from adapter.out.persistence.repository import Repository

from application.domain.BinaryCampaign import BinaryCampaign
from typing import List
from injector import inject
from database import session
from adapter.out.persistence.models.binaryCampaign import BinaryCampaignModel



class BinaryCampaignRepository(Repository):
    @inject
    def __init__(self):
        self.db = session
        self.model = BinaryCampaignModel
    
    def create(self, binaryCampaign: BinaryCampaign) -> BinaryCampaign:
        binaryCampaign_model = self.model(user_id=binaryCampaign.user_id, context_id=binaryCampaign.context_id, created_at=binaryCampaign.created_at, updated_at=binaryCampaign.updated_at, is_active=binaryCampaign.is_active)
        self.db.add(binaryCampaign_model)
        self.db.commit()
        self.db.refresh(binaryCampaign_model)
        return BinaryCampaign(id=binaryCampaign_model.id, user_id=binaryCampaign_model.user_id, context_id=binaryCampaign_model.context_id, created_at=binaryCampaign_model.created_at, updated_at=binaryCampaign_model.updated_at, is_active=binaryCampaign_model.is_active)
    
    def read(self, id: int) -> BinaryCampaign:
        binaryCampaign_model = self.db.query(self.model).filter(self.model.id == id).first()
        if binaryCampaign_model is None:
            raise Exception("BinaryCampaign not found")

        return BinaryCampaign(id=binaryCampaign_model.id, user_id=binaryCampaign_model.user_id, context_id=binaryCampaign_model.context_id, created_at=binaryCampaign_model.created_at, updated_at=binaryCampaign_model.updated_at, is_active=binaryCampaign_model.is_active)


    def find_by_user(self, user_id: int) -> List[BinaryCampaign]:
        binaryCampaign_model = self.db.query(self.model).filter(self.model.user_id == user_id).all()
        if binaryCampaign_model is None:
            raise Exception("BinaryCampaign not found")
        return [BinaryCampaign(id=binaryCampaign_model.id, user_id=binaryCampaign_model.user_id, context_id=binaryCampaign_model.context_id, created_at=binaryCampaign_model.created_at, updated_at=binaryCampaign_model.updated_at, is_active=binaryCampaign_model.is_active) for binaryCampaign_model in binaryCampaign_model]

    def find_by_context(self, context_id: int) -> List[BinaryCampaign]:
        binaryCampaign_model = self.db.query(self.model).filter(self.model.context_id == context_id).all()
        if binaryCampaign_model is None:
            raise Exception("BinaryCampaign not found")
        return [BinaryCampaign(id=binaryCampaign_model.id, user_id=binaryCampaign_model.user_id, context_id=binaryCampaign_model.context_id, created_at=binaryCampaign_model.created_at, updated_at=binaryCampaign_model.updated_at, is_active=binaryCampaign_model.is_active) for binaryCampaign_model in binaryCampaign_model]

    def find_by_user_and_context(self, user_id: int, context_id: int) -> BinaryCampaign:
        binaryCampaign_model = self.db.query(self.model).filter(self.model.user_id == user_id, self.model.context_id == context_id).first()
        if binaryCampaign_model is None:
            raise Exception("BinaryCampaign not found")
        return BinaryCampaign(id=binaryCampaign_model.id, user_id=binaryCampaign_model.user_id, context_id=binaryCampaign_model.context_id, created_at=binaryCampaign_model.created_at, updated_at=binaryCampaign_model.updated_at, is_active=binaryCampaign_model.is_active)