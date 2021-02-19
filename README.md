# CArgs

`curl` argument generator

```bash
cargs example.com POST

>>> -XPOST example.com
```

```bash
cargs example.com POST foo=bar bar=baz

>>> -XPOST -Ffoo=bar -Fbar=baz example.com
```

```bash
curl `cargs example.com PUT foo=bar bar=baz`
```

