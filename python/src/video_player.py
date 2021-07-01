"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playing = []
        self.pause = []
        self.playlist = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")

        videos = self._video_library.get_all_videos()
        videoToSort = []

        for video in videos:
            videoToSort.append([video.title, video.video_id, video.tags])

        sortedVideo = sorted(videoToSort, key=lambda x: x[0])

        for video in sortedVideo:
            # print(f' {video[0]} {video[1]} {" ".join([video[2])}')
            print(video[0] + " (" + video[1] + ") " + "[" + " ".join(video[2]) + "]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        videoToPlay = self._video_library.get_video(video_id)
        # print(self.playing)

        if videoToPlay is None:
            print("Cannot play video: Video does not exist")
        else:
            if len(self.playing) > 0:
                self.stop_video()  ## stop the previous video

            self.playing.append(videoToPlay)
            # print(self.playing)
            print(f"Playing video: {videoToPlay.title}")

    def stop_video(self):
        """Stops the current video."""
        if len(self.playing) == 0:
            print("Cannot stop video: No video is currently playing")
        elif len(self.playing) > 0:
            videoToStop = self.playing.pop()
            print(f"Stopping video: {videoToStop.title}")

    def play_random_video(self):
        """Plays a random video from the video library."""
        allVideos = self._video_library.get_all_videos()
        videoPlay = []
        for video in allVideos:
            videoPlay.append(video.video_id)

        num = random.randint(0, 4)
        self.play_video(videoPlay[num])

    def pause_video(self):
        """Pauses the current video."""
        if len(self.playing) == 0:
            print("Cannot pause video: No video is currently playing")
            return

        videoToPause = self.playing[-1]

        if videoToPause in self.pause:
            print(f"Video already paused: {videoToPause.title}")
            return
        else:
            self.pause.append(videoToPause)
            print(f"Pausing video: {videoToPause.title}")

    def continue_video(self):
        """Resumes playing the current video."""

        if len(self.playing) == 0:
            print("Cannot continue video: No video is currently playing")
            return

        if len(self.pause) == 0 and len(self.playing) > 0:
            print("Cannot continue video: Video is not paused")
            return

        videoToContinue = self.pause.pop()
        print(f"Continuing video: {videoToContinue.title}")

    def show_playing(self):
        """Displays video currently playing."""

        if len(self.playing) == 0:
            print("No video is currently playing")
            return

        if len(self.pause) > 0:
            print("Currently playing: " + self.playing[-1].title + " (" + self.playing[
                -1].video_id + ") " + "[" + " ".join(self.playing[-1].tags) + "] - " + "PAUSED")
        elif len(self.playing) > 0 and len(self.pause) == 0:
            print("Currently playing: " + self.playing[-1].title + " (" + self.playing[
                -1].video_id + ") " + "[" + " ".join(self.playing[-1].tags) + "]")

        # if self.playing[-1] == self.pause[-1]:
        #     print("Currently playing: " + self.playing[-1].title + " (" + self.playing[
        #         -1].video_id + ") " + "[" + " ".join(self.playing[-1].tags) + "] - PAUSED")
        # elif self.playing > 0 and self.playing[-1] not in self.pause[-1]:
        #     print("Currently playing: " + self.playing[-1].title + " (" + self.playing[
        #         -1].video_id + ") " + "[" + " ".join(self.playing[-1].tags) + "]")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for key in self.playlist:
            if str(key).upper() == str(playlist_name).upper():
                print("Cannot create playlist: A playlist with the same name already exists")
                return
        self.playlist[playlist_name] = []
        # print(self.playlist)
        print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        videoToAdd = self._video_library.get_video(video_id)
        playlistNameUpper = str(playlist_name).upper()
        if playlistNameUpper not in str(self.playlist.keys()).upper():
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            return

        if videoToAdd is None:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return


        for key in self.playlist:
            if videoToAdd in self.playlist[key]:
                print(f"Cannot add video to {playlist_name}: Video already added")
                return

        for key in self.playlist:
            if str(key).upper() == playlistNameUpper:
                self.playlist[key].append(videoToAdd)
                print(f"Added video to {playlist_name}: {videoToAdd.title}")
                return

        # print(f"Cannot add video to {playlist_name}: Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""
        if len(self.playlist) == 0:
            print("No playlists exist yet")
            return

        print("Showing all playlists:")

        for key in sorted(self.playlist):
            print(key)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        # if len(self.playlist[playlist_name]) == 0:
        #     print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
        #     return

        playlistNameUpper = str(playlist_name).upper()
        if playlistNameUpper not in str(self.playlist.keys()).upper():
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
            return

        print(f"Showing playlist: {playlist_name}")
        for key in self.playlist:
            if str(key).upper() == playlistNameUpper:
                if len(self.playlist[key]) == 0:
                    print("No videos here yet")
                elif len(self.playlist[key]) > 0:
                    for video in self.playlist[key]:
                        print(video.title + " (" + video.video_id + ") " + "[" + " ".join(video.tags) + "]")


        # print(f"Showing playlist: {playlist_name}")
        # if len(self.playlist[playlist_name]) == 0:
        #     print("No videos here yet")
        # elif len(self.playlist[playlist_name]) > 0:
        #     print(self.playlist[playlist_name].title + " " + self.playlist[playlist_name].video_id + " " + " ".join(self.playlist[playlist_name].tags))

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        # videoToRemove = self._video_library.get_video(video_id)
        #
        # playlistNameUpper = str(playlist_name).upper()
        # if playlistNameUpper not in str(self.playlist.keys()).upper():
        #     print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
        #     return
        #
        # for key in self.playlist:
        #     if videoToRemove == key:
        #         if len(self.playlist[key]) > 0:
        #             print(f"Removed video from {playlist_name}: {videoToRemove.title}")
        videoToRemove = self._video_library.get_video(video_id)

        playlistNameUpper = str(playlist_name).upper()
        if playlistNameUpper not in str(self.playlist.keys()).upper():
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
            return

        if videoToRemove is None:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
            return

        for key in self.playlist:
            if playlistNameUpper == str(key).upper():
                if videoToRemove in self.playlist[key]:
                    self.playlist[key].remove(videoToRemove)
                    print(f"Removed video from {playlist_name}: {videoToRemove.title}")
                else:
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")



    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlistNameUpper = str(playlist_name).upper()
        if playlistNameUpper not in str(self.playlist.keys()).upper():
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
            return

        for key in self.playlist:
            if playlistNameUpper == str(key).upper():
                self.playlist[key].clear()
                print(f"Successfully removed all videos from {playlist_name}")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlistNameUpper = str(playlist_name).upper()
        if playlistNameUpper not in str(self.playlist.keys()).upper():
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
            return

        for key in self.playlist:
            if playlistNameUpper == str(key).upper():
                self.playlist.pop(key)
                print(f"Deleted playlist: {playlist_name}")
                return


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        result = []
        videos = self._video_library.get_all_videos()
        searchTermUpper = search_term.upper()

        for video in videos:
            if searchTermUpper in video.title.upper():
                result.append([video.title, video.video_id, video.tags])

        if len(result) == 0:
            print(f"No search results for {search_term}")
            return

        sortedVideo = sorted(result, key=lambda x: x[0])

        for video in sortedVideo:
            print(video[0] + " (" + video[1] + ") " + "[" + " ".join(video[2]) + "]")
        inp = input("Would you like to play any of the above? If yes, specify the number of the video. If your answer is not a valid number, we will assume it's a no")

        if inp.isalpha():
            return

        if inp.isdigit():
            if len(sortedVideo) > int(inp):
                return
            else:
                videoToPlay = sortedVideo[int(inp)-1]
                self.play_video(videoToPlay[1])

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
