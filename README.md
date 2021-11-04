# DMR Kaitai protocols

This repository contains [Kaitai-IO](https://kaitai.io/) definitions of various protocols that can be met in DMR networks, both amateur and professional

## Contributing

Please follow these steps

  1. Add or update `.ksy` definition file
  2. Run re-compilation script `./rebuild-all.sh` (generates .py from .ksy and formats them using *black* formatter)
  3. Provide at least one example dataset to check the implementation with

And specifically avoid these mistakes:

  1. Modifying generated python sources / dissectors after generating

## Testing

run `make test` (or pytest directly like this `env PYTHONPATH=. pytest -vrpP`)

## License

AGPLv3.0 see LICENSE file for more info
