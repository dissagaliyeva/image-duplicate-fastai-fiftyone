# Image duplicate finder with FiftyOne and FastAI
Colab code: <a href="https://colab.research.google.com/drive/1qasxsy-yErhTt9LP0VH197yXkqkc8xNe?usp=sharing">link</a> <br>
Project folder: <a href="https://drive.google.com/drive/folders/1Ces2VpC1WN3fE0HQQ1yfxZIBcQ06xAuF?usp=sharing">link</a> <br>

Working with images requires very careful analysis. There are a lot of things that can go wrong, and today we will be covering the idea of duplicates. I know it might be tempting to go over the images one by one if you have a fairly small dataset. However, let’s be honest — it’s quite a tedious and prone-to-error approach.

This notebook provides a complete solution that tackles the following tasks:
- Gather and clean data
- Create and remove duplicates both automatically and manually 
- Train CNN model with ResNet50
- Analyze misclassifications
