
class Files:
    def __init__(self, name, year, duration_time, quality_type, quality_size, stars):
        self.name = name
        self.year = year
        self.duration_time = duration_time
        self.quality_type = quality_size  # [ 1080 Full hd | 720 Hd | Low ] ..
        self.quality_size = quality_size  # [ Quality size by : ] GB or MB
        self.stars = stars

    def serialize(self):
        return {
            "name": self.name,
            "quality_type": self.quality_type,
            "quality_size": self.quality_size,
            "url": self.url
        }

    def from_json(self, json_):
        self.name = json_["name"]
        self.quality_type = json_["quality_type"]
        self.quality_size = json_["quality_size"]
        self.url = json_["url"]

    # def transform(self):
    #     if isinstance(self.name, Files):
    #         return self.name.__dict__
    #     else:
    #         print('exception')
