# Awful MLOps

[mlops.af](https://mlops.af) is a compiled list of links to public **failure stories** related to MLOps.
The list is being constantly updated.
Most recent publications on top.

* [Why we switched from fluent-bit to Fluentd in 2 hours - PrometheusKube - blog post 2020](https://prometheuskube.com/why-we-switched-from-fluent-bit-to-fluentd-in-2-hours) 
    * involved: fluent-bit, missing logs, Fluentd
    * impact: lost application logs in production

* [What Happens to AI When the World Stops(COVID-19)? - High-level analytics page on Data Science stability](https://towardsdatascience.com/what-happens-to-ai-when-the-world-stops-covid-19-cf905a331b2f) (This is just an example from the world of BI)
    * involved: Data Science, COVID-19
    * impact: all failed

# Why

MLOps is a fairly new area of software development, which can be [defined](https://cloud.google.com/solutions/machine-learning/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) as "continuous delivery and automation pipelines in machine learning".
This tech field combines multiple different aspects such as ML and data pipelines, infrastructure management and DevOps, model management, and many other.
And since this area is being currently established, the tech community eagers for the real-world horror stories to learn from!

The idea to create such a page came up to us during the first Clubhouse meeting of the [AI Infrastructure Alliance](https://ai-infrastructure.org/) on March 1, 2021.
During the discussion, we came up to the conclusion that MLOps engineering community needs a collection of failure stories similar to [k8s.af](https://k8s.af/) for Kubernetes.

Please, don't be too much scared of these horror stories, they all end well 😉


# Contributing

Please help the community and **[share a link to your failure story by opening a Pull Request!](https://github.com/artemlops/awful-mlops/pulls)**
Failure stories can be anything like blog posts, conference/meetup talks, incident postmortems, tweetstorms, ...

# Thanks

Thanks to all contributors and everybody who writes public Kubernetes postmortems! 👏

Thanks to [k8s.af](https://k8s.af/) for the inspirational idea and site design! 👏

Thanks to [Neu.ro](https://neu.ro) for hosting [mlops.af](https://mlops.af)! 👏
