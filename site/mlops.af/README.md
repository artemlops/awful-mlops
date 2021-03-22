# Domain name proxy

In order to serve this static page `https://artemlops.github.io/awful-mlops/` as `mlops.af`, we need to run an nginx proxy.
Note that simply having a CNAME `mlops.af` -> `artemlops.github.io` would not work because, firstly, the URL path will remain, and secondly, domain's root [can't be a CNAME](https://www.freecodecamp.org/news/why-cant-a-domain-s-root-be-a-cname-8cbab38e5f5c/).

Thus, we run a small 1-replica nginx proxying all `https://mlops.af` to `https://artemlops.github.io/awful-mlops/`.
Since we already have a K8s cluster (thanks to [Neu.ro](https://neu.ro)), the easiest way is to deploy it there.
