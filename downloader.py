import os
import subprocess
import sys
from pathlib import Path
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix.exceptions import BotDetection
from slugify import slugify

def main():
    limpa_tela()

    url_yt: str = recebe_valida_url()
    o_que_baixar: str = menu_audio_video()

    destino = Path.home() / ("Music" if o_que_baixar == "audio" else "Videos")
    yt: YouTube = YouTube(url_yt, on_progress_callback=on_progress)

    limpa_tela()
    try:
        print(f"\nTítulo do vídeo a ser baixado :\n\n\t {yt.title}")
    except BotDetection:
        msg: str = "Aparentemente você foi bloqueado por excesso de downloads."
        msg += "\n\nAcesse o link abaixo para mais informações :\n\n\t"
        msg += "https://github.com/JuanBindez/pytubefix/pull/209"
        erro_sair(msg)

    titulo_slug:str = slugify(yt.title)

    if o_que_baixar == "audio":
        audio_path = baixa_audio(yt, destino, titulo_slug)
        limpa_tela()
        print(f"\n✅ Áudio salvo em :\n\n\t{audio_path}.")
    elif o_que_baixar == "video":
        video_path, resolucao = baixa_video(yt, destino, titulo_slug)
        limpa_tela()
        print(f"\n✅ Vídeo salvo em :\n\n\t{video_path}.")
    else:
        video_path, resolucao = baixa_video(yt, destino, titulo_slug)
        audio_path = baixa_audio(yt, destino, titulo_slug)

        output_path = destino / f"{titulo_slug}-{resolucao}.mp4"
        junta_audio_video(audio_path, video_path, output_path)
        limpa_tela()
        print(f"\n✅ Vídeo final salvo em :\n\n\t{output_path}")

# funções de download
def baixa_audio(yt: YouTube, destino: Path, titulo: str):
    """ função para baixar apenas o áudio """
    audio_stream = yt.streams.filter(
        only_audio=True, file_extension='mp4').order_by('abr').desc().first()
    if not audio_stream:
        erro_sair("Stream de áudio não encontrado")

    audio_path = destino / f"{titulo}-audio.mp3"
    print("\nBaixando áudio...")
    audio_stream.download(output_path=destino, filename=audio_path.name)

    if not audio_path.exists() or audio_path.stat().st_size == 0:
        erro_sair("Áudio não foi baixado corretamente")

    return audio_path

def baixa_video(yt: YouTube, destino: Path, titulo: str):
    """ função para baixar apenas o vídeo """
    video_streams = yt.streams.filter(
        adaptive=True, only_video=True, file_extension='mp4'
    ).order_by('resolution').desc()

    resolucao_escolhida: str = menu_resolucoes(video_streams)

    video_stream = yt.streams.filter(
        res=resolucao_escolhida, only_video=True, file_extension='mp4').first()

    if not video_stream:
        erro_sair("Stream de vídeo não encontrado")

    video_path = destino / f"{titulo}-video.mp4"

    print(f"\nBaixando vídeo em {resolucao_escolhida}...")
    video_stream.download(output_path=destino, filename=video_path.name)

    if not video_path.exists() or video_path.stat().st_size == 0:
        erro_sair("Vídeo não foi baixado corretamente")

    return video_path, resolucao_escolhida

def junta_audio_video(video_path, audio_path, output_path):
    print("\n\nMesclando vídeo e áudio com FFmpeg...")
    ffmpeg_cmd = [
        "ffmpeg",
        "-y",
        "-i", str(video_path),
        "-i", str(audio_path),
        "-c:v", "copy",
        "-c:a", "aac",
        "-strict", "experimental",
        str(output_path)
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
    except subprocess.CalledProcessError:
        erro_sair("Erro ao mesclar vídeo e áudio com FFmpeg")
    # erro quando FFmpeg não está instalado
    except FileNotFoundError:
        erro_sair("Verifique se está com FFmpeg instalado")

    os.remove(video_path)
    os.remove(audio_path)

# funções de menu
def menu_resolucoes(streams) -> str:
    """ menu das resoluções disponíveis do vídeo """
    print("\nEscolha uma resolução da lista abaixo : ")
    resolucoes: list[str] = []
    for stream in streams:
        resolucao = stream.resolution
        if resolucao and resolucao not in resolucoes:
            resolucoes.append(resolucao)
            print(f"\t{len(resolucoes)}. {resolucao}")
    print("\t0. encerrar")
    opcao = input(" >> ")

    while True:
        try:
            opcao = int(opcao)
            if opcao == 0:
                encerrar()
            elif 0 < opcao <= len(resolucoes):
                return resolucoes[opcao - 1]
        except ValueError:
            pass

        print("\nOpção inválida. Digite novamente.")
        opcao = input(" >> ")

def menu_audio_video():
    """ mostra as opções de download e retorna a escolhida """
    print("\nEscolha uma das opções de download :")
    print("\t1. somente áudio")
    print("\t2. somente vídeo")
    print("\t3. vídeo com áudio")
    print("\t0. encerrar")
    opcao: str = input("\n >> ")

    while opcao not in ("0", "1", "2", "3"):
        print("\nOpção inválida. Digite novamente.")
        opcao = input(" >> ")

    if opcao == "0":
        encerrar()
    elif opcao == "1":
        return "audio"
    elif opcao == "2":
        return "video"
    return "audio_video"

def recebe_valida_url() -> str:
    """ recebe e valida a url para receber um link do YouTube válido """
    # link válido : https://www.youtube.com/watch?v=exemplo
    link_modelo: str = "https://www.youtube.com/watch?v="
    # link encurtado válido : https://youtu.be/exemplo
    link_curto: str = "https://youtu.be"

    print("Digite a url conforme um dos modelos abaixo (0 para encerrar) : ")
    print(f"\t - {link_modelo}exemplo")
    print("\t ou")
    print(f"\t - {link_curto}/exemplo")
    url = input("\n >> ")

    while link_modelo not in url and link_curto not in url and url != "0":
        print("\nLink inválido. Digite novamente.")
        url = input(" >> ")

    if url == "0":
        encerrar()

    # remove o conteúdo do link após o identificador do vídeo
    # https://youtu.be/exemplo?t=123, https://youtu.be/exemplo?si=codigo, etc
    if link_curto in url:
        return url.split("?")[0]

    # https://www.youtube.com/watch?v=exemplo&list=WL&index=1&t=251s
    return url.split("&")[0]

# funções do sistema
def limpa_tela():
    os.system('cls' if os.name=='nt' else 'clear')

def erro_sair(msg: str):
    """ mostra a mensagem de erro e sair do prgrama """
    print(f"\n❌ {msg}.\n")
    sys.exit(1)

def encerrar():
    """ função para encerrar o programa de forma amigável """
    limpa_tela()
    print("\n\tEncerrando o programa.\n")
    sys.exit()

if __name__ == "__main__":
    main()
