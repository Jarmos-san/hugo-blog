---
title: "Deep Learning Vs Traditional Computer Vision Techniques — Which Should You Choose?"
date: 2020-08-13 23:46:37
category: Computer Vision
slug: deep-learning-vs-traditional-techniques-a-comparison
summary: Deep Learning(DL) techniques are beating the human baseline accuracy rates. Media is going haywire about AI being the next big thing. Everyone is writing a tutorial or two about building a startup or a product using DL. So should you board the hype train too?
description: Deep Learning(DL) techniques are beating the human baseline accuracy rates. Media is going haywire about AI being the next big thing. Everyone is writing a tutorial or two about building a startup or a product using DL. So should you board the hype train too?
cover:
  image: "https://miro.medium.com/max/1400/0*6SzpiBodhv9vNEXb"
  alt: "A MacBook beside an old typewriter"
  caption: "Photo by Glenn Carstens-Peters on Unsplash"
  relative: false
showtoc: true
---

[Deep Learning](https://en.wikipedia.org/wiki/Deep_learning) (DL) is undeniably one of the most popular tools used in the field of [Computer Vision](https://en.wikipedia.org/wiki/Computer_vision) (CV). It’s popular enough to be deemed as the current de facto standard for training models to be later deployed in CV applications. But is DL the only available option for us to develop CV applications? What about Traditional techniques that have served the CV community for an eternity? Has the time to move ahead & drop working on Traditional CV techniques all together in favour of DL arrived already? In this article, we try to answer some of these questions with comprehensive use-case scenarios in support of both DL & Traditional CV implementations.

## A Little Bit Of History First

The field of Computer Vision started gaining traction dating as far back as the late 1950s till the late 1960s when researchers wanted to teach computers “*to be…human*”. It was around this time when researchers tried to mimic the human visual system in order to achieve a new stepping stone to endow machines with human intelligence. Thanks to the extensive research being done back then, Traditional CV techniques like [Edge Detection](https://en.wikipedia.org/wiki/Edge_detection), [Motion Estimation](https://en.wikipedia.org/wiki/Motion_estimation), [Optical Flow](https://en.wikipedia.org/wiki/Optical_flow) were developed.

It wasn’t until the 1980s when [Convolutional Neural Networks](https://en.wikipedia.org/wiki/Convolutional_neural_network) (CNNs) were developed. Aptly named, the [Neocognitron](https://en.wikipedia.org/wiki/Neocognitron) which was the first CNN with the usual multilayered & shared weights [Neural Nets](https://en.wikipedia.org/wiki/Multilayer_perceptron) we see today. But the popularity of DL skyrocketed only after [LeNet](https://en.wikipedia.org/wiki/LeNet) was developed jointly by Yann LeCun & his colleagues in the 1990s. It was a pioneering moment since no other previous algorithms could ever achieve such an incredibly high accuracy as CNNs.

A decade and a half later, CNNs have made such vast developments, it even outperforms a human being with accuracy rates as high as 99% in the popular [MNIST dataset](https://en.wikipedia.org/wiki/MNIST_database)! [1] No wonder, it’s so easy to believe, CNNs would come down as a messiah for the CV community. But I doubt it happening any time soon.

CNNs & DL techniques come with certain caveats which when compared to older Traditional techniques might make the latter appear like a godsend gift for us mortals. And this article should throw some light into those differences. We’ll gradually dive deeper into what those differences are & how do they fare for certain use cases in the following sections.

## The Differences

To properly contemplate the differences between the two approaches — Deep Learning & Traditional techniques, I like to give an example of comparing an SUV and/or a hatchback. They’re both four-wheeler & an experienced driver can differentiate the pain-points as well as the ease-of-use for both the vehicles. While the hatchback might be preferable to drop your child to school & bring him/her back, the SUV would be perfect for cross-country travel if comfort & fuel efficiency is your concern. The vice-versa is possible but is probably not advisable, in general.

In this context, consider DL techniques the SUV among all ML tools for use in Computer Vision while the hatchback as the Traditional techniques. Similar to the difference in an SUV and the hatchback, DL & other Traditional techniques have merits-demerits too. So what are those differences? Let’s take a look at some of the prominent differences followed by a detailed description of the merits & demerits below.

The following infographic feature some of the differences between the two approaches very briefly.

![Deep Learning vs Traditional Techniques: An Infographic Comparison](https://miro.medium.com/max/700/0*veZFlekYYfy6Jt8F)

The infographic makes it so much more clear about why Deep Learning is getting all the attention. A quick glance & you’ll notice with *so many tick marks* obviously DL has to be the best approach among the two, right? But, is it really the case?

Let’s dig deeper & analyze the differences mentioned in the infographic.

1. **Requirement Of Manually Extracting Features From the Image By an Expert**: A major drawback of the first few Machine Learning algorithms created during the early 1960s was the requirement of painstaking manual feature extraction of the images. The little bit of automation employed back then also required careful tuning by an expert since algorithms like SVM and/or KNN were used to find the important features. This requirement meant building a dataset with set features for the model to learn from. Hence, DL techniques was a real life-saver for the practitioners, since no longer do they’ve to worry about manually selecting the features for the model to learn from.

2. **The Requirement of Heavy Computational Resources**: Deep Learning is a computationally heavy task which was why the mid-1950s barely saw any advancements in the field. Fast forward a few decades, with major advancements made in GPU capabilities & other related computational resources, this present time has never been more perfect for advancing DL research. But it comes with a caveat, bigger & better computational resources has a hefty price tag as well which might not be very pocket-friendly for most people & enterprises. Thus in context to easily available resources, the Traditional approach might look like a clear winner against Deep Learning.

3. **The Need For Huge Labeled Datasets**: We live at a point of time when every second thousand & thousands of petabytes of data are being created & stored globally. It must be good news then, right? Well sadly, contrary to popular belief, storing huge amounts of data, especially image data is neither economically viable nor does it portray a sustainable business opportunity. You would be surprised to know, often most enterprises are sitting on a gold mine of a dataset, yet either they don’t have to expertise to benefit from it or the business can’t get rid of them, legally. Hence, finding a useful, labelled & in-context dataset is no easy task which is why most often Deep Learning is an overkill approach for a simple CV solution.

4. **Black Box Models Which Are Difficult to Interpret**: Traditional approaches make use of easy to understand & interpret statistical methods like SVM & KNN to find features for resolving common CV problems. While on the other hand, DL involves using very complex layers of Multilayered Perceptrons(MLP). These MLPs extract informative features from the images by activating the relevant areas on the images which are often difficult to interpret. In other words, you’ll have no clue why certain areas of an image were activated while the other wasn’t.

5. **Small & Easy Enough to Be Shipped and/or Deployed Inside a Microprocessor**: Besides being computationally heavy, the model used in a DL approach are huge in size compared to other simple Traditional approaches. These models often vary from sizes of a few hundred megabytes to a gigabyte or two which is absolutely massive. While on the other hand, traditional approaches often output a model in sizes of just a few megabytes.

6. **How Accurate Are the Predictions From the Two Approaches**: One of the winning factors for DL to completely overshadow the achievements of the Traditional approaches is how extremely accurate the predictions are. It was a massive leap in the late 90s to the early 20s when Yann LeCunn & his colleagues came up with LeNet. It completely blitzed the previous accuracy rates made using Traditional approaches. Ever since then, DL has almost become the de facto go-to tool for any Computer Vision problems.

## Challenges Of Deep Learning Techniques

Although both DL & Traditional approaches have their trade-offs depending on certain use cases. Traditional approaches are more well established. DL techniques show promising results with incredibly high accuracy rates though. Without a doubt, DL based techniques are the poster child in the Computer Vision community. But DL techniques have their own set of drawbacks.

And in the following section, I describe a few of those challenges faced by the DL techniques comprehensively.

1. Deep Neural Networks(DNNs) are infamous for being computationally resource-heavy which is quite the contrast from Traditional techniques. Mixing both the techniques together can perhaps significantly reduce computation time & even half the bandwidth usage or even lesser!

2. Big Data is the loudest buzzword at the moment but in reality, useful data is hard to come by. Finding viable image data for training a DNN is a costly, difficult & time-consuming process.

3. With the advent of Cloud Computing services like GCP & other Cloud Machine Learning platforms like Google AI platform, high-performance resources are readily available at a click of a button. But the ease of access comes with a caveat, significant price build-ups. At first glance, a $3/hr high-performant GPU instance doesn’t sound too costly. But the expenditures build up over time as the business grows & DL techniques take a lot of time to train as well.

4. There are still certain fields of CV where DL techniques are yet to make any significant developments. Some of those fields include — 3D Vision, 360 Cameras, SLAM, among many others. Until & unless DL techniques make progress towards resolving problems in those sub-fields traditional techniques are here to stay for a long time. [2]_

5. Quite surprisingly certain individuals of the community appear to advocate a data-driven approach towards resolving most CV problems. “Just increase the dataset size” is common knowledge in the community as of writing this article. But quite contrary to the opinion, the fundamental problem at the root is quality data to train the models on. There’s a popular saying in the community right now, “Garbage In, Garbage Out”. So until & unless a proper alternative to the data-driven approach is discovered, current DNNs will not perform better than what they’re already capable of.

## Some Possible Solutions To the Aforementioned Challenges

Hybrid techniques can be leveraged extensively across various fields of implementation by using traditional techniques only on a portion of the computation process, while DNNs can be employed for identification and/or the classification process. In other words, the end-to-end ML job can be divided into CPU-bound jobs & GPU-bound jobs. For example, preprocessing on the CPU while training on the GPU.

As multi-threaded CPUs are becoming more common, I doubt it will take longer for a data pipeline which will make preprocessing before training a breeze by taking advantage of the multi-threaded environment. Besides, it is observed DNNs tend to be more accurate when the input data is preprocessed. Hence, it goes without saying, there’s a need for developing a system of data pipelines to be run on the CPU instead of the GPU.

Today, [Transfer Learning](https://en.wikipedia.org/wiki/Transfer_learning) or using a pre-trained model is almost the de facto standard for training a new Image Classifier and/or an Object Detection model. But the caveat is, this kind of model performs even better when the new input data are somewhat similar to that of the pre-trained model. So once again preprocessing on the input data on the CPU & then training with a pre-trained model can significantly reduce Cloud Computing expenditures without any loss in performance.

Employing a data-driven approach for certain business ventures might pay off in the future. But there’s always a logic-driven alternative albeit one which mightn’t sound very attractive. So sticking with age-old tried-and-tested logic-driven techniques cannot go wrong. Worst that could happen is you mightn’t make more money than you’re already earning.

## Wrapping Up

The developments made over the two decades in Deep Learning techniques for Computer Vision applications are no doubt enticing. I mean a research paper boasting of beating the human baseline on the MNIST dataset sounds amazing, almost futuristic. No wonder, some entrepreneurs out there with a sky-high vision would talk big about the next big thing with his/her product. But we shouldn’t forget the fact that the Machine Learning research community is facing a reproducibility crisis. [3] Researchers tend to just publish the best experiment out of many which worked as expected.

What does it mean for businesses & entrepreneurs looking forward to taking advantage of this supposedly bleeding-edge proofs-of-concept?

Simple, tread carefully.

Towards the end of the day, you’ll come back to employing Traditional techniques for your product anyway. The tried & tested techniques will almost always suit your needs.

So what’s the lesson here?

When in doubt stick to Traditional techniques, Deep Learning has a long way to go & will take another eternity to **REALLY** production-ready for your business.

### References

[1] Savita Ahlawat, Amit Choudhary, et al, [Improved Handwritten Digit Recognition Using Convolutional Neural Networks (CNN)](https://www.mdpi.com/1424-8220/20/12/3344/pdf) (2018), MDPI

[2] Nial O’ Mahony, et al, [Deep Learning Vs. Traditional Computer Vision](https://arxiv.org/ftp/arxiv/papers/1910/1910.13796.pdf), Institute of Technology Tralee (2019)

[3]  Shlomo Engelson Argamon, [People Cause Replication Problems, Not Machine Learning](https://www.americanscientist.org/blog/macroscope/people-cause-replication-problems-not-machine-learning) (2019), American Scientist (*accessed on 14th August 2020*)
