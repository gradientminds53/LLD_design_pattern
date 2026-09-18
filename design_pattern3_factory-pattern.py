# factory design pattern 
# without factory pattern 
class RandomForestModel:
    def train(self):
        print("Training Random Forest")


class XGBoostModel:
    def train(self):
        print("Training XGBoost")


class LightGBMModel:
    def train(self):
        print("Training LightGBM")

algorithm = "xgboost"

if algorithm == "random_forest":
    model = RandomForestModel()

elif algorithm == "xgboost":
    model = XGBoostModel()

elif algorithm == "lightgbm":
    model = LightGBMModel()

model.train()


#  With Factory

class RandomForestModel:
    def train(self):
        print("Training Random Forest")


class XGBoostModel:
    def train(self):
        print("Training XGBoost")


class LightGBMModel:
    def train(self):
        print("Training LightGBM")

class ModelFactory:

    @staticmethod
    def create_model(algorithm):

        if algorithm == "random_forest":
            return RandomForestModel()

        elif algorithm == "xgboost":
            return XGBoostModel()

        elif algorithm == "lightgbm":
            return LightGBMModel()

        else:
            raise ValueError("Unknown algorithm")

# client code

model = ModelFactory.create_model("xgboost")

model.train()
