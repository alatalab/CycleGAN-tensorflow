<!-- <img src='imgs/horse2zebra.gif' align="right" width=384> 

<br><br><br>
-->
# CycleGAN

Tensorflow implementation for learning an image-to-image translation **without** input-output pairs.
The method is proposed by [Jun-Yan Zhu](https://people.eecs.berkeley.edu/~junyanz/) in 
[Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networkssee](https://arxiv.org/pdf/1703.10593.pdf). 
For example in paper:

<img src="imgs/teaser.jpg" width="1000px"/>


This is modified model for human<->map

Every human is unique and complicated, so as a city.

Human database - custom big face crops from celebA, map databases - cities with population >10k on Google Maps.


Changes added by Sergei to original model - skip-connection, low L1 (cycle), bug fixing, depth2space instead of deconv.
