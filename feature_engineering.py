from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineering(BaseEstimator, TransformerMixin):
    def fit(self, x, y=None):
        return self

    def transform(self, x):
        x = x.copy()

        # HighRisk feature
        x["HighRisk"] = ((x["InternetService"] == "Fiber optic") & (x["PaymentMethod"] == "Electronic check")).astype(int)

        # Has any kind of Protecteion
        col = ["OnlineSecurity","TechSupport"]
        x["ProtectionScore"] = (x[col] == "Yes").astype(int).sum(axis=1)

        # IsNewCustomer feature
        x["IsNewCustomer"] = ((x["tenure"]<12).astype(int))

        # HasStreaming feature
        stream =[ "StreamingMovies"]
        x["StreamingScore"] = (x[stream] == "Yes").astype(int).sum(axis=1)

        # mapping categorial features into numerical
        mapping={"Yes": 1,
                  "No": 0,
                  "No internet service": 0,
                  "No phone service": 0}
        
        cols = ["TechSupport",
                "OnlineSecurity",
                "StreamingMovies",
                "MultipleLines",
                "Dependents",
                "PaperlessBilling"]

        for col in cols:
            x[col]= x[col].map(mapping)

        # creating totalcharges feature
        x["TotalCharges"] = x["MonthlyCharges"] * x["tenure"]

        # remove temporary columns
        # x.drop(columns=['StreamingTV', 'StreamingMovies','OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport'], inplace=True)

        return x