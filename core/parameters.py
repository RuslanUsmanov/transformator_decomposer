from dataclasses import dataclass


@dataclass
class PassportParams:
    type: str = ""
    power: str = ""
    voltage: str = ""
    phase_num: str = ""
    material: str = ""


@dataclass
class SourceParams:
    R_meas: float = 352.8
    K_u: float = 2000.0
    R_one: float = 0.683
