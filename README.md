# Calamari Kurrent Model

This repository contains the practical part of my Bachelor thesis. 
The goal is to train and evaluate an Handwritten Text Recognition (HTR) model using the OCR engine [calamari](https://github.com/Calamari-OCR/calamari) to recognizes 19th-century German Kurrent script. 

## Ground Truth Data

### Protokolle des Akademischen Senats (1799-1847)

The [Senatsprotokolle](GroundTruthData/Senatsprotokolle) folder contains transcriptions of the "Protokolle des Akademischen Senats" from Eberhard Karls Universität Tübingen during the period of 1799-1847. 

The data was sourced from https://github.com/ubtue/Ground-Truth/tree/main/Senatsprotokolle

#### Folder Structure
- **AnnotatedImages**: Contains JPEG images with the textline layout outlined in red created using the [LineExtractor tool](LineExtractor)
- **extracted_lines_UAT_047_15.zip**: Contains all 813 textline images along with their respective PAGE XML files, extracted from the original Images and PageXML [files](https://github.com/ubtue/Ground-Truth/tree/main/Senatsprotokolle/UAT_047_15) using the [LineExtractor tool](LineExtractor).
- **extracted_lines_UAT_047_19.zip**: Contains all 696 textline images along with their respective PAGE XML files, extracted from the original Images and PageXML [files](https://github.com/ubtue/Ground-Truth/tree/main/Senatsprotokolle/UAT_047_19) using the [LineExtractor tool](LineExtractor).
- **extracted_lines_UAT_047_19.zip**: Contains all 715 textline images along with their respective PAGE XML files, extracted from the original Images and PageXML [files](https://github.com/ubtue/Ground-Truth/tree/main/Senatsprotokolle/UAT_047_20a) using the [LineExtractor tool](LineExtractor).
- **extracted_lines_UAT_047_22.zip**: Contains all 692 textline images along with their respective PAGE XML files, extracted from the original Images and PageXML [files](https://github.com/ubtue/Ground-Truth/tree/main/Senatsprotokolle/UAT_047_22) using the [LineExtractor tool](LineExtractor).
- **extracted_lines_UAT_047_24.zip**: Contains all 1085 textline images along with their respective PAGE XML files, extracted from the original Images and PageXML [files](https://github.com/ubtue/Ground-Truth/tree/main/Senatsprotokolle/UAT_047_24) using the [LineExtractor tool](LineExtractor).
- **extracted_lines_UAT_047_25.zip**: Contains all 854 textline images along with their respective PAGE XML files, extracted from the original Images and PageXML [files](https://github.com/ubtue/Ground-Truth/tree/main/Senatsprotokolle/UAT_047_25) using the [LineExtractor tool](LineExtractor).
- **extracted_lines_UAT_047_28_1.zip**: Contains 1799 textline images along with their respective PAGE XML files, extracted from the original Images and PageXML [files](https://github.com/ubtue/Ground-Truth/tree/main/Senatsprotokolle/UAT_047_28) using the [LineExtractor tool](LineExtractor).
- **extracted_lines_UAT_047_28_2.zip**: Contains 1862 textline images along with their respective PAGE XML files, extracted from the original Images and PageXML [files](https://github.com/ubtue/Ground-Truth/tree/main/Senatsprotokolle/UAT_047_28) using the [LineExtractor tool](LineExtractor).

#### Dataset Overview
- **Pages**: 229 pages from seven volumes.
- **Textlines**: 8_516 textlines.
- **Words**: 37_313 words.
- **Characters**: 235_612 characters.

#### Script and Layout
- **Script**: Mostly Kurrent by different scribes.
- **Layout**: Text regions and baselines are manually corrected.

#### Transcription guidelines 
All transcriptions were created using Transkribus. The transcription rules are based on the OCR-D transcription guidelines Level 2

#### Sources
The transcriptions are based on digitized material available through OpenDigi from the University Library of Tübingen. Below are the specific volumes referenced:

- [Protokolle des Akademischen Senats Band 63, UAT_047_15](https://opendigi.ub.uni-tuebingen.de/opendigi/UAT_047_15#p=1)
- [Protokolle des Akademischen Senats Band 67, UAT_047_19](https://opendigi.ub.uni-tuebingen.de/opendigi/UAT_047_19#p=1)
- [Protokolle des Akademischen Senats Band 69, UAT_047_20a](https://opendigi.ub.uni-tuebingen.de/opendigi/UAT_047_20a#p=1)
- [Protokolle des Akademischen Senats Band 71, UAT_047_22](https://opendigi.ub.uni-tuebingen.de/opendigi/UAT_047_22#p=1)
- [Protokolle des Akademischen Senats Band 73, UAT_047_24](https://opendigi.ub.uni-tuebingen.de/opendigi/UAT_047_24#p=1)
- [Protokolle des Akademischen Senats Band 74, UAT_047_25](https://opendigi.ub.uni-tuebingen.de/opendigi/UAT_047_25#p=1)
- [Protokolle des Akademischen Senats Band 77, UAT_047_28](https://opendigi.ub.uni-tuebingen.de/opendigi/UAT_047_28#p=1)


### Test Set: Minutes of the Swiss Federal Council (1848-1903)
- **Description:** The data set consists of extracts of the minutes of the Swiss Federal Council. 
- **Citation:** Hodel, T., & Schoch, D. (2021). Handwritten Text Recognition Test Set: Minutes of the Swiss Federal Council (1848-1903) (1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4746342
