from flix.kodi import ADDON_ICON
from flix.provider import Provider, ProviderResult
from xbmc import executebuiltin
from xbmcgui import ListItem
from xbmcplugin import setResolvedUrl


# noinspection PyMethodMayBeStatic
class DummyProvider(Provider):
    def search(self, query):
        return [
            ProviderResult(
                label="Big Buck Bunny",
                label2="Blender Foundation - archive.org - 720p - query:" + query,
                icon=ADDON_ICON,
                url="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4",
            ),
        ]

    def search_movie(self, tmdb_id, title, titles, year=None):
        return [
            ProviderResult(
                label="Ignored result",
                label2="First result is ignored, as there is no url",
                icon=ADDON_ICON,
            ),
            ProviderResult(
                label="With all parameters but provider_data",
                label2="provider_data is not necessary as we have the url",
                icon=ADDON_ICON,
                url="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4",
            ),
            ProviderResult(
                label="Test fallback icon with provider_data (use setResolvedUrl)",
                label2="Test fallback icon when no icon is provided",
                provider_data={
                    "path": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.avi",
                }
            ),
            ProviderResult(
                label="Test fallback icon with provider_data (return url)",
                label2="This will then call resolve method (which will return the resolved url to Flix)",
                provider_data={
                    "url": "https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.ogv",
                }
            ),
            ProviderResult(
                label="Check input args",
                label2="tmdb_id={}, title={}, titles={}, year={}".format(tmdb_id, title, titles, year),
                url="-",
            ),
        ]

    def search_episode(self, tmdb_id, show_title, season_number, episode_number, titles):
        return [
            ProviderResult(
                label="Test with no url but with provider_data",
                label2="This will then call resolve method (which will call youtube for this case)",
                icon=ADDON_ICON,
                provider_data={"youtube": "aqz-KE-bpKQ"}
            ),
            ProviderResult(
                label="Check input args",
                label2="tmdb_id={}, show_title={}, season_number={}, episode_number={}, titles={}".format(
                    tmdb_id, show_title, season_number, episode_number, titles),
                url="-",
            ),
        ]

    def resolve(self, handle, provider_data):
        if isinstance(provider_data, dict):
            if "youtube" in provider_data:
                executebuiltin("RunPlugin(plugin://plugin.video.youtube/play/?video_id={})".format(
                    provider_data["youtube"]))
                return None
            elif "path" in provider_data:
                setResolvedUrl(handle, True, ListItem(path=provider_data["path"]))
                return None
            elif "url" in provider_data:
                return provider_data["url"]

        raise ValueError("Unknown provider_data")
