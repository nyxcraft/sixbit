# sixbit

A framework for recreating original PDP-10 software in Python. Classic programs
run from their original FORTRAN-10 source on the forterp interpreter.

> **Status: pre-alpha.** This release establishes the package name and layout.
> The interpreter integration and the individual programs land in subsequent
> versions.

## Namespace

`sixbit` is a [PEP 420](https://peps.python.org/pep-0420/) namespace package.
This distribution provides `sixbit.core`; individual programs ship as their own
sibling distributions that add to the shared namespace:

| Distribution | Import path | Contents |
|--------------|-------------|----------|
| `sixbit` | `sixbit.core` | shared foundation (this package) |
| `sixbit-empire` | `sixbit.games.empire` | Empire (Walter Bright, 1978) |
| `sixbit-decwar` | `sixbit.games.decwar` | DECWAR (UT Austin, 1979) |
| `sixbit-advent` | `sixbit.games.advent` | Colossal Cave Adventure |

Installing a program distribution drops its subpackage into `sixbit.games.*`
alongside whatever else is installed -- no top-level `sixbit` package owns the
namespace, so the pieces compose freely.

The historical programs are *not* redistributed here; each program package
documents how to fetch its original source.

## Install

```
pip install sixbit
```

## License

MIT. See [LICENSE](LICENSE).
