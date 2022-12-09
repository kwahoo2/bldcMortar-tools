# bldcMortar-tools

bldcMortar-tools is a configuration and testing tool for [bldcMortar-drive](https://github.com/kwahoo2/bldcMortar-drive) firmware and [bldcMortar-hardware](https://github.com/twizzter/bldcMortar-hardware) board. The bldcMortar package delivers a standalone BLDC motors driver with Bluetooth Low Energy communication. It is aimed for hobbyist and educational usage.

## Prerequisites

### Software Dependencies

* PySide6
* bleak

### Hardware

* The custom bldc-Mortar board

or

* a nRF52840-based board plus TI DRV10983 driver boards


## Installation and Usage

Install PySide6 and bleak modules.
```
pip install pyside6 bleak
```

Clone and run the script:

```
git clone https://github.com/kwahoo2/bldcMortar-tools
cd bldcMortar-tools
python bldcMortar-tools.py
```


![Main page][mortar-page1]

[mortar-page1]: https://raw.githubusercontent.com/kwahoo2/bldcMortar-tools/main/.github/images/mortar-page1.png "Main page of the tool"

![Motorparams page][mortar-page2]

[mortar-page2]: https://raw.githubusercontent.com/kwahoo2/bldcMortar-tools/main/.github/images/mortar-page2.png "Motorparams page of the tool"

![SysOpts page][mortar-page3]

[mortar-page3]: https://raw.githubusercontent.com/kwahoo2/bldcMortar-tools/main/.github/images/mortar-page3.png "SysOpts page of the tool"


## License

Check [LICENSE](LICENSE) for details.

