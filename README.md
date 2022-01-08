# Image duplicate finder with FiftyOne and FastAI
Medium article: <a href="https://medium.com/@dissagaliyeva/image-duplicate-finder-with-fiftyone-and-fastai-217c26ef3802#8a97">link</a> <br>
Colab code: <a href="https://colab.research.google.com/drive/1qasxsy-yErhTt9LP0VH197yXkqkc8xNe?usp=sharing">link</a> 

Working with images requires very careful analysis. There are a lot of things that can go wrong, and today we will be covering the idea of duplicates. I know it might be tempting to go over the images one by one if you have a fairly small dataset. However, let’s be honest — it’s quite a tedious and prone-to-error approach.

This notebook provides a complete solution that tackles the following tasks:
- Gather and clean data
- Create and remove duplicates both automatically and manually 
- Train CNN model with ResNet50
- Analyze misclassifications
