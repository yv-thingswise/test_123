
import digital_machine
import digital_machine.templates as tmpl
from digital_machine import dmCompile

from .model_1 import model_1
from .model_0 import model_0


try:
    from ._legacy import models as legacy_models
except ModuleNotFoundError:
    legacy_models = {}

py_model_collection = tmpl.PyModelCollection()



model_1().generate_model(digital_machine.digital_twin_model("package_0", "model_1"), py_model_collection)
model_0().generate_model(digital_machine.digital_twin_model("package_0", "model_0"), py_model_collection)


models = py_model_collection.models
models.update(legacy_models)
