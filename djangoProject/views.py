from django.shortcuts import render
from django.http import HttpResponse
import youtube_dl
from .forms import DownloadForm
import re


def download_video(request):
    global context
    form = DownloadForm(request.POST or None)

    if form.is_valid():
        video_url = form.cleaned_data.get("url")
        regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'

        if not re.match(regex, video_url):
            return HttpResponse('Enter correct url.')

        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(video_url, download=False)

        video_audio_streams = []
        for m in meta['formats']:
            file_size = m['filesize']
            if file_size is not None:
                file_size = f'{round(int(file_size) / 1000000, 2)} mb'

            # Check if the format includes both video and audio
            if 'acodec' in m and m['acodec'] != 'none' and 'vcodec' in m and m['vcodec'] != 'none':
                resolution = f"{m['height']}x{m['width']}"
            else:
                # Skip formats that do not include both video and audio
                continue

            video_audio_streams.append({
                'resolution': resolution,
                'extension': m['ext'],
                'file_size': file_size,
                'video_url': m['url']
            })


        # Custom sorting function to prioritize MP4 and then MP3
        def custom_sort(stream):
            extension_priority = {'mp4': 1, 'mp3': 2, 'other': 3}
            strem_priority = {'2160p': 1, '1440p': 2, '1080p': 3, '720p': 4,'480p': 5, '360p': 6, '240p': 7, '144p': 8, 'other': 9}
            return (extension_priority.get(stream['extension'], 3), strem_priority.get(stream['resolution'],7), stream['extension'])

        video_audio_streams = sorted(video_audio_streams, key=custom_sort)

        context = {
            'form': form,
            'title': meta['title'],
            'streams': video_audio_streams,
            'description': meta['description'], 'likes': meta['like_count'],
            'dislikes': meta['dislike_count'], 'thumb': meta['thumbnails'][3]['url'],
            'duration': round(int(meta['duration'])/60, 2), 'views': f'{int(meta["view_count"]):,}'
        }
        print(f"Resolution: resolution, Extension: {m['ext']}, File Size: {m['filesize']}")

        return render(request, 'home.html', context)

    return render(request, 'home.html', {'form': form})
