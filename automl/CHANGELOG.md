# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-automl/#history

## 0.2.0

04-03-2019 09:16 PDT


### Implementation Changes
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))
- Sort generated classes (via synth). ([#7256](https://github.com/googleapis/google-cloud-python/pull/7256))
- Protoc-generated serialization update. ([#7074](https://github.com/googleapis/google-cloud-python/pull/7074))

### New Features
- Video Classification, Text Extraction, Text Sentiment, Tables support. ([#7650](https://github.com/googleapis/google-cloud-python/pull/7650))

### Documentation
- Updated client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))
- AutoML: pick up stub docstring fix in GAPIC generator. ([#6964](https://github.com/googleapis/google-cloud-python/pull/6964))

### Internal / Testing Changes
- Update copyright headers

## 0.1.2

12-17-2018 16:27 PST


### Implementation Changes
- Add protoc-generated descriptor changes from updated .proto files. ([#6899](https://github.com/googleapis/google-cloud-python/pull/6899))
- Import `iam.policy` from `google.api_core.iam.policy`. ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Pick up fixes in GAPIC generator. ([#6490](https://github.com/googleapis/google-cloud-python/pull/6490))
- Assorted synth fixups / cleanups ([#6400](https://github.com/googleapis/google-cloud-python/pull/6400))
- Fix client_info bug, update docstrings. ([#6404](https://github.com/googleapis/google-cloud-python/pull/6404))
- Re-generate library using automl/synth.py ([#5972](https://github.com/googleapis/google-cloud-python/pull/5972))
- Re-generate library using automl/synth.py ([#5946](https://github.com/googleapis/google-cloud-python/pull/5946))

### Dependencies
- Add 'mock' to unit test dependencies for autogen libs. ([#6402](https://github.com/googleapis/google-cloud-python/pull/6402))
- Bump minimum `api_core`' version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))
- Avoid broken 'google-common-apis 1.5.4' release. ([#6355](https://github.com/googleapis/google-cloud-python/pull/6355))

### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Harmonize / DRY 'README.rst' / 'docs/index.rst'. ([#6005](https://github.com/googleapis/google-cloud-python/pull/6005))
- Replace links to '/stable/' with '/latest/'. ([#5901](https://github.com/googleapis/google-cloud-python/pull/5901))

### Internal / Testing Changes
- Update noxfile.
- Blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- Omit local deps ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Unblack automl gapic and protos.
- Run Black on Generated libraries ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Add synth metadata. ([#6561](https://github.com/googleapis/google-cloud-python/pull/6561))
- Normalize use of support level badges ([#6159](https://github.com/googleapis/google-cloud-python/pull/6159))
- Add / fix badges for PyPI / versions. ([#6158](https://github.com/googleapis/google-cloud-python/pull/6158))
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))

## 0.1.1

### Documentation
- Fix broken links (#5675)
- bad trove classifier (#5648)

## 0.1.0

### New Features
- Initial Release of AutoML v1beta1

