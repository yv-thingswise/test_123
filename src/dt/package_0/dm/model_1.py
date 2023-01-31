from digital_machine import *
from digital_machine.templates import simple
from digital_machine.templates import templates as t

class model_1(simple.SimpleClassTemplate):
  
  @t.model(invocation_frequency='5s')
  @t.input(
    features={
      'group_test': {
        'group': 'domain_0.group_0',
        'aggregation': '5s',
        'aggregation_func': 'avg'
      }
    }  
  )
  @t.output(
    features={
      'output': {
        'metric': 'domain_0.output',
        'aggregation': '5s',
        'aggregation_func': 'avg'
      }
    }
  )
  def model_yv(self, input, output):
    print('model_yv invoked with inputs: ', input.data)
    print('model_yv invoked with outputs: ', output.data)
    
    output.data['output'] = input.data['group_test']['group_0']
    