import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

def train_nexgen_models():
    orders = pd.read_csv('data/orders.csv')
    perf = pd.read_csv('data/delivery_performance.csv')
    routes = pd.read_csv('data/routes_distance.csv')
    costs = pd.read_csv('data/cost_breakdown.csv')
    feedback = pd.read_csv('data/customer_feedback.csv')
    fleet = pd.read_csv('data/vehicle_fleet.csv')
    inv = pd.read_csv('data/warehouse_inventory.csv')

    df = pd.merge(perf, orders, on='Order_ID', how='inner')
    df = pd.merge(df, routes[['Order_ID', 'Route', 'Distance_KM', 'Traffic_Delay_Minutes', 'Weather_Impact']], on='Order_ID', how='inner')
    df = pd.merge(df, costs, on='Order_ID', how='inner')

    df['Weather_Impact'] = df['Weather_Impact'].fillna('Clear')
    df['Delay_Days'] = df['Actual_Delivery_Days'] - df['Promised_Delivery_Days']
    df['Is_Delayed'] = (df['Delay_Days'] > 0).astype(int)
    
    df['Failure_Cost'] = np.where(df['Is_Delayed'] == 1, (df['Delivery_Cost_INR'] * 0.5) + 100, 0)

    le_dict = {}
    for col in ['Carrier', 'Route', 'Priority']:
        le = LabelEncoder()
        df[f'{col}_Enc'] = le.fit_transform(df[col])
        le_dict[col] = le

    features = ['Carrier_Enc', 'Route_Enc', 'Priority_Enc', 'Distance_KM', 'Traffic_Delay_Minutes']
    X = df[features]
    
    clf = RandomForestClassifier(n_estimators=100, random_state=42).fit(X, df['Is_Delayed'])
    reg = RandomForestRegressor(n_estimators=100, random_state=42).fit(X, df['Delay_Days'])

    df.to_csv('models/processed_data.csv', index=False)
    joblib.dump(clf, 'models/classifier.pkl')
    joblib.dump(reg, 'models/regressor.pkl')
    joblib.dump(le_dict, 'models/encoders.pkl')
    print("Training Complete. Intelligence stored in models/ directory.")

if __name__ == "__main__":
    train_nexgen_models()