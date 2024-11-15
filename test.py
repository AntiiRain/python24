import numpy as np

def convolution(image, kernel):
  """
  实现二维卷积操作

  Args:
    image: 输入图像，numpy数组
    kernel: 卷积核，numpy数组

  Returns:
    卷积后的图像，numpy数组
  """

  # 获取图像和卷积核的尺寸
  image_height, image_width = image.shape
  kernel_height, kernel_width = kernel.shape

  # 计算输出图像的尺寸（假设使用valid填充）
  output_height = image_height - kernel_height + 1
  output_width = image_width - kernel_width + 1

  # 初始化输出图像
  output = np.zeros((output_height, output_width))

  # 进行卷积操作
  for i in range(output_height):
    for j in range(output_width):
      output[i, j] = np.sum(image[i:i+kernel_height, j:j+kernel_width] * kernel)

  return output

# 定义输入图像和卷积核
image = np.array([[10, 20, 20, 10],
                   [10, 20, 10, 0],
                   [10, 20, 10, 0],
                   [10, 20, 10, 0]])
kernel = np.array([[-1, 0, -1],
                   [ 0, 4,  0],
                   [-1, 0, -1]])

# 执行卷积操作
result = convolution(image, kernel)

print(result)

print(3840*2160)