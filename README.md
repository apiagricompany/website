# ApiAgri website

This is a develop branch.

To start contributing, first checkout main repository:
```console
$ git clone https://apiagricompany@bitbucket.org/apiagricompany/website.git
```

After that, enter master branch and checkout `source` branch:
```console
$ cd website
$ git checkout -b source
```

Change your stuff. If you have commit authorization to master, just do:
```console
$ make publish && make github
```

Otherwise please create a push request. Do not forget to commit and push your changes on source to the `source` branch.
