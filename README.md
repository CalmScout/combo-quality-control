# COMBO project quality control
There is a huge interest in exploration of the efficacy of combination of different compounds to address one or another disease. To check the effect, wet lab experiment is needed.Different combinations of concentrations of compounds are stored in different wells that form a rectangle. And after some time in incubator the effect of those combinations is measured. However, not always experiment is successful due to technical issues. One of the brightest signs of failed experiment is very different values in neighbouring wells and the lack of "gradient" pattern. It makes sense, because the values in the plate are usually changing gradually. This makes a good fit for a pattern recognition approach for quality control of a such experiments.<br>

So idea of the approach in this project is the following:
1. Convert measurement results into images
2. Build an image classifier (fine-tune image-net pretrained architecture) to distinguish a pattern of successful experiment from a failed one.

This is only one of the approaches that can be used simultaneously in the pipeline of experiments quality control.

The data is unbalanced, because only 2% - 10% of the plates don't pass the quality control. Algorithm should be adaptable to different sizes of plates (standard plates consist of 384 or 96 wells, but it can change as technology changes). Idea behind the method is that all experiments have gradual change pattern due to organization of drugs concentration.<br>

TODO:
0. Clustering of existing based on their similarity with following visulalization.
1. Automatic detection of number of quadrants: can be 4, 2, 1.
2. Splitting of the plate into separete experiments based on the number of cuadrants.
3. Explore various ways to encode the `.csv` files into `.png` files. Compare performance of linear scale, log-scale conversions.