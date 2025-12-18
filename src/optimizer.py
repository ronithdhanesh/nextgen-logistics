# import joblib
# import pandas as pd

# def get_best_recommendation(route, current_carrier, priority, distance, traffic):
#     # Load brains
#     clf = joblib.load('models/classifier.pkl')
#     reg = joblib.load('models/regressor.pkl')
#     encoders = joblib.load('models/encoders.pkl')
    
#     all_carriers = encoders['Carrier'].classes_
#     results = []

#     r_enc = encoders['Route'].transform([route])[0]
#     p_enc = encoders['Priority'].transform([priority])[0]

#     for c in all_carriers:
#         c_enc = encoders['Carrier'].transform([c])[0]
#         test_input = [[c_enc, r_enc, p_enc, distance, traffic]]
        
#         prob = clf.predict_proba(test_input)[0][1]
#         days = reg.predict(test_input)[0]
        
#         results.append({'Carrier': c, 'Risk': prob, 'Days': days})

#     res_df = pd.DataFrame(results).sort_values(['Risk', 'Days'])
#     best = res_df.iloc[0]
#     current = res_df[res_df['Carrier'] == current_carrier].iloc[0]

#     return {
#         'current_risk': current['Risk'],
#         'current_days': current['Days'],
#         'best_carrier': best['Carrier'],
#         'best_risk': best['Risk'],
#         'risk_reduced': current['Risk'] - best['Risk']
#     }


import numpy as np


CARRIER_RISK = {
'FastLogistics': 0.42,
'QuickShip': 0.35,
'GlobalTransit': 0.28,
'EcoDeliver': 0.25,
'PrimeExpress': 0.31
}


def get_best_recommendation(route, carrier, priority, distance, traffic):
    base_risk = CARRIER_RISK.get(carrier, 0.35)
    traffic_factor = min(traffic / 120, 1)
    distance_factor = min(distance / 1500, 1)


    priority_modifier = {'Express': 0.9, 'Standard': 1.0, 'Economy': 1.1}
    risk = base_risk * (1 + traffic_factor + distance_factor) * priority_modifier.get(priority, 1)
    risk = min(risk, 0.95)


    best_carrier = min(CARRIER_RISK, key=CARRIER_RISK.get)
    best_risk = CARRIER_RISK[best_carrier]


    return {
    'current_risk': risk,
    'current_days': int(2 + risk * 4),
    'best_carrier': best_carrier,
    'risk_reduced': max(risk - best_risk, 0)
    }