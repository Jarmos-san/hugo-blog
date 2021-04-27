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

Google defines Cloud Run as "a fully managed service for deploying containerized applications". To be more specific, Cloud Run provides an API through Knative. The developer then can utilize the API to interact with the containerized instances. And under the hood Knative is just an open-source wrapper around Kubernetes which enables developers to host serverless infrastructure for themselves.

Do note, since Cloud Run utilizes Containers, you can basically use any programming language of your choice or a binary! The only thing stopping you would be if the image to build a specific container isn't available for download on the Internet. You can find more information on Cloud Run at: [cloud.google.com/run](https://cloud.google.com/run)

### App Engine

App Engine on the other hand is pretty much like renting out a server for yourself. The caveat being, the server is managed by someone else & it comes with every set of tools you would ever need. In other words, you have the freedom of choosing either one of the most popular programming languages or you could use something else of your choice.

So, you could build the backend of your application in Python & let App Engine take care of scaling it and/or integrating it with other services as well. And if you don't like Python for some reason, you could also use either Node.js, Golang, Ruby, C#, PHP or something else of your choice!

You can deliver you code using Docker containers & App Engine will do the rest. Besides that, App Engine also provides additional services like versioning your application & so on. Other similar integrated services involves traffic spliting, monitoring, etc.

So, as you can see App Engine is perfect for production applications which require a lot of resources. And certain situations wherein you would prefer to not manage backend servers & what not. You'll find more use cases of App Engine later on in the article.

For now you can find comprehensive details at: [cloud.google.com/appengine](https://cloud.google.com/appengine)

### Cloud Functions

GCP provides Cloud Functions on a "_Functions-as-a-Service_", as in modular pieces of code which are executed in response to certain events. So, if you're building an application based on a microservice architecture, this is the best option your money could buy.

And as is the case with most serverless infrastucture, Cloud Fundtions provides certain similara benefits as well. For example, increased development velocty, built-in scalability, hence the developer needn't worry about server maintenance.

Besides, Cloud Functions can be a less burden on your wallet as well. Since, Cloud Functions are priced based on how long the functions run, the number of times they're invoked & the extra resources provisioned for the functions.

The only drawback of using Cloud Functions though, is testing them. Since, you're obligated to "upload" you functions to GCP, it's hard to ensure quality of your functions. Thus, without a robust CI/CD pipeline to test & ensure quality of the functions, if your code breaks, things will go south faster than a Bugatti Veron.

That said, you can find more information on Cloud Functions on it's official page at: [cloud.google.com/functions](https://cloud.google.com/functions).

## Which Service Should You Use

And now for the question

## Final Words
