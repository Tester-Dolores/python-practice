from pydub import AudioSegment
from pydub.utils import make_chunks

# 音频处理(粗暴切割)
class TestPydub:
    @classmethod
    def setup_class(cls):
        cls.mp3_path = "./nnqdzj01_input.mp3"

    def test_pydub(self):
        """
        博文: https://www.cnblogs.com/Tester_Dolores/p/14846491.html
        功能: 使用pydub将音频平均分割为30s一块,并且采样率,声道数,解码器.
        可能存在的问题:
          1. 本地执行环境已配置ffmpeg,未知未配置ffmpeg是否可执行,若是失败,请自行配置ffmpeg.
          2. MP3文件请自行准备. 否则会报错"FileNotFoundError: [Errno 2] No such file or directory: './nnqdzj01_input.mp3'"
        """
        audio = AudioSegment.from_file(self.mp3_path, "mp3")

        size = 30000  # 切割的毫秒数 10s=10000

        chunks = make_chunks(audio, size)  # 将文件切割为30s一块

        for i, chunk in enumerate(chunks):
            chunk_name = "./nnqdzj01_out{}.wav".format(i)
            print(chunk_name)
            chunk.export(
                chunk_name,
                format="wav",
                parameters=["-ar", "16000", "-ac", "1", "-acodec", "pcm_s16le"],
            )
