from pytube import YouTube

def download_videos_from_file(filename):
    with open(filename, 'r') as file:
        links = file.readlines()

    for link in links:
        link = link.strip()
        try:
            youtube = YouTube(link)
            video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            if video:
                print(f"Baixando '{youtube.title}'...")
                video.download()
                print(f"Download de '{youtube.title}' concluído.")
            else:
                print(f"Vídeo não disponível em resolução máxima: '{youtube.title}'")
        except Exception as e:
            print(f"Erro ao baixar o vídeo '{link}': {e}")

if __name__ == "__main__":
    file_path = "links.txt"
    download_videos_from_file(file_path)
