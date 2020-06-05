#still under progress

from pyomo.environ import ConcreteModel, Constraint, Objective, SolverFactory, TransformationFactory, Constraint, Var
from pyomo.network import Arc
from idaes.core import FlowsheetBlock
from idaes.generic_models.unit_models import Mixer, HeatExchanger, Separator, GibbsReactor, Heater
from idaes.generic_models.unit_models.separator import SplittingType
from idaes.generic_models.unit_models.heat_exchanger import delta_temperature_amtd_callback
from idaes.core.util.model_statistics import degrees_of_freedom as dof

import idaes.generic_models.properties.activity_coeff_models.methane_combustion_ideal as thermo_props

class SOFC_Modeling():
	def Initiation (self, )
	m = ConcreteModel()
	m.fs = FlowsheetBlock(default={"dynamic": False})
	m.fs.thermo_params = thermo_props.MethaneParameterBlock()

