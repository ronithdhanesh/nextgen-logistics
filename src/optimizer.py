
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