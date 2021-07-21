import GPUtil


class TestGPUtil:
    def get_gpu_info(self):
        """
        :return:
        """
        gpulist = []
        Gpus = GPUtil.getGPUs()
        GPUtil.showUtilization()

        # 获取多个GPU的信息，存在列表里
        for gpu in Gpus:
            # 按GPU逐个添加信息
            gpulist.append(
                [
                    "驱动:",
                    gpu.driver,
                    "gpu.id:",
                    gpu.id,
                    "显存总量：",
                    gpu.memoryTotal,
                    "显存使用量：",
                    gpu.memoryUsed,
                    "显存使用占比:",
                    gpu.memoryUtil * 100,
                    "GPU使用占比:",
                    gpu.load * 100,
                    "display_mode:",
                    gpu.display_mode,
                    "display_active:",
                    gpu.display_active,
                    "温度：",
                    gpu.temperature,
                ]
            )

    def test_get_gpu_info(self):
        print(self.get_gpu_info())
