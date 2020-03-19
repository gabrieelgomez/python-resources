import pdb;
class VotingBox:

    def __init__(self, id, cities_availables):
        self._id = id
        self._cities_availables = cities_availables
        self._region = None
    
    @property
    def region(self):
        return self._region
    
    @region.setter
    def region (self, region):
        if region in self._cities_availables:
            self._region = region
        else:
            raise ValueError(f'Region {region}, is not valid in {self._cities_availables}')

if __name__ == '__main__':
    box = VotingBox(99, ['New York', 'Madrid'])
    print(box.region)
    box.region = 'Madrid'
    print(box.region)