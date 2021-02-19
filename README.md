# CArgs

`curl` argument generator

## How to use

```bash
curl `cargs example.com PUT foo=bar bar=baz`
curl `cargs example.com POST -c json {foo: "bar"}`
```

### HTTP From

```bash
cargs example.com POST foo=bar bar=baz

```

Output:

```bash
-XPOST -Ffoo=bar -Fbar=baz example.com
```

### Help?

```bash
cargs --help
```

