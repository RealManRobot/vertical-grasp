from setuptools import setup

setup(
    name="vertical_grab",
    version="0.1.0",
    description='该sdk是为了更方便的连接相机而封装的一个sdk。它可以很方便的帮我们初始化相机对象，获取相机的深度图像和rgb图像流。',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="http://192.168.0.188:8090/ai_lab_rd02/ai_sdks/vertical_grab.git",
    packages=["vertical_grab"],
    install_requires=["scipy", "opencv-python", "numpy"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.8',
    include_package_data=True,
    zip_safe=False,
)
