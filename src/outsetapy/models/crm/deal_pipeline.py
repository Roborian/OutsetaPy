from typing import List
from datetime import datetime


class DealPipelineStage:
    # Define the DealPipelineStage class here
    pass


class DealPipeline:
    def __init__(
        self,
        Name: str,
        DealPipelineStages: List[DealPipelineStage],
        Uid: str,
        Created: datetime,
        Updated: datetime,
    ):
        self.Name = Name
        self.DealPipelineStages = DealPipelineStages
        self.Uid = Uid
        self.Created = Created
        self.Updated = Updated
