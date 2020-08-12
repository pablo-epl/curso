import unittest
import json

import jsonschema

'''#

# name: test_gene	Version 1.0

## synopsis

```python

```

## examples

```python
python -m unittest test_gene.py
```

## description
Programa que valida el esquema de gene

## arguments


## requirements


## softwareRequirements
json
unittest
jsonschema

## memoryRequirements
N/A

## storageRequirements
N/A

* __Input Format - __ __gene.json__ Schema del gene

## output

* __String - __ __Tests__ Resultado de los tests

__Return:__

N/A

## [Program Code]

#'''

class TestGene(unittest.TestCase):

    def setUp(self):
        """
        Carga todo lo necesario para los tests
        """
        with open("../schemas/gene.json", 'r') as gene_schema_fp:
            gene_schema_json = gene_schema_fp.read()
            self.gene_schema = json.loads(gene_schema_json)["gene"]["validator"]["$jsonSchema"]

        with open("../data/correct_data/gene.json") as gene_data_fp:
            gene_data_json = gene_data_fp.read()
            self.gene_data = json.loads(gene_data_json)["gene"]

        with open("../data/wrong_data/gene.json", 'r') as gene_id_wrong_data_fp:
            self.gene_id_wrong = json.loads(gene_id_wrong_data_fp.read())["wrong_id"]

        with open("../data/wrong_data/gene.json", 'r') as gene_sequence_wrong_data_fp:
            self.gene_sequence_wrong = json.loads(gene_sequence_wrong_data_fp.read())["wrong_sequence"]

    def test_gene_schema(self):
        '''#

        ### test_gene_schema

        __description:__

        test del gene_schema
        #'''
        try:
            jsonschema.Draft4Validator.check_schema(self.gene_schema)
        except jsonschema.exceptions.SchemaError:
            self.fail("Gene schema written incorrectly")

    def test_gene_data_against_gene_schema(self):
        """
        Testea la información del gene contra el esquema definido previamente
        """
        try:
            for gene_object in self.gene_data:
                jsonschema.validate(instance=gene_object, schema=self.gene_schema,
                                    format_checker=jsonschema.draft4_format_checker)
        except jsonschema.exceptions.ValidationError:
            self.fail("Gene data does not map against the gene schema")

    def test_gene_data_object_when_id_is_wrong(self):
        """
        """
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            jsonschema.validate(instance=self.gene_id_wrong, schema=self.gene_schema,
                                format_checker=jsonschema.draft4_format_checker)
            self.fail("Pattern from _id property did not raise an exception")

    def test_gene_when_sequence_has_not_valid_nucleotides(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            jsonschema.validate(instance=self.gene_sequence_wrong, schema=self.gene_schema,
                                format_checker=jsonschema.draft4_format_checker)
            self.fail("Pattern from sequence property did not raise an exception")


if __name__ == '__main__':
    unittest.main()