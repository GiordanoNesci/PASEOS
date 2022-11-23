from loguru import logger


from .paseos import PASEOS
from .actors.base_actor import BaseActor
from .actors.actor_builder import ActorBuilder
from .actors.spacecraft_actor import SpacecraftActor
from .actors.ground_station_actor import GroundstationActor
from .utils.set_log_level import set_log_level
from .visualization.plot import plot, PlotType


set_log_level("DEBUG")

logger.debug("Loaded module.")


def init_sim(local_actor: BaseActor):
    """Initializes PASEOS

    Args:
        local_actor (BaseActor): The actor linked to the local device which is required to model anything.

    Returns:
        PASEOS: Instance of the simulation (only one can exist, singleton)
    """
    logger.debug("Initializing simulation.")
    sim = PASEOS(local_actor=local_actor)
    return sim


__all__ = [
    "ActorBuilder",
    "BaseActor",
    "GroundstationActor",
    "PASEOS",
    "plot",
    "PlotType",
    "set_log_level",
    "SpacecraftActor",
]