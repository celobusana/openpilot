from openpilot.selfdrive.car import CarSpecs, PlatformConfig, Platforms, dbc_dict
from openpilot.selfdrive.car.docs_definitions import CarDocs

class CAR(Platforms):
  HAVAL_H6_PHEV = PlatformConfig(
    [CarDocs("Haval H6 PHEV", "All")],
    CarSpecs(mass=2000., wheelbase=2.959, steerRatio=15.0),
    dbc_dict('haval_powertrain', 'tesla_radar_bosch_generated', chassis_dbc='haval_can')
  )

class CarControllerParams:
  def __init__(self, CP):
    pass