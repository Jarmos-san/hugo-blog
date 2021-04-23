---
title: "Google Serverless Infrastructure: A Detailed Overview of the Serverless Service"
date: 2021-04-19T10:50:28+05:30
slug: deatails-of-google-serverless-infrastructure
category: "Cloud Computing"
summary: A detailed overview of all the available Google Cloud Serverless services.
description: A detailed overview of all the available Google Cloud Serverless services.
covers:
  image:
  alt:
  caption:
  relative: false
showtoc: true
draft: true
---

Have you ever wondered how do you showcase your latest Machine Learning project to the rest of the world? Or perhaps, you are a full-time Machine Learning practitioner & you want to deploy your product to the Internet. The product which would accessed through a ReST API. How would you do that?

Well short answer is; Rent out a Virtual Private Server (VPS) on Digital Ocean or Linode or any VPS service provider of your choice. And then set up your projects on the server. It's quite doable & is nothing out of the ordinary but it comes with a compromise. You would've to take care of securing it, manage dependencies & what not. Basically, you would've to have DevOps knowledge just to showcase your project to the rest of the world.

If you ask me, that's quite a lot of work to do! And I would rather focus on ensuring my product's end-users are having the better experience rather than focus on maintaining servers. And for people like me, I bring some good news: _Serverless Computing_.

And to be more specific, this article is all about _Google's Serverless Computing_ infrastructure.

## What is Serverless Computing

There's a lot of buzz about "_Serverless architecture_", "_Serverless this-and-that_". Filtering out the buzz & understanding the core concepts of Serverless Computing first is important to maintain your project properly. So, let's understand what Serverless Computing is all about.

Here's a brief description of the concept from Wikipedia;

{{< blockquote link="https://en.wikipedia.org/wiki/Serverless_computing" author="Source:">}}
  Serverless computing is a cloud computing execution model in which the cloud provider allocates machine resources on demand, taking care of the servers on behalf of their customers. [...] When an app is not in use, there are no computing resources allocated to the app. Pricing is based on the actual amount of resources consumed by an application. [...] "Serverless" is a misnomer in the sense that servers are still used by cloud service providers to execute code for developers. However developers of serverless applications are not concerned with capacity planning, configuration, management, maintenance, operating or scaling of containers, VMs, or physical servers.
{{< /blockquote >}}

So, reiterating on the information shared on Wikipedia, here's what you should know about Serverless Computing:

1. The cloud service providers (_like Google Cloud Platform, Amazon Web Services & Azure_) offer a range of serverless services wherein they dynamically manage all required resources for your project.
2. Pricing is based only the specific amount of resources used by the project. Hence, often times it's cheaper to use Serverless Computing over renting out an actual server.
3. The developers needn't worry about the state of the servers. They can focus on developing their products & leave the responsibility of maintaining the servers to the Cloud Service Providers.

Now that you understand what serverless computing is, let's dive deeper into what Google offers as part of their Serverless Computing services.

## Google's Serverless Computing Solutions

Google Cloud Platform (GCP) provides three serverless computing services; namely:

1. Cloud Run
2. Cloud Functions
3. App Engine

While each of these services might look pretty much the same on face value, they're not. Their specific use cases differs, the programming language to use with them varies as well. So, let's check out how, when & why you might want to use any of these services.

### Cloud Run

Google defines Cloud Run as "a fully managed service for deploying containerized applications". To be more specific, More information available at: https://cloud.google.com/run

### Cloud Functions

Functions-as-a-Service (FaaS) service which scales dynamically as & when needed but with no server maintenance requirements. More information at: https://cloud.google.com/functions

### App Engine

A more comprehensive service for deploying web applications. More information available at: https://cloud.google.com/appengine

## Which Serverless Service to Use & When

## Final Words
