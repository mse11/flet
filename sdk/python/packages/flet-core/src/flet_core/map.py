import dataclasses
from dataclasses import dataclass, field
from typing import Any, Optional, Union, List, Tuple

from flet_core.constrained_control import ConstrainedControl
from flet_core.control import OptionalNumber
from flet_core.map_rich_attribution import MapRichAttribution
from flet_core.map_tile_layer import MapTileLayer
from flet_core.ref import Ref
from flet_core.types import (
    AnimationValue,
    OffsetValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
)


@dataclasses.dataclass
class MapLatitudeLongitude:
    latitude: Union[float, int]
    longitude: Union[float, int]


@dataclass
class MapOption:
    apply_pointer_translucency_to_layers: Optional[bool] = field(default=None)
    bgcolor: Optional[str] = field(default=None)
    initial_center: Optional[Tuple[Union[int, float], Union[int, float]]] = field(
        default=None
    )  # todo: change type to MapLatitudeLongitude
    initial_rotation: OptionalNumber = field(default=None)
    initial_zoom: OptionalNumber = field(default=None)
    keep_alive: Optional[bool] = field(default=None)
    max_zoom: OptionalNumber = field(default=None)
    min_zoom: OptionalNumber = field(default=None)


class Map(ConstrainedControl):
    """
    Map Control.

    -----

    Online docs: https://flet.dev/docs/controls/map
    """

    def __init__(
        self,
        layers: List[Union[MapTileLayer, MapRichAttribution]] = None,
        option: Optional[MapOption] = None,
        #
        # ConstrainedControl
        #
        ref: Optional[Ref] = None,
        key: Optional[str] = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[None, bool, int] = None,
        expand_loose: Optional[bool] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        aspect_ratio: OptionalNumber = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        on_animation_end=None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
    ):

        ConstrainedControl.__init__(
            self,
            ref=ref,
            key=key,
            width=width,
            height=height,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            expand=expand,
            expand_loose=expand_loose,
            col=col,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            aspect_ratio=aspect_ratio,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            on_animation_end=on_animation_end,
            tooltip=tooltip,
            visible=visible,
            disabled=disabled,
            data=data,
        )

        self.option = option
        self.layers = layers

    def _get_control_name(self):
        return "map"

    def _get_children(self):
        return self.layers

    def before_update(self):
        super().before_update()
        if isinstance(self.__option, MapOption):
            self._set_attr_json("option", self.__option)

    # option
    @property
    def option(self) -> Optional[MapOption]:
        return self.__option

    @option.setter
    def option(self, value: Optional[MapOption]):
        self.__option = value

    # layers
    @property
    def layers(self) -> List[Union[MapTileLayer, MapRichAttribution]]:
        return self.__layers

    @layers.setter
    def layers(self, value: List[Union[MapTileLayer, MapRichAttribution]]):
        self.__layers = value
