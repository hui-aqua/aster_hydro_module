from forces import morisonModel as morisonModel
from forces import screenModel as screenModel
from weakEffects import weakModel as wakeModel
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

row = 1025  # [kg/m3]   sea water density
kinematic_viscosity = 1.004e-6  # when the water temperature is 20 degree.
dynamic_viscosity = 1.002e-3  # when the water temperature is 20 degree.

morisonModel.row_fluid = row
morisonModel.kinematic_viscosity = kinematic_viscosity
morisonModel.dynamic_viscosity = dynamic_viscosity
screenModel.row_fluid = row
screenModel.kinematic_viscosity = kinematic_viscosity
screenModel.dynamic_viscosity = dynamic_viscosity





# two function used by code_aster
def get_position_aster(table_aster):
    """
    Module public function.\n
    :param table_aster: A table from Code_Aster by ``POST_RELEVE_T`` command with NOM_CHAM=('DEPL')
    :return:  [np.array].shape=(N,3) Unit: [m]. A numpy array of all the nodes positions.
    """
    content = table_aster.EXTR_TABLE()
    original_x = content.values()['COOR_X']
    original_y = content.values()['COOR_Y']
    original_z = content.values()['COOR_Z']
    delta_x = content.values()['DX']
    delta_y = content.values()['DY']
    delta_z = content.values()['DZ']
    position = np.array([original_x, original_y, original_z]) + np.array([delta_x, delta_y, delta_z])
    return np.transpose(position)


def get_velocity_aster(table_aster):  # to get the velocity
    """
    Module public function.\n
    :param table_aster: A table from Code_Aster by ``POST_RELEVE_T`` command with NOM_CHAM=('VITE')
    :return:  [np.array].shape=(N,3) Unit: [m/s]. A numpy array of all the nodes velocities.
    """
    content = table_aster.EXTR_TABLE()
    velocity_x = content.values()['DX']
    velocity_y = content.values()['DY']
    velocity_z = content.values()['DZ']
    velocity = np.array([velocity_x, velocity_y, velocity_z])
    return np.transpose(velocity)




if __name__ == "__main__":
    # test code here
    
    
    pass
