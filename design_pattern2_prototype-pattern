# prototype design pattern 
# ml prototype
# without using protype pattern 
class DataLoader:

    def load_data(self):
        print("Loading training data...")

    def load_features(self):
        print("Loading feature metadata...")


class MLPipeline:

    def __init__(self):
        loader = DataLoader()

        loader.load_data()
        loader.load_features()

        self.algorithm = "XGBoost"

    def train(self):
        print(f"Training {self.algorithm}")

model1 = MLPipeline()
model2 = MLPipeline()
model3 = MLPipeline()


#with prototype
import copy


class DataLoader:

    def load_data(self):
        print("Loading training data...")

    def load_features(self):
        print("Loading feature metadata...")


class MLPipeline:

    def __init__(self):
        loader = DataLoader()

        loader.load_data()
        loader.load_features()

        self.algorithm = "XGBoost"

    def clone(self):
        return copy.deepcopy(self)

    def train(self):
        print(f"Training {self.algorithm}")



template = MLPipeline()

model1 = template.clone()
model2 = template.clone()
model3 = template.clone()

model1.algorithm = "RandomForest"
model2.algorithm = "XGBoost"
model3.algorithm = "LightGBM"

model1.train()
model2.train()
model3.train()
