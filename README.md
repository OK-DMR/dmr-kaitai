# DMR Kaitai protocols

This repository contains [Kaitai-IO](https://kaitai.io/) definitions of various protocols that can be met in DMR networks, both amateur and professional

## Contributing

Please follow these steps

  1. Add or update `.ksy` definition file
  2. Run re-compilation scripts (generate .py and format using *black* formatter)
  3. Provide at least one example dataset to check the implementation with

And specifically avoid these mistakes:

  1. Modifying generated python sources / dissectors

## Testing

Simply run `pytest` in the project root directory, that should pick up files `test_*.py` and run test methods named `test_*`

## License

AGPLv3.0 see LICENSE file for more info
