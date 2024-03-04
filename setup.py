import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="top2vec_modified",
    packages=["top2vec_modified"],
    version="1.0.34",
    author="Dimo Angelov",
    author_email="dimo.angelov@gmail.com",
    description="Top2Vec learns jointly embedded topic, document and word vectors.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ddangelov/Top2Vec",
    keywords="topic modeling semantic search word document embedding",
    license="BSD",
    include_package_data=True,
    package_data={'top2vec_modified': ['*.yaml']},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy >= 1.20.0',
        'pandas',
        'pacmap',
        'scikit-learn >= 1.2.0',
        'gensim >= 4.0.0',
        'umap-learn >= 0.5.1',
        'hdbscan >= 0.8.27',
        'wordcloud',
    ],
    extras_require={
        'sentence_encoders': [
            'tensorflow',
            'tensorflow_hub',
            'tensorflow_text',
        ],
        'sentence_transformers': [
            'torch',
            'sentence_transformers',
        ],
        'indexing': [
            'hnswlib',
        ],
    },
    python_requires='>=3.8',
)
