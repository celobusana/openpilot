from openpilot.selfdrive.car.interfaces import CarControllerBase, SendCan
from openpilot.selfdrive.car.gwm.values import CarControllerParams
from openpilot.selfdrive.car.gwm.gmwcan import GwmCan
from opendbc.can.packer import CANPacker
from cereal import car

class CarController(CarControllerBase):
  def __init__(self, dbc_name, CP, VM):
    fingerprint = None

    self.CP = CP
    self.CAN = GwmCan(CP, fingerprint)
    self.params = CarControllerParams(CP)
    self.packer = CANPacker(dbc_name)


  def update(self, CC: car.CarControl.Actuators, CS: car.CarState, now_nanos: int) -> tuple[car.CarControl.Actuators, list[SendCan]]:
    actuators = CC.actuators
    can_sends = []

    return self.actuators_output(actuators), can_sends

  def actuators_output(self, actuators):
    actuators_output = actuators.copy()
    return actuators_output
