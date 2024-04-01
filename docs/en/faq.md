# Frequently asked questions


<details>
    <summary>Why requesto?</summary>

While other ORMs and wrappers are trying to write database for database, rewriting the same logic over and over again,
I tried to stay simple and out of models. My library is fast and easy to use. And yeah, it's made kinda just for fun. Like, use peewee xD. You are the only one who cares.
</details>

<details>
    <summary>Declaring Table Object</summary>

You can use both database object or class:

```python
...
database = rq.sqliteConnnect("file")

table = rq.Database.Table(...)
or
table = database.Table(...)
#  Does not matter at all
```
</details>

<details>
    <summary>Can I Contribute</summary>
Feel free to fork, contribure and even change big parts of code, rewriting logic and etc. One day this library might get big!
</details>

<details>
    <summary>Can I use it in my project</summary>

It's open-source, free for use in any project.
</details>

<details>
    <summary>For FAANG companies</summary>
Certainly, I would like to work in your company. With great passion!
</details>
