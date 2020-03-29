from flix.kodi import ADDON_ICON
from flix.provider import Provider, ProviderResult
from xbmc import executebuiltin
from xbmcgui import ListItem
from xbmcplugin import setResolvedUrl


# noinspection PyMethodMayBeStatic,PyUnusedLocal
class DummyProvider(Provider):
    def search(self, query):
        return []

    def search_movie(self, tmdb_id, title, year, titles):
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
        ]

    def search_episode(self, tmdb_id, show_title, season_number, episode_number, titles):
        return [
            ProviderResult(
                label="Test with no url but with provider_data",
                label2="This will then call resolve method (which will call youtube for this case)",
                icon=ADDON_ICON,
                provider_data={"youtube": "aqz-KE-bpKQ"}
            ),
        ]

    def resolve(self, handle, item, provider_data):
        if isinstance(provider_data, dict):
            if "youtube" in provider_data:
                executebuiltin("RunPlugin(plugin://plugin.video.youtube/play/?video_id={})".format(
                    provider_data["youtube"]))
                return None
            elif "path" in provider_data:
                list_item = ListItem(item["title"], path=provider_data["path"])
                list_item.setInfo("video", item["info"])
                list_item.setArt(item["art"])
                setResolvedUrl(handle, True, list_item)
                return None
            elif "url" in provider_data:
                return provider_data["url"]

        raise ValueError("Unknown provider_data")