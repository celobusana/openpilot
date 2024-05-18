from openpilot.selfdrive.car.interfaces import CarStateBase
from openpilot.common.conversions import Conversions as CV
from cereal import car

class CarState(CarStateBase):
  def __init__(self, CP):
    super().__init__(CP)

    self.state_processors = {
      "vehicle_speed": self.processor_vehicle_speed
    }

  def update(self, cp, cp_cam):
    self.state = car.CarState.new_message()
    self.cp = cp
    self.cp_cam = cp_cam

    for processor in self.state_processors.values():
      processor()

    return self.state

  def processor_vehicle_speed(self) -> None:
    # Vehicle speed Raw
    self.state.vEgoRaw = self.cp.vl["ESP_B"]["ESP_vehicleSpeed"] * CV.KPH_TO_MS
    # Vehicle speed Filtered, Acceleration
    self.state.vEgo, self.state.aEgo = self.update_speed_kf(self.state.vEgoRaw)
    self.state.standstill = (self.state.vEgo < 0.1)

