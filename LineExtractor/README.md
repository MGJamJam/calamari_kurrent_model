# Line Extractor

The Line Extractor script extracts individual text lines from PageXML files and their corresponding image files. 
It saves each text line and its relevant information into separate files for further processing by an OCR engine.

## Usage Guide
### Setup
Clone the repository and go to the LineExtractor folder. Make sure you have `python` and `pip` installed. 

Run `pip install -r requirements.txt` to install all the necessary libraries. 

### Running the Script

Place your image files (`.png`) and corresponding PageXML files (`.xml`) in the input folder. Navigate to the `src` folder and run the Line Extractor script with `python3 main.py`.

#### Expected Input 
* Image Files: PNG images representing scanned text.
* PageXML Files: XML files containing the text line data. Ensure that each XML file has an `imageFilename` attribute pointing to the correct PNG file.

#### Expected Output: 
* Image Files: Separate PNG image files for each text line, saved in the output directory.
* XML Files: Updated PageXML files containing only the information for each individual text line, saved alongside the corresponding images.