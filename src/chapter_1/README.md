# Chapter 1: Introduction to Tensorflow

I’ve tinkered with TensorFlow and a few other ML tools before, but this project is all about learning the 
bigger picture. These are my notes and examples along the way — hopefully they’ll make it easier for anyone 
new to Python to follow along and pick up the core ideas.

Traditional Programming has limitations in which you utilize rules and data to return answers - this could be 
demonstrated with a basic if, else statement, in which you return a specific value. 

For example, you might want to have a game that needs to determine how bright the environment is 
in order to turn on streetlamps. This could be shown as something like this:

```python
streetlamp: bool = False
light: float = 1.50

if light > 1.00:
    streetlamp = False
elif light < 1.00:
    streetlamp = True
```

Traditional programming relies on rules you define to generate answers. Machine learning flips that logic — 
you give it the data and examples of the answers, and it figures out the rules for itself using pattern 
recognition and other algorithms.

