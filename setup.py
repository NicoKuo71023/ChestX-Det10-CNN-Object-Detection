from setuptools import setup, find_packages

setup(
    name='chestCNN_ref',
    version='1.1',
    
    packages=find_packages(),  # 自動尋找模組
    install_requires=[  # 列出所有需要的依賴
        'torch'
        
        # 其他依賴...
    ],
)
