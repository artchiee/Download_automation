
class Files:
    def __init__(self, name,year,  quality_type,quality_size, url, stars): 
        self.name = name
        self.quality_type = quality_type  #[ 1080 Full hd | 720 Hd | Low ] ..
        self.quality_size = quality_size  # [ Quality size by : ] GB or MB
        self.url  = url   # Final download link will be web page

    # def serialize(self):
    #     return { 
    #         "name" : self.name,
    #         "quality_type" : self.quality_type,
    #         "quality_size" : self.quality_size,
    #         "url" : self.url
    #     }

    # def transform(self):
    #     if isinstance(self.name, Files):
    #         return self.name.__dict__
    #     else:
    #         print('exception')
    
    # def from_json(self, json_):
    #     self.name = json_["name"]
    #     self.quality_type = json_["quality_type"]
    #     self.quality_size = json_["quality_size"]
    #     self.url = json_["url"]