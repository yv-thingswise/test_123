from digital_machine import *
from digital_machine.templates import simple
from digital_machine.templates import templates as t

class model_1(simple.SimpleClassTemplate):
  
    @t.model(invocation_frequency='5s')
    @t.input(
        features={
            # You can access groups like this
            'temperature_test': {
                'group': 'domain_0.temperature',
                'aggregation': '5s',
                'aggregation_func': 'avg',
            },
            # You can also do it with source
            'source_temp': {
                'source': {
                    'group': 'domain_0.temperature',
                },
                'interpolation': 'fill',
            },
            # Non numeric groups are aslo supported
            'string_group': {'group': 'domain_0.string_group'},
            # You also can access group items
            'string_val': {'metric': 'domain_0.string',},
            'ceiling': {
                'metric': 'domain_0.ceiling',
                'aggregation': '5s',
                'aggregation_func': 'avg',
            }
        }
    )
    @t.output(
        features={
            # NOTE: group metrics cannot be used in output features
            'output_temperature': {
                'metric': 'domain_0.output',
                'aggregation': '5s',
                'aggregation_func': 'avg',
            }
        }
    )
    def model0(self, input, output):
        
        # You can access group features like this. They will contain
        # each group item and aggregated value
        # print(input.data['temperature_test'])  # {'ceiling': 10, 'floor': 8, 'temperature': 9}
        
        # # Group added with source will have same values inside
        # print(input.data['source_temp'])  # {'ceiling': 10, 'floor': 8, 'temperature': 9}
    
        # # Non numeric groups are also supported, but such groups won't
        # # contain aggregated value as it is not applicable
        # print(input.data['string_group'])  # {'string': 'test', 'string1': 'test'1}
    
        # # Group items accessed as usual
        # print(input.data['string'])  # 'test'
        # print(input.data['ceiling'])  # 10
        
        # output.data['output_temperature'] = input.data['temperature_test']['temperature']
        pass
