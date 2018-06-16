from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()

minimum_volume, max_volume, step = volume.GetVolumeRange()


def set_volume(volume_level):
    absolute_volume = minimum_volume + (max_volume - minimum_volume) * volume_level
    volume.SetMasterVolumeLevel(absolute_volume, None)
