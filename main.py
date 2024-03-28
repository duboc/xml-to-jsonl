import xml.etree.ElementTree as ET
import json

def xml_to_jsonl(xml_file, jsonl_file):
    """Converts an XML file to JSONL format.

    Args:
        xml_file (str): Path to the XML file.
        jsonl_file (str): Path to the output JSONL file.
    """

    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(jsonl_file, 'w') as f:
        for item in root.findall('channel/item'):
            item_dict = {}
            for child in item:
                if child.tag.startswith('{http://base.google.com/ns/1.0}'):
                    tag = child.tag.split('}')[1]  # Remove namespace prefix
                else:
                    tag = child.tag
                item_dict[tag] = child.text

            f.write(json.dumps(item_dict) + '\n')

if __name__ == '__main__':
    xml_file = 'your_xml_file.xml'  # Replace with your XML file path
    jsonl_file = 'output.jsonl'  # Replace with your desired output path
    xml_to_jsonl(xml_file, jsonl_file)