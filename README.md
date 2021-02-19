# CArgs

`curl` argument generator

```bash
cargs example.com POST
```

Output:

```bash
-XPOST example.com
```

```bash
cargs example.com POST foo=bar bar=baz

```

Output:

```bash
-XPOST -Ffoo=bar -Fbar=baz example.com
```

```bash
curl `cargs example.com PUT foo=bar bar=baz`
```

