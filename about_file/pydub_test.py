from pydub import AudioSegment
from pydub.utils import make_chunks

# 音频处理(粗暴切割)
class TestPydub:
    @classmethod
    def setup_class(cls):
        cls.resource_path = "./wav/test.wav"

    def operate(self, resource_path, resource_format, to_format, split_size=0):
        resource = AudioSegment.from_file(resource_path, resource_format)
        output_key = resource_path.split("\\")[-1].split(".")[0]

        if split_size != 0:
            size = split_size * 1000  # 切割的毫秒数 10s=10000

            chunks = make_chunks(resource, size)  # 将文件切割为10s一块

            for i, chunk in enumerate(chunks):
                chunk_name = "./wav/temp{1}{0}.wav".format(i, output_key)
                print(chunk_name)
                chunk.export(
                    chunk_name,
                    format=to_format,
                    parameters=["-ar", "16000", "-ac", "1", "-acodec", "pcm_s16le"],
                )
        else:
            resource.apply_gain(+10)
            chunk_name = "./temp1/{}_out.wav".format(output_key)
            resource.export(
                chunk_name,
                format="wav",
                parameters=["-ar", "16000", "-ac", "1", "-acodec", "pcm_s16le"],
            )
            print(chunk_name)

    def test_pydub(self):
        """
        博文: https://www.cnblogs.com/Tester_Dolores/p/14846491.html
        功能: 使用pydub将音频平均分割为30s一块,并且采样率,声道数,解码器.
        可能存在的问题:
          1. 本地执行环境已配置ffmpeg,未知未配置ffmpeg是否可执行,若是失败,请自行配置ffmpeg.
          若是未配置可能报错"FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg': 'ffmpeg'"
        """
        self.operate(
            self.resource_path,
            self.resource_path.split("\\")[-1].split(".")[1],
            "wav",
            split_size=33,
        )
