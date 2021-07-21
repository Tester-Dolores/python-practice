import ffmpeg

# 音频处理(格式)
class TestFFmpegPython:
    """
    博文: https://www.cnblogs.com/Tester_Dolores/p/14846491.html
    功能:
      使用ffmpeg-python设置采样率,声道数,解码器.
      test_001和test_002本质上没什么区别,只是写法不同.
    可能存在的问题:
      1. 本地执行环境已配置ffmpeg,未知未配置ffmpeg是否可执行,若是失败,请自行配置ffmpeg.
      若是未配置可能报错"FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg': 'ffmpeg'"
    """

    @classmethod
    def setup_class(cls):
        cls.resource_path = "./wav/test.wav"

    def test_001(self):
        (
            ffmpeg.input(self.resource_path)
            .output(
                "./wav/testout1.wav",
                **{"ar": "16000", "ac": "1", "acodec": "pcm_s16le"}
            )
            .run()
        )

    def test_002(self):
        stream = ffmpeg.input(self.resource_path)
        # stream = ffmpeg.hflip(stream)
        stream = ffmpeg.output(
            stream,
            "./testout2.wav",
            **{"ar": "18000", "ac": "1", "acodec": "pcm_s16le"}
        )
        ffmpeg.run(stream)
