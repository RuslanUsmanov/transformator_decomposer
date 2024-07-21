from dataclasses import dataclass


@dataclass
class PassportParams:
    type: str = ""
    power: float = 0
    voltage: float = 0
    phase_num: int = 0
    material: str = ""


@dataclass
class SourceParams:
    R_meas: float = 352.8
    K_u: float = 2000.0
    R_one: float = 0.683
