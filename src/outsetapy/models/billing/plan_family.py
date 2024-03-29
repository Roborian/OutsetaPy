class PlanFamily:
    def __init__(self, data: object):
        self.Name = data.get("Name")
        self.IsActive = data.get("IsActive")
        self.Plans = data.get("Plans")
        self.Uid = data.get("Uid")
        self.Created = data.get("Created")
        self.Updated = data.get("Updated")
