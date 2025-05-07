from pytubefix import YouTube
from pytubefix.cli import on_progress
from slugify import slugify
import os
from pathlib import Path
import subprocess
import sys

def main():
    limpa_tela()

    url_yt: str = valida_url_yt()
    o_que_baixar: str = opcoes_audio_video()

    destino = Path.home() / ("Music" if o_que_baixar == "audio" else "Videos")
    yt: YouTube = YouTube(url_yt, on_progress_callback=on_progress)

    print(f"\nTítulo do vídeo: {yt.title}")
    print(f"Salvando em: {destino}")

    safe_title = slugify(yt.title)

    if o_que_baixar == "audio":
        audio_stream = yt.streams.filter(
            only_audio=True, file_extension='mp4').order_by('abr').desc().first()
        if not audio_stream:
            erro_sair("Stream de áudio não encontrado")

        audio_path = destino / f"{safe_title}_audio.mp4"
        print("Baixando áudio...")
        audio_stream.download(output_path=destino, filename=audio_path.name)

        if not audio_path.exists() or audio_path.stat().st_size == 0:
            erro_sair("Áudio não foi baixado corretamente")

        print(f"\n✅ Áudio salvo em: {audio_path}")
        sys.exit(0)

    video_streams = yt.streams.filter(
        adaptive=True, only_video=True, file_extension='mp4'
    ).order_by('resolution').desc()

    resolucoes = []
    print("\nEscolha a resolução de vídeo desejada:")
    for stream in video_streams:
        resolucao = stream.resolution
        if resolucao and resolucao not in resolucoes:
            resolucoes.append(resolucao)
            print(f"{len(resolucoes)} - {resolucao}")

    try:
        opcao = int(input("\nDigite o número da resolução desejada: ")) - 1
        resolucao_escolhida = resolucoes[opcao]
    except (IndexError, ValueError):
        print("❌ Opção inválida.")
        sys.exit(1)

    video_stream = yt.streams.filter(
        res=resolucao_escolhida, only_video=True, file_extension='mp4'
    ).first()
    audio_stream = yt.streams.filter(
        only_audio=True, file_extension='mp4'
    ).order_by('abr').desc().first()

    if not video_stream:
        erro_sair("Stream de vídeo não encontrado")
    if not audio_stream:
        erro_sair("Stream de áudio não encontrado")

    video_path = destino / f"{yt.video_id}_video.mp4"
    audio_path = destino / f"{yt.video_id}_audio.mp4"
    output_path = destino / f"{safe_title}_{resolucao_escolhida}.mp4"

    print(f"\nBaixando vídeo em {resolucao_escolhida}...")
    video_stream.download(output_path=destino, filename=video_path.name)

    print("Baixando áudio...")
    audio_stream.download(output_path=destino, filename=audio_path.name)

    if not video_path.exists() or video_path.stat().st_size == 0:
        erro_sair("Vídeo não foi baixado corretamente")
    if not audio_path.exists() or audio_path.stat().st_size == 0:
        erro_sair("Áudio não foi baixado corretamente")

    print("\nMesclando vídeo e áudio com FFmpeg...")
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
        print(f"\n✅ Vídeo final salvo em: {output_path}")
    except subprocess.CalledProcessError:
        erro_sair("Erro ao mesclar vídeo e áudio com FFmpeg")
    # erro quando FFmpeg não está instalado
    except FileNotFoundError:
        erro_sair("Verifique se está com FFmpeg instalado")

    os.remove(video_path)
    os.remove(audio_path)

def opcoes_audio_video():
    """ mostra as opções de download e retorna a opção escolhida """
    print("\nEscolha uma das opções de download :")
    print("\t1. somente áudio")
    print("\t2. vídeo com aúdio")
    opcao: str = input("\n >> ")

    if opcao not in ("1", "2"):
        erro_sair("Opção incorreta")

    return "audio" if opcao == "1" else "audio_video"

def erro_sair(msg: str):
    """ mostra a mensagem de erro e sair do prgrama """
    print(f"\n❌ {msg}.\n")
    sys.exit(1)

def valida_url_yt() -> str:
    """ valida a url para receber um link do YouTube válido """

    # link válido
    # https://www.youtube.com/watch?v=exemplo
    link_modelo: str = "https://www.youtube.com/watch?v="
    # link encurtado válido : https://youtu.be/exemplo
    link_curto: str = "https://youtu.be"

    url = input("Digite a URL do vídeo: ")

    if link_modelo in url or link_curto in url:
        return url

    erro_sair("Link inválido")

def limpa_tela():
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == "__main__":
    main()
