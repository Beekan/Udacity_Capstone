# Udacity_Capstone
AWS cloud devops nanodegree capstone

## Cluster intialization

The cluster is intialized using
```
eksctl create cluster --name capstonebeeko --region us-west-2 --with-oidc --ssh-access --ssh-public-key MiniProject2 --managed
```


The jenkins server is configured manually.

## Updates

The update strategy is a rolling update. The instances are not changed, rather the pods within these instances do. In the images folder the output of the container changed after a period of time as the update was integrated.
